import logging
from databases import Database


class SQLiteDatabase:
    def __init__(self, conn_string: str):
        # data def
        self.conn_string = conn_string
        self.database = Database(self.conn_string)
    
    async def connect_db(self):
        # imports
        from services.db.create_base_tables import create_base_table

        # execution
        logging.info("Connecting to SQLite database...")
        await self.database.connect()
        logging.info("Creating tables if needed...")
        await create_base_table(db=self.database)
    
    async def disconnect_db(self):
        # execution
        logging.info("Disconnecting from SQLite database...")
        await self.database.disconnect()
    
    async def get_one(self, query: str):
        # execution
        result = await self.database.fetch_val(query=query)
        logging.debug(result)
        return result
    
    async def get_all(self, query: str):
        # execution
        result = await self.database.fetch_all(query=query)
        logging.debug(result)
        return result
    
    async def execute(self, query: str, values: dict):
        # execution
        logging.debug(query)
        logging.debug(values)
        await self.database.execute(query=query, values=values)
