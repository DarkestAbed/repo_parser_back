import sqlalchemy
from databases import Database

from services.table_definitions.repos import Repos


async def create_base_table(db: Database):
    # imports
    import logging

    # execution
    dialect = sqlalchemy.dialects.sqlite.dialect()
    metadata = sqlalchemy.MetaData()

    repos = Repos(metadata=metadata)

    for table in metadata.tables.values():
        # Set `if_not_exists=False` if you want the query to throw an
        # exception when the table already exists
        schema = sqlalchemy.schema.CreateTable(table, if_not_exists=True)
        query = str(schema.compile(dialect=dialect))
        logging.info(f"Creating table '{table}' if not exists...")
        await db.execute(query=query)


async def insert_data_into_repos(db: Database, repo: dict):
    # imports
    import logging

    # data def
    query = """
        INSERT INTO 
            repositories
            (
                id
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
    query_validation = f"SELECT id FROM repositories WHERE id = {repo['id']}"
    # execution
    # # validating the id does not exists
    logging.info(f"Checking data for repo '{repo['name']}'...")
    result = await db.fetch_one(query=query_validation)
    if not result is None:
        raise Exception("Data already exists on DB")
    # # executing insert
    logging.info(f"Adding data for repo '{repo['name']}'...")
    await db.execute(query=query, values=repo)
