import logging

from services.sqlite import SQLiteDatabase


async def check_if_data_exists(db: SQLiteDatabase, id_db: int):
    # data def
    query = f"SELECT id FROM repositories WHERE id = {id_db}"
    logging.debug(db)
    logging.debug(query)

    # execution
    result = await db.get_one(query=query)
    result_bool = False if result is None else True
    logging.debug(result_bool)
    logging.debug(f"Is the data present?: {result_bool}")
    return result_bool
