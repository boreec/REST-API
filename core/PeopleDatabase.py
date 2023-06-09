# Author: Cyprien Borée boreec@tuta.io

from core.Person import Person
import sqlite3
from sqlite3 import Error
from collections import OrderedDict


class PeopleDatabase:
    """
    A class representing a database for storing people.
    ivar db_connection: a connection object to the database.
    """

    def __init__(self):
        """
        Initialize a new PeopleDatabase object.
        """

        self.db_connection = self.create_db_connection()
        self.build_table()
        self.create_persons()

    def build_table(self):
        """
        Create a table named "persons" in the database with the following columns:

        - id (text): The unique identifier of the person with the format UUID v4.
        - firstName (text): The first name of the person.
        - lastName (text): The last name of the person.
        - email (text): The email address of the person.
        - birthday (text): The birthday of the person with the format YYYY-MM-DD.
        """

        sql_statement = """
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
        Inserts a new person into the database.

        :param person: The person object to insert.
        :type person: Person
        :raises sqlite3.Error: If an error occurs while inserting the person into the database.
        """
        sql_statement = """
            INSERT INTO persons (id, firstName, lastName, email, birthday) 
                VALUES (?, ?, ?, ?, ?);
        """

        cursor = self.db_connection.cursor()
        cursor.execute(sql_statement, person.to_tuple())
        self.db_connection.commit()

    def create_persons(self):
        """
        Inserts 4 new persons in the database to perform basic operations
        on them during runtime.

        :raises sqlite3.Error: if an error occurs while inserting the person into the database.
        """
        p1 = Person(
            "bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de",
            "John",
            "Doe",
            "johndoe@example.com",
            "1997-01-01",
        )
        p2 = Person(
            "d5356358-b39f-4c6e-9690-2c965a607702",
            "Jane",
            "Doe",
            "janedoe@example.com",
            "1991-07-28",
        )
        p3 = Person(
            "cb2bfa60-e2ae-46ec-ad77-60cf7e8979fd",
            "Brian",
            "Smith",
            "briansmith@example.com",
            "2000-05-10",
        )
        p4 = Person(
            "d82fc695-5ac2-4fed-9387-a7d9c0fb0c4f",
            "Ashley",
            "Yu",
            "ashleyyu@example.com",
            "2003-12-24",
        )
        self.create_person(p1)
        self.create_person(p2)
        self.create_person(p3)
        self.create_person(p4)

    def select_all_persons(self) -> [Person]:
        """
        Selects all persons from the database.

        :return: A list of all persons in the database.
        :rtype: [Person]
        :raises sqlite3.Error: If an error occurs while querying the database.
        """
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM persons;")
        rows = cursor.fetchall()

        persons = []
        for row in rows:
            p = Person(row[0], row[1], row[2], row[3], row[4])
            persons.append(p)

        return persons

    def select_person_by_id(self, id: str) -> Person:
        """
        Selects a person from the database by their id.

        :param id: The id to search for.
        :type id: str
        :return: The person with the specified email address, or None if not found.
        :raises sqlite3.Error: If an error occurs while querying the database.
        """
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM persons WHERE id = ?", (id,))
        row = cursor.fetchone()

        return None if row == None else Person(row[0], row[1], row[2], row[3], row[4])

    def select_person_by_email(self, email: str) -> Person:
        """
        Selects a person from the database by their email address.

        :param email: The email address to search for.
        :type email: str
        :return: The person with the specified email address, or None if not found.
        :raises sqlite3.Error: If an error occurs while querying the database.
        """
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM persons WHERE email = ?", (email,))
        row = cursor.fetchone()

        return None if row == None else Person(row[0], row[1], row[2], row[3], row[4])

    def select_persons_by_name_starting_with(self, name: str) -> [Person]:
        """
        Selects persons from the database whose firstName or lastName starts with a given string.
        If the given string has no match, an empty list is returned.
        If the given string is empty, all persons are returned.

        :param name: The string to match against the beginning of the first name.
        :type name: str
        :return: A list of persons whose firstName or lastName starts with the given string.
        :rtype: [Person]
        :raises sqlite3.Error: If an error occurs while querying the database.
        """
        cursor = self.db_connection.cursor()
        cursor.execute(
            "SELECT * FROM persons WHERE firstName LIKE ? OR lastName LIKE ?;",
            (
                name + "%",
                name + "%",
            ),
        )
        rows = cursor.fetchall()
        persons = []
        for row in rows:
            p = Person(row[0], row[1], row[2], row[3], row[4])
            persons.append(p)

        return persons

    def update_person(self, person: Person):
        """
        Updates a person in the database. An Error is raised if
        the update fails.

        :param person: The person to update.
        :type person: Person
        :raises sqlite.Error
        """
        sql_statement = """
                UPDATE persons
                SET firstname = ?,
                    lastname = ?,
                    email = ?,
                    birthday = ?
                WHERE id = ?;
            """
        cursor = self.db_connection.cursor()
        cursor.execute(
            sql_statement,
            (
                person["firstName"],
                person["lastName"],
                person["email"],
                person["birthday"],
                person["id"],
            ),
        )
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
        cursor.execute("DELETE FROM persons WHERE id = ?;", (person["id"],))
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
