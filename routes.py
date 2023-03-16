from datetime import date
from flask import Response, abort, jsonify, request
from utils import *
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
        error_message = "Invalid email: '{}' already exists in the database.\n".format(email)   
    if len(error_message) > 0:
        return Response(error_message, 400)

    try:
        inserted_person = (id, firstName, lastName, email, birthday)
        db.create_person(inserted_person)
        retrieved_person = db.select_person_by_id(id)
        return Response((json.dumps(retrieved_person), '\n'), status=200, mimetype='application/json')
    except Exception as e:
        return Response('Failed inserting verified data into database: {}\n'.format(e), status=500)