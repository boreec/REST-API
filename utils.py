import re

uuid_regex = re.compile('^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z', re.I)
email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def verify_id(id: str):
    if id == None:
        raise Exception("Id is missing.")
    if len(id) == 0:
        raise Exception("Invalid id: empty.")
    if not re.fullmatch(uuid_regex, id):
        raise Exception("Invalid id: not compliant with uuid v4 format.")
    
def verify_email(address: str):
    if address == None:
        raise Exception("Email address is missing.")
    if len(address) == 0:
        raise Exception("Invalid email address: empty.")
    if not re.fullmatch(email_regex, address):
        raise Exception("Invalid email address: not compliant with email address format.")  