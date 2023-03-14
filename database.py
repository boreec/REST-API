import sqlite3
from sqlite3 import Error

def create_db_connection():
    db_connection = None
    try:
        db_connection = sqlite3.connect(":memory:")
    except Error as e:
        print(e)
    return db_connection

def build_table(db_connection):
    sql_statement = \
    """
        CREATE TABLE IF NOT EXISTS persons (
            id text PRIMARY KEY,
            firstName text NOT NULL,
            lastName text NOT NULL,
            email text,
            birthday text
        );
    """

    try:
        cursor = db_connection.cursor()
        cursor.execute(sql_statement)
    except Error as e:
        print(e)
    
def create():
    print("Creating database in memory.")
    db_connection = create_db_connection()
    build_table(db_connection)