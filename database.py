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
            id text NOT NULL,
            firstName text NOT NULL,
            lastName text NOT NULL,
            email text NOT NULL,
            birthday text NOT NULL
        );
    """

    try:
        cursor = db_connection.cursor()
        cursor.execute(sql_statement)
    except Error as e:
        print(e)

def create_person(db_connection, person):
    sql_statement = \
    """
        INSERT INTO persons (id, firstName, lastName, email, birthday) 
            VALUES (?, ?, ?, ?, ?);
    """

    cursor = db_connection.cursor()
    cursor.execute(sql_statement, person)
    db_connection.commit()

def create_persons(db_connection):
    p1 = ('bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de','John','Doe','johndoe@example.com','1997-01-01')
    p2 = ('d5356358-b39f-4c6e-9690-2c965a607702','Jane','Doe','janedoe@example.com','1991-07-28')
    p3 = ('cb2bfa60-e2ae-46ec-ad77-60cf7e8979fd','Brian','Smith','briansmith@example.com','2000-05-10') 
    p4 = ('d82fc695-5ac2-4fed-9387-a7d9c0fb0c4f','Ashley','Yu','ashleyyu@example.com','2003-12-24')
    create_person(db_connection, p1)
    create_person(db_connection, p2)
    create_person(db_connection, p3)
    create_person(db_connection, p4)

def select_all_persons(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM persons;")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    
def create():
    print(">> Creating database in memory.")
    db_connection = create_db_connection()
    print(">> Creating table 'persons'")
    build_table(db_connection)
    print(">> Inserting values into 'persons'")
    create_persons(db_connection)
    print(">> Displaying 'persons' table")
    select_all_persons(db_connection)