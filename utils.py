from datetime import datetime, date
from __main__ import db
import re

uuid_regex = re.compile('^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z', re.I)
name_regex = re.compile(r'[A-Za-z]{2,50}')
email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def verify_id(id: str):
    if id == None:
        raise Exception("Id is missing.")
    if len(id) == 0:
        raise Exception("Invalid id: empty.")
    if not re.fullmatch(uuid_regex, id):
        raise Exception("Invalid id: not compliant with uuid v4 format.")

def verify_name(name: str):
    if name == None:
        raise Exception("Name is missing.")
    if len(name) == 0:
        raise Exception("Name is empty.")
    if not re.fullmatch(name_regex, name):
        raise Exception("Invalid name: Bad format.")
        
def verify_email(address: str):
    if address == None:
        raise Exception("Email address is missing.")
    if len(address) == 0:
        raise Exception("Invalid email address: empty.")
    if not re.fullmatch(email_regex, address):
        raise Exception("Invalid email address: not compliant with email address format.")

def verify_birthday(birthday: str):
    if birthday == None:
        raise Exception("Birthday is missing.")
    try: 
        birthday_date = datetime.strptime(birthday, '%Y-%m-%d').date()
    except Exception as e:
        raise Exception("Invalid birthday: Bad format. Try YYYY-MM-DD.")

    approximate_age = date.today().year - birthday_date.year

    if approximate_age > 150:
        raise Exception("Invalid birthday: {} years old is humanly too old.".format(approximate_age))
    if date.today() < birthday_date :
        raise Exception("Invalid birthday: You can not be born in the future.")

def verify_data(id, firstName, lastName, email, birthday) -> str:
    error_message = ""

    try:
        verify_id(id)
    except Exception as e:
        error_message += e.__str__() + "\n"

    try:
        verify_name(firstName)
    except Exception as e:
        error_message += e.__str__() + "\n"

    try:
        verify_name(lastName)
    except Exception as e:
        error_message += e.__str__() + "\n"
        
    try:
        verify_email(email)
    except Exception as e:
        error_message += e.__str__() + "\n"

    try: 
        verify_birthday(birthday)
    except Exception as e:
        error_message += e.__str__() + "\n"

    similar_email = db.select_person_by_email(email)
    if similar_email != None:
        error_message += "Invalid email: '{}' already exists in the database.\n".format(email)   

    return error_message