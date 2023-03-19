from Person import Person
import sqlite3
from sqlite3 import Error
from collections import OrderedDict

class PeopleDatabase():
    """
        Class used for creating a database containing persons
        in memory and handling various queries on the table. 
    """
    def __init__(self):
        """
            Create a connection to the database, build the
            main table and insert persons into it.            
        """
        self.db_connection = self.create_db_connection()
        self.build_table()
        self.create_persons()
        
    def build_table(self):
        """
            Create the 'persons' table with its fields.             
        """
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
            cursor = self.db_connection.cursor()
            cursor.execute(sql_statement)
        except Error as e:
            print(e)
    
    def create_person(self, person: Person):
        """
            Insert a person information inside the 'persons' table. 
        """
        sql_statement = \
        """
            INSERT INTO persons (id, firstName, lastName, email, birthday) 
                VALUES (?, ?, ?, ?, ?);
        """

        cursor = self.db_connection.cursor()
        cursor.execute(sql_statement, person.to_tuple())
        self.db_connection.commit()

    def create_persons(self):
        """
            Define various different persons and insert them inside the
            'persons' table via create_person(). 
        """
        p1 = Person('bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de','John','Doe','johndoe@example.com','1997-01-01')
        p2 = Person('d5356358-b39f-4c6e-9690-2c965a607702','Jane','Doe','janedoe@example.com','1991-07-28')
        p3 = Person('cb2bfa60-e2ae-46ec-ad77-60cf7e8979fd','Brian','Smith','briansmith@example.com','2000-05-10') 
        p4 = Person('d82fc695-5ac2-4fed-9387-a7d9c0fb0c4f','Ashley','Yu','ashleyyu@example.com','2003-12-24')
        self.create_person(p1)
        self.create_person(p2)
        self.create_person(p3)
        self.create_person(p4)

    def select_all_persons(self) -> [Person]:
        """
            Return the entire 'persons' table as a
            list of fields. 
        """
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM persons;")
        rows = cursor.fetchall()

        persons = []
        for row in rows:
            p = Person(row[0], row[1], row[2], row[3], row[4])
            persons.append(p)
            
        return persons

    def select_person_by_id(self, id) -> Person:
        """
            Return a person from the table corresponding to
            a provided id.  
        """
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM persons WHERE id = ?", (id,))
        row = cursor.fetchone()
        
        return None if row == None else Person(row[0],row[1],row[2],row[3],row[4])

    def select_person_by_email(self, email) -> Person:
        """
            Return a person from the table corresponding to
            a provided id.  
        """
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM persons WHERE email = ?", (email,))
        row = cursor.fetchone()

        return None if row == None else Person(row[0],row[1],row[2],row[3],row[4])
    
    def select_persons_by_name_starting_with(self, name) -> [Person]:
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM persons WHERE firstName LIKE ?;", (name+'%',))
        rows = cursor.fetchall()
        persons = []
        for row in rows:
            p = Person(row[0],row[1],row[2],row[3],row[4])
            persons.append(p)
            
        return persons

    def update_person(self, person: Person):
        sql_statement = """
                UPDATE persons
                SET firstname = ?,
                    lastname = ?,
                    email = ?,
                    birthday = ?
                WHERE id = ?;
            """
        cursor = self.db_connection.cursor()
        cursor.execute(sql_statement, (person['firstName'],person['lastName'],person['email'],person['birthday'], person['id']))
        self.db_connection.commit()

    def delete_person(self, person: Person) -> Person:
        """
        Deletes a person from the database. If the deletion is successful, the deleted
        person is returned, otherwise an Error is raised.

        :param person: The person to delete.
        :type person: Person
        :raises sqlite3.Error: If an error occurs while deleting the person.
        """
        cursor = self.db_connection.cursor()
        cursor.execute("DELETE FROM persons WHERE id = ?;", (person['id'],))
        self.db_connection.commit()
        
    def create_db_connection(self):
        """
        Create a database connection to a in-memory database.
        The database will only be active during the runtime of the program.
        All data are created at runtime and deleted after execution.

        :return: A database connection object.
        :rtype: sqlite3.Connection
        :raises Error: If the connection cannot be established. 
        """
        db_connection = None
        try:
            db_connection = sqlite3.connect(":memory:", check_same_thread=False)
        except Error as e:
            print(e)
        return db_connection


