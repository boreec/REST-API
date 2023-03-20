# Author: Cyprien Borée boreec@tuta.io

from datetime import date
from flask import Response, abort, jsonify, request
from app import app, db
from core.Person import Person

import json

@app.route("/people", methods=['GET'])
def get_people():
    """
    Retrieves a list of people from the database.

    If the paramer 'name' is provided, the list of people that
    firstName or lastName starting with the value of this parameter
    is returned.
    
    :param name: The name of the person(s) to retrieve.
    :type name: str
    :returns: A JSON representation of the list of people.
    :rtype: str
    """
    
    args = request.args
    name = args.get('name')
    persons = []
    if name == None:
        persons = db.select_all_persons()
    else:
        persons = db.select_persons_by_name_starting_with(name)
    return Response((json.dumps(persons), '\n'), mimetype='application/json')
    
@app.route("/people/<id>", methods=['GET'])
def get_person_by_id(id):
    """
    Retrieves the person with the specified ID from the database.

    :param id: The ID of the person.
    :type id: str
    :returns: A JSON representation of the person.
    :rtype: str
    :raises 404: If the person with the specified ID is not found in the database.
    """
    
    answer = db.select_person_by_id(id)

    if answer == None :
        abort(404)
    else :
        return Response((json.dumps(answer),'\n'), mimetype='application/json')

@app.route("/people/<id>/age", methods=['GET'])
def get_person_age(id):
    """
    Returns the age of the person with the specified ID.

    :param id: The ID of the person.
    :type id: str
    :returns: A JSON representation of the person's age.
    :rtype: str
    :raises 404: If the person with the specified ID is not found in the database.
    """
    
    person = db.select_person_by_id(id)

    if person == None:
        abort(404)
    else :
        born_year = int(person["birthday"].split('-')[0])
        born_month = int(person["birthday"].split('-')[1])
        born_day = int(person["birthday"].split('-')[2])
        today = date.today()
        age = today.year - born_year - ((today.month, today.day) < (born_month, born_day))
        return jsonify(age)

@app.route("/people", methods=['POST'])
def create_person():
    """
    Creates a person inside the database.

    :returns: a JSON response containing the person details.
    :rtype: flask.Response

    :raises 400: If the request contains invalid data.
    :raises 500: If the query to insert the data failed.   
    """
    
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
    """
    Updates the person with given id in the database.

    :param id: The id of the person to be updated.
    :type id: str
    :returns: A JSON response containing the updated person details.
    :rtype: flask.Response

    :raises 404: If the person with the given id does not exist in the database.
    :raises 400: If the request contains invalid data.

    """    
    
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
    """
    Delete a person from the database by ID.

    :param id: The ID of the person to delete.
    :type id: str
    :return: A JSON response containing the deleted person's information.
    :rtype: flask.Response
    :raises 404: If the person with the specified ID is not found.
    """

    person = db.select_person_by_id(id)

    if person == None :
        abort(404)

    db.delete_person(person)

    return Response((json.dumps(person), "\n"), status=200, mimetype='application/json')