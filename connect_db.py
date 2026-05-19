from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import urllib.parse  # NEW: Added to handle special characters in passwords

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")

# NEW: This safely encodes the '@' in your password so it doesn't break the URL
encoded_password = urllib.parse.quote_plus(DB_PASSWORD)

DATABASE_URL = (
    f"postgresql://{DB_USER}:{encoded_password}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

try:
    connection = engine.connect()
    print("Connected to Supabase PostgreSQL successfully!")
    connection.close()
except Exception as e:
    print("Connection failed:")
    print(e)