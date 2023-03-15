from collections import OrderedDict
from database import PeopleDatabase
from flask import Flask, Response

import json

app = Flask(__name__)
db = PeopleDatabase()

@app.route("/people", methods=['GET'])
def get_people():
    """
        Return a 200 response that contains all people in the system. 
    """
    rows = db.select_all_persons()
    rows_json = []
    for row in rows:
        # preserve the order of data for the json file
        od = OrderedDict()
        od['id'] = row[0]
        od['firstName'] = row[1]
        od['lastName'] = row[2]
        od['email'] = row[3]
        od['birthday'] = row[4]
        
        rows_json.append(od)
           
    return Response(json.dumps(rows_json), mimetype='application/json')

@app.route("/people/<id>", methods=['GET'])
def get_people_by_id(id):
    """
        Return a 200 response containing the person with the provided
        id, or a 404 response if that person is not in the system.
    """
    answer = db.select_person_by_id(id)

    if len(answer) != 1 :
        flask.abort(404)
    else :
        return Response(json.dumps(answer), mimetype='application/json')

if __name__ == "__main__":
    app.run()