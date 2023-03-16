from datetime import date
from flask import Response, abort, jsonify
from __main__ import app, db

import json

@app.route("/people", methods=['GET'])
def get_people():
    """
        Return a 200 response that contains all people in the system. 
    """
    persons = db.select_all_persons()
    return Response((json.dumps(persons), '\n'), mimetype='application/json')

@app.route("/people/<id>", methods=['GET'])
def get_person_by_id(id):
    """
        Return a 200 response containing the person with the provided
        id, or a 404 response if that person is not in the system.
    """
    answer = db.select_person_by_id(id)

    if answer == None :
        abort(404)
    else :
        return Response((json.dumps(answer),'\n'), mimetype='application/json')

@app.route("/people/<id>/age", methods=['GET'])
def get_person_age(id):
    """
        Identify a person by a provided it, calculate and return a 200 of its age.
        A 404 response is returned if that person is not in the system.
    """
    answer = db.select_person_by_id(id)

    if answer == None:
        abort(404)
    else :
        born_year = int(answer["birthday"].split('-')[0])
        born_month = int(answer["birthday"].split('-')[1])
        born_day = int(answer["birthday"].split('-')[2])
        today = date.today()
        age = today.year - born_year - ((today.month, today.day) < (born_month, born_day))
        return jsonify(age)
