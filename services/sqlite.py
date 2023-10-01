import logging
from databases import Database


class SQLiteDatabase:
    def __init__(self, conn_string: str):
        # data def
        self.db_path = conn_string
        self.conn_string = f"sqlite+aiosqlite:///{conn_string}"
    
    def create_db_if_not_exists(self):
        # imports
        import sqlite3
        from app.exceptions import NoSQLiteDatabase

        # execution
        try:
            logging.info("Creating SQLite DB if needed...")
            conn = sqlite3.connect(database=self.db_path)
            logging.debug(conn)
        except Exception as e:
            logging.exception("EXCEPTION - Exception found: {e}")
            logging.error("Cannot create SQLite database.")
            raise NoSQLiteDatabase
        if conn:
            conn.close()
            logging.debug(conn)
            self.database = Database(self.conn_string)
            logging.debug(self.database)
        return None
    
    async def connect_db(self):
        # imports
        from services.db.create_base_tables import create_base_table

        # execution
        self.create_db_if_not_exists()
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
