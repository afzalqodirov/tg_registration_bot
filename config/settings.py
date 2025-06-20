from dotenv import load_dotenv
from os import getenv

load_dotenv()
db_name = str(getenv('DB_NAME'))
BOT_TOKEN = str(getenv('BOT_TOKEN'))