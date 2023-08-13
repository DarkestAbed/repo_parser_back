import logging
import sqlalchemy
from databases import Database

from services.table_definitions.repos import Repos


async def create_base_table(db: Database):
    # execution
    dialect = sqlalchemy.dialects.sqlite.dialect()
    metadata = sqlalchemy.MetaData()
    repos = Repos(metadata=metadata)
    logging.debug(repos)
    for table in metadata.tables.values():
        # Set `if_not_exists=False` if you want the query to throw an
        # exception when the table already exists
        schema = sqlalchemy.schema.CreateTable(table, if_not_exists=True)
        query = str(schema.compile(dialect=dialect))
        logging.info(f"Creating table '{table}' if not exists...")
        await db.execute(query=query)
