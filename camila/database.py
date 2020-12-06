import os
import logging

import aiosqlite3


class DatabaseConnector:
    def __init__(self):
        self.db = None

    async def load_db(self, db_name, loop):
        if not os.path.isfile(db_name):
            logging.info(f"Creating new database: {db_name}")
            with open("schema.sql", "r", encoding="utf-8") as f:
                schema = f.read()
            self.db = await aiosqlite3.connect(db_name, loop=loop)
            await self.db.executescript(schema)
            await self.db.commit()
            logging.info(f"Database initialized: {db_name}")
        else:
            self.db = await aiosqlite3.connect(db_name, loop=loop)
            logging.info(f"Database loaded: {db_name}")

    async def __aenter__(self):
        self.db.__enter__()
        cursor = await self.db.cursor()
        return cursor

    async def __aexit__(self, exc_class, exc, traceback):
        self.db.__exit__(exc_class, exc, traceback)
        if self.db.in_transaction:
            await self.db.commit()
