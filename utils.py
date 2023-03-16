import re

email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def verify_email(address: str):
    if address == None:
        raise Exception("Email address is missing.")
    if len(address) < 4:
        raise Exception("Invalid email address: too short.")
    if not re.fullmatch(email_regex, address):
        raise Exception("Invalid email address: bad format.")    