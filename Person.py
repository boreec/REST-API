from collections import OrderedDict
from datetime import datetime, date
import json
import re

uuid_regex = re.compile('^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z', re.I)
name_regex = re.compile(r'[A-Za-z]{2,50}')
email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

class Person(OrderedDict):
    
    def __init__(self, id: str, firstName: str, lastName: str, email: str, birthday: str):
        super(OrderedDict, self).__init__()
        self['id'] = id
        self['firstName'] = firstName
        self['lastName'] = lastName
        self['email'] = email
        self['birthday'] = birthday

    def to_tuple(self) -> tuple:
        return (self['id'], self['firstName'], self['lastName'], self['email'], self['birthday'])     


    def verify_id(self):
        if self['id'] == None:
            raise Exception("Id is missing.")
        if len(self['id']) == 0:
            raise Exception("Invalid id: empty.")
        if not re.fullmatch(uuid_regex, self['id']):
            raise Exception("Invalid id: not compliant with uuid v4 format.")

    def verify_firstName(self):
        if self['firstName'] == None:
            raise Exception("firstName is missing.")
        if len(self['firstName']) == 0:
            raise Exception("firstName is empty.")
        if not re.fullmatch(name_regex, self['firstName']):
            raise Exception("Invalid firstName: Bad format.")
    
    def verify_lastName(self):
        if self['lastName'] == None:
            raise Exception("lastName is missing.")
        if len(self['lastName']) == 0:
            raise Exception("lastName is empty.")
        if not re.fullmatch(name_regex, self['lastName']):
            raise Exception("Invalid lastName: Bad format.")
        
    def verify_email(self):
        if self['email'] == None:
            raise Exception("Email address is missing.")
        if len(self['email']) == 0:
            raise Exception("Invalid email address: empty.")
        if not re.fullmatch(email_regex, self['email']):
            raise Exception("Invalid email address: not compliant with email address format.")

    def verify_birthday(self):
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