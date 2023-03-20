# Author: Cyprien Borée boreec@tuta.io

from core.PeopleDatabase import PeopleDatabase
from flask import Flask

app = Flask(__name__)
"""
Flask application instance. 
"""

db = PeopleDatabase()
"""
Database instance used by the application.  
"""

from core.routes import *
"""
Import the Flask routes from the routes 'module'.  
"""

if __name__ == "__main__":
    app.run()