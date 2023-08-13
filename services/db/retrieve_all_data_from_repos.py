import logging

from app.exceptions import NoDataOnRepoDatabase
from services.sqlite import SQLiteDatabase


async def get_all_repo_data(db: SQLiteDatabase):
    # data def
    query = f"SELECT * FROM repositories"
    logging.debug(db)
    logging.debug(query)

    # execution
    result = await db.get_all(query=query)
    result_bool = False if result is None else True
    logging.debug(result_bool)
    logging.debug(f"Is some data present?: {result_bool}")
    if not result_bool:
        raise NoDataOnRepoDatabase
    else:
        return result
