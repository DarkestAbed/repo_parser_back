import sqlalchemy
from databases import Database

from services.table_definitions.repos import Repos
from app.exceptions import ErrorAddingRepoToSQLite


async def create_base_table(db: Database):
    # imports
    import logging

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


async def check_if_data_exists(db: Database, id_db: int):
    # imports
    import logging

    # data def
    query_validation = f"SELECT id FROM repositories WHERE id = {id_db}"

    # execution
    result = await db.fetch_val(query=query_validation)
    logging.debug(result)
    result_bool = False if result is None else True
    logging.debug(result_bool)
    logging.debug(f"Is the data present?: {result_bool}")
    if result is None:
        return False
    else:
        return True


async def insert_data_into_repos(db: Database, repo: dict):
    # imports
    import logging

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

    # execution
    logging.info(f"Checking data for repo '{repo['name']}'...")
    if await check_if_data_exists(db=db, id_db=repo["id"]):
        raise ErrorAddingRepoToSQLite
    # # executing insert
    logging.info(f"Adding data for repo '{repo['name']}'...")
    await db.execute(query=query, values=repo)
