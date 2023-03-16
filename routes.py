from datetime import date
from flask import Response, abort, jsonify, request
from __main__ import app, db

import json

@app.route("/people", methods=['GET'])
def get_people():
    """
        Return a 200 response that contains all people in the system. 
    """
    args = request.args
    name = args.get('name')
    persons = []
    if name == None:
        persons = db.select_all_persons()
    else:
        persons = db.select_persons_by_name(name)
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

@app.route("/people", methods=['POST'])
def create_person():
    id = request.json.get("id")
    firstName = request.json.get("firstName")
    lastName = request.json.get("lastName")
    email = request.json.get("email")
    birthday = request.json.get("birthday")

    error_msg = ""
    if id == None :
        error_msg += "Missing 'id' field.\n"
    if firstName == None :
        error_msg += "Missing 'firstName' field.\n"
    if lastName == None :
        error_msg += "Missing 'lastName' field.\n"
    if birthday == None :
        error_msg += "Missing 'birthday' field.\n"
    if email == None:
        error_msg += "Missing 'email' field.\n"

    if len(error_msg) > 0:
        return Response(error_msg, 400)
    
    return ""