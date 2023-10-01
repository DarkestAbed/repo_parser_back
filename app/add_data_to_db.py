import logging
import pdb

from app.exceptions import ErrorAddingRepoToSQLite, RemoteRepoNotFound, RepoAlreadyExistsOnDB, NoTopicOnRepo
from app.get_repo_info import get_repo_info
from services.sqlite import SQLiteDatabase
from services.db.insert_data_into_repos import insert_data_into_repos
from services.db.insert_data_into_topics import insert_data_into_topics


async def add_repo_to_db(db: SQLiteDatabase, url: str):
    # execution
    logging.debug(db)
    data_to_add = get_repo_info(url=url)
    if data_to_add is None:
        logging.error(f"Repo '{url}' not found on GitHub")
        raise RemoteRepoNotFound
    try:
        await insert_data_into_repos(db=db, repo=data_to_add)
        await insert_data_into_topics(db=db, repo=data_to_add)
        # pdb.set_trace()
        return data_to_add
    except RepoAlreadyExistsOnDB:
        logging.error(f"EXCEPTION FOUND: Data from repo '{url}' already exists on SQLite database")
        raise ErrorAddingRepoToSQLite
    except NoTopicOnRepo:
        logging.warn(f"WARNING: No topics found for repo '{url}'")
    except Exception as e:
        logging.error(f"EXCEPTION FOUND: {e}")
        raise Exception(e)
