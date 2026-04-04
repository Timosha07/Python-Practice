# connect.py
import psycopg2
from config import DB_PARAMS

def get_connection():
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        return conn
    except Exception as e:
        print(f"Ошибка подключения: {e}")
        return None