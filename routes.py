from datetime import date
from flask import Response, abort, jsonify, request
from __main__ import app, db
from Person import Person

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

    person = Person(
        request.json['id'],
        request.json['firstName'],
        request.json['lastName'],
        request.json['email'],
        request.json['birthday']
    )
    
    error_message = person.verify_data()

    if len(error_message) > 0:
        return Response(error_message, 400)

    if db.select_person_by_id(person['id']) != None :
        return Response("Person with similar id already exist in database.", 400)
    if db.select_person_by_email(person['email']) != None :
        return Response("Person with similar email already exist in database.", 400)
    
    try:
        db.create_person(person)
        return Response((json.dumps(person), '\n'), status=200, mimetype='application/json')
    except Exception as e:
        return Response('Failed inserting verified data into database: {}\n'.format(e), status=500)

@app.route("/people/<id>", methods=['PUT'])
def update_person(id):
    
    person = db.select_person_by_id(id)

    if person == None :
        abort(404)
    
    if request.json.get('id') != None :
        return Response('Impossible to update someone\'s id, as one is linked per user.\n', 400)
    if request.json.get('email') != None :
        if db.select_person_by_email(request.json['email']) != None :
            return Response('Impossible to update that person with that email, someone already has this email registered in database.\n', 400)
        else:
            person['email'] = request.json['email']

    person['firstName'] = request.json['firstName'] if request.json.get('firstName') != None else person['firstName']
    person['lastName'] = request.json['lastName'] if request.json.get('lastName') != None else person['lastName']
    person['birthday'] = request.json['birthday'] if request.json.get('birthday') != None else person['birthday']

    error_message = person.verify_data()

    if len(error_message) > 0 :
        return Response(error_message, 400)

    db.update_person(person)
    return Response((json.dumps(person), '\n'), status=200, mimetype='application/json')

@app.route("/people/<id>", methods=['DELETE'])
def delete_person(id):
    person = db.select_person_by_id(id)

    if person == None :
        abort(404)

    db.delete_person(person)

    return Response((json.dumps(person), "\n"), status=200, mimetype='application/json')