from databases import Database

from app.exceptions import ErrorAddingRepoToSQLite, RemoteRepoNotFound
from app.get_repo_info import get_repo_info
from services.sqlite import insert_data_into_repos


async def add_repo_to_db(db: Database, url: str):
    # imports
    import logging
    from datetime import datetime

    # execution
    data_to_add = get_repo_info(url=url)
    if data_to_add is None:
        logging.error(f"Repo '{url}' not found on GitHub")
        raise RemoteRepoNotFound
    data_to_add["added_date"] = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S")
    try:
        await insert_data_into_repos(db=db, repo=data_to_add)
        return data_to_add
    except Exception as e:
        logging.error(f"EXCEPTION FOUND: {e}")
        raise ErrorAddingRepoToSQLite
