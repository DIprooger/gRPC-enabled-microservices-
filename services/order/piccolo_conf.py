from piccolo.engine.postgres import PostgresEngine
from dotenv import load_dotenv
import os

load_dotenv()

DB = PostgresEngine(config={
    "database": os.getenv('DB_NAME_POS'),
    "user": os.getenv('DB_USER_POS'),
    "password": os.getenv('DB_PASSWORD_POS'),
    "host": os.getenv("DB_HOST_POS"),
    "port": int(os.getenv("DB_PORT_POS"))
})

