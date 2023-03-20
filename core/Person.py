# Author: Cyprien Borée boreec@tuta.io

from collections import OrderedDict
from datetime import datetime, date
import json
import re

uuid_regex = re.compile('^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z', re.I)
name_regex = re.compile(r'[A-Za-z]{2,50}')
email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

class Person(OrderedDict):
    """
    The `Person` class is a subclass of `OrderedDict` and represents an individual person
    wih the following attributes:
    - `id` a string representing the unique identifier of the person.
    - `firstName` a string representing the first name of the person.
    - `lastName` a string representing the last name of the person.
    - `email` a string representing the email address of the person.
    - `birthday`: a string representing the birth of the person in the format YYYY-MM-DD.      
    """
    
    def __init__(self, id: str, firstName: str, lastName: str, email: str, birthday: str):
        """
        Constructor for the Person class.

        :param id: A string representing the person's ID.
        :type id: str
        :param firstName: A string representing the person's first name.
        :type firstName: str
        :param lastName: A string representing the person's last name.
        :type lastName: str
        :param email: A string representing the person's email.
        :type email: str
        :param birthday: A string representing the person's birthday in the format 'YYYY-MM-DD'.
        :type birthday: str
        """
        super(OrderedDict, self).__init__()
        self['id'] = id
        self['firstName'] = firstName
        self['lastName'] = lastName
        self['email'] = email
        self['birthday'] = birthday

    def to_tuple(self) -> tuple:
        """
        Returns a tuple representation of the person object.

        :return: A tuple of the form (id, firstName, lastName, email, birthday).
        :rtype: tuple   
        """
        return (self['id'], self['firstName'], self['lastName'], self['email'], self['birthday'])     


    def verify_id(self):
        """
        Verify that the 'id' attribute of the Person object is valid.
        It is considered valid if it respects the UUID v4 format.

        :raises Exception: If the 'id' attribute is missing or invalid.
        """
        
        if self['id'] == None:
            raise Exception("Id is missing.")
        if len(self['id']) == 0:
            raise Exception("Invalid id: empty.")
        if not re.fullmatch(uuid_regex, self['id']):
            raise Exception("Invalid id: not compliant with uuid v4 format.")

    def verify_firstName(self):
        """
        Verify that the 'firstName' attribute of the Person object is valid.
        
        :raises Exception: If the 'firstName' attribute is missing or invalid.
        """

        if self['firstName'] == None:
            raise Exception("firstName is missing.")
        if len(self['firstName']) == 0:
            raise Exception("firstName is empty.")
        if not re.fullmatch(name_regex, self['firstName']):
            raise Exception("Invalid firstName: Bad format.")
    
    def verify_lastName(self):
        """
        Verify that the 'lastName' attribute of the Person object is valid.

        :raises Exception: If the 'lastName' attribute is missing or invalid.
        """

        if self['lastName'] == None:
            raise Exception("lastName is missing.")
        if len(self['lastName']) == 0:
            raise Exception("lastName is empty.")
        if not re.fullmatch(name_regex, self['lastName']):
            raise Exception("Invalid lastName: Bad format.")
        
    def verify_email(self):
        """
        Verify that the 'email' attribute of the Person object is valid.

        :raises Exception: If the 'email' attribute is missing or invalid.
        """
        
        if self['email'] == None:
            raise Exception("Email address is missing.")
        if len(self['email']) == 0:
            raise Exception("Invalid email address: empty.")
        if not re.fullmatch(email_regex, self['email']):
            raise Exception("Invalid email address: not compliant with email address format.")

    def verify_birthday(self):
        """
        Verify that the 'birthday' attribute of the Person object is valid.

        :raises Exception: If the 'birthday' attribute is missing or invalid.
        """
        
        if self['birthday'] == None:
            raise Exception("Birthday is missing.")
        try: 
            birthday_date = datetime.strptime(self['birthday'], '%Y-%m-%d').date()
        except Exception as e:
            raise Exception("Invalid birthday: Bad format. Try YYYY-MM-DD.")

        approximate_age = date.today().year - birthday_date.year

        if approximate_age > 150:
            raise Exception("Invalid birthday: {} years old is humanly too old.".format(approximate_age))
        if date.today() < birthday_date :
            raise Exception("Invalid birthday: You can not be born in the future.")

    def verify_data(self) -> str:
        """
        Verify the data entered for a Person object.

        This method calls several other methods to verify the different
        attributes of the Person object: id, firstName, lastName, email and
        birthday. If any of the verification methods raises an exception, the
        error message is concatenated to a string, which is returned at the end
        of the method.

        Returns:
            str: an error message string that contains all the errors raised
                 during the verification process. If there are no errors, the
                 string will be empty.
        """
        
        error_message = ""

        try:
            self.verify_id()
        except Exception as e:
            error_message += e.__str__() + "\n"

        try:
            self.verify_firstName()
        except Exception as e:
            error_message += e.__str__() + "\n"
        
        try:
            self.verify_lastName()
        except Exception as e:
            error_message += e.__str__() + "\n"
        
        try:
            self.verify_email()
        except Exception as e:
            error_message += e.__str__() + "\n"

        try: 
            self.verify_birthday()
        except Exception as e:
            error_message += e.__str__() + "\n"

        return error_message