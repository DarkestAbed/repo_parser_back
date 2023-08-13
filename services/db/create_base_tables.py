import logging
import sqlalchemy

from services.sqlite import SQLiteDatabase
from services.table_definitions.repos import Repos
from services.table_definitions.topics import Topics


async def create_base_table(db: SQLiteDatabase):
    # execution
    dialect = sqlalchemy.dialects.sqlite.dialect()
    metadata = sqlalchemy.MetaData()
    repos = Repos(metadata=metadata)
    topics = Topics(metadata=metadata)
    logging.debug(repos)
    logging.debug(topics)
    for table in metadata.tables.values():
        # Set `if_not_exists=False` if you want the query to throw an
        # exception when the table already exists
        schema = sqlalchemy.schema.CreateTable(table, if_not_exists=True)
        query = str(schema.compile(dialect=dialect))
        logging.info(f"Creating table '{table}' if not exists...")
        await db.execute(query=query)
