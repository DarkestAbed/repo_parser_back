from typing import Union
from fastapi import FastAPI, HTTPException
from app.get_repo_info import get_repo_info_raw
from utils.parse_urls import parse_url
from utils.check_for_gh import check_for_gh
from utils.get_jsons import get_responses
from icecream import ic
import sys

init_test = check_for_gh()

if init_test:
    print("All dependencies found.")
    app = FastAPI()
    url_get_responses = get_responses()
else:
    print("Missing dependencies on local. Exiting now...")
    sys.exit(1)


@app.get("/")
def read_root():
    return {"Message": "This is a nice app that gets some GitHub repo info"}


@app.get("/repos/{url}", responses=url_get_responses)
def read_url(url: Union[str, None] = None):
    if url is None:
        raise HTTPException(status_code=400, detail="No repo URL provided")
    ic(url)
    repo_location = parse_url(url=url)
    repo_data = get_repo_info_raw(repo_location=repo_location)
    if repo_data is None:
        raise HTTPException(status_code=404, detail=f"Repo {repo_location} not found")
    else:
        return repo_data
