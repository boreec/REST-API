from database import PeopleDatabase
from flask import Flask

app = Flask(__name__)
db = PeopleDatabase()

from routes import *

if __name__ == "__main__":
    app.run()