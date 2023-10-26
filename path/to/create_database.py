import sqlite3
from sqlite3 import Error

def create_database(db_name):
    conn = None;
    try:
        conn = sqlite3.connect(db_name)
        print(f"SQLite database {db_name} created")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

create_database("db1.db")