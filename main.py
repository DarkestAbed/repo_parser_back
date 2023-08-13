import logging
import os
import sys
from typing import Union

from fastapi import FastAPI, HTTPException

from app.add_data_to_db import add_repo_to_db
from app.exceptions import ErrorAddingRepoToSQLite, RemoteRepoNotFound
from app.get_all_local_data import get_all_repo_data
from app.get_repo_info import get_repo_info
from services.sqlite import SQLiteDatabase
from services.read_env import read_environ

from utils.check_for_gh import check_for_gh
from utils.get_jsons import get_responses
from utils.parse_urls import parse_url

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

url_get_responses = get_responses(call="get")
url_post_responses = get_responses(call="put")
read_environ()

app = FastAPI(
    title="RepoParser Backend v0.0.1",
    summary="""
        Local app to store all your non-starred GitHub repos.
        This application is the Python backend (built with FastAPI) for a local store for your
        GitHub non-starred repos. It will provide a front-end interface so you can see some repo
        information, such as last updated, topics, and repo description and domain.
        """,
    version="0.0.1",
)
database = SQLiteDatabase(conn_string=os.getenv("SQLITE_PATH"))
logging.debug(database)


@app.on_event("startup")
async def check_dependencies():
    init_test = check_for_gh()
    if init_test:
        logging.info("All dependencies found.")
        await database.connect_db()
    else:
        logging.info("Missing dependencies on local. Exiting now...")
        sys.exit(1)


@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect_db()


@app.get("/")
def read_root():
    return {"message": "This is a nice app that gets some GitHub repo info"}


@app.get("/get-remote-repo/{url}", responses=url_get_responses)
def read_url(url: Union[str, None] = None):
    if url is None:
        raise HTTPException(status_code=400, detail="No repo URL provided")
    repo_location = parse_url(url=url)
    try:
        repo_data = get_repo_info(url=repo_location)
    except RemoteRepoNotFound:
        raise HTTPException(status_code=404, detail=f"Repo '{repo_location}' not found")
    else:
        return repo_data


@app.get("/get-local-repos/")
async def read_all_repos_from_local():
    try:
        repo_data = await get_all_repo_data(db=database)
        if repo_data is None:
            raise HTTPException(status_code=501, detail=f"No repo data on database")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching repo data")
    else:
        return repo_data


@app.post("/put-new-repo/{url}", responses=url_post_responses)
async def insert_repo(url: str):
    repo_location = parse_url(url=url)
    try:
        data_to_add = get_repo_info(url=repo_location)
        logging.debug(data_to_add)
        logging.debug(database)
        await add_repo_to_db(db=database, url=repo_location)
        logging.info(f"Repo '{repo_location}' added to SQLite database")
        return data_to_add
    except RemoteRepoNotFound as e:
        raise HTTPException(
            status_code=403,
            detail=f"Repo '{repo_location}' not found and cannot be added",
        )
    except ErrorAddingRepoToSQLite as e:
        raise HTTPException(status_code=503, detail="Error adding the repo to database")
