import psycopg2
from config import load_config

def connect():
    config = load_config()
    try:
        conn = psycopg2.connect(**config)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)