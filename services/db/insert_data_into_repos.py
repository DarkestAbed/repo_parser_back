import logging
from datetime import datetime

from services.sqlite import SQLiteDatabase
from services.db.check_if_data_exist import check_if_data_exists
from app.exceptions import RepoAlreadyExistsOnDB


async def insert_data_into_repos(db: SQLiteDatabase, repo: dict):
    # data def
    query = """
        INSERT INTO 
            repositories
            (
                id
                ,url
                ,name
                ,created_at
                ,updated_at
                ,pushed_at
                ,description
                ,fork
                ,disabled
                ,homepage
                ,language
                ,private
                ,visibility
                ,default_branch
                ,topics
                ,added_date
            )
        VALUES
            (
                :id
                ,:url
                ,:name
                ,:created_at
                ,:updated_at
                ,:pushed_at
                ,:description
                ,:fork
                ,:disabled
                ,:homepage
                ,:language
                ,:private
                ,:visibility
                ,:default_branch
                ,:topics
                ,:added_date
            )
    """
    repo["added_date"] = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S")

    # execution
    logging.info(f"Checking data for repo '{repo['name']}'...")
    if await check_if_data_exists(db=db, id_db=repo["id"]):
        raise RepoAlreadyExistsOnDB
    # # executing insert
    logging.info(f"Adding data for repo '{repo['name']}'...")
    await db.execute(query=query, values=repo)
