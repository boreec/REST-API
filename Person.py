class Person():

    def __init__(self, id: str, firstName: str, lastName: str, email: str, birthday: str):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.birthday = birthday

    def to_tuple(self) -> tuple:
        return (self.id, self.firstName, self.lastName, self.email, self.birthday)     
