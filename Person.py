from collections import OrderedDict
import json

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

