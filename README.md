# REST API

This REST API is written in Python with the Flask framework and uses SQLite to store
information in memory.

For this example, the dabase contains a list of 4 persons with the following fields:
- `id` : text (UUID version 4) 
- `firstName` : text
- `lastName` : text
- `email` : text (with format a@b.cd)
- `birthday` : text (compliant with ISO 8601 like '2022-01-01')

## How to use ?

### Install the requirements

It is recommended to create a virtual environment at first:

```terminal
python3 -m venv api_env  
```

Once the command completes, activate the virtual environment by running
the appropriate command for your operating system:

On Windows:

```terminal
api_env\Scripts\activate.bat
```

On Unix or Linux:

```terminal
source api_env/bin/activate
```

The virtual environment should be activated, and you can install packages and run
Python scripts within it.

To install the required packages into your virtual environment, navigate to the
directory where you cloned this repository and use the `pip` command.

```terminal
pip install -r requirements.txt
```

This will install all the packages listed in the `requirements.txt` file. If any packages
are already installed, `pip` will skip them and move on to the next one. If you encounter 
any errors during the installation process, make sure to check the output for any error 
messages and resolve them accordingly. 

### Run the server

The entry point of the server is located in the file `app.py`.

```terminal
python3 app.py
````

### Call the API endpoints

Once the server is launched, the API can be queried through many RESTful routes.
Note that all data received from the endpoints or the data sent to the endpoints
is in a JSON format with the mimetype `application/JSON`.

#### route GET /people
The route `GET /people` has a 200 response that contains all people in the system
as a JSON format.

For example:
```terminal
$ curl http://localhost:5000/people
[{"id": "bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de", "firstName": "John", "lastName": "Doe", "email": "johndoe@example.com", "birthday": "1997-01-01"}, {"id": "d5356358-b39f-4c6e-9690-2c965a607702", "firstName": "Jane", "lastName": "Doe", "email": "janedoe@example.com", "birthday": "1991-07-28"}, {"id": "cb2bfa60-e2ae-46ec-ad77-60cf7e8979fd", "firstName": "Brian", "lastName": "Smith", "email": "briansmith@example.com", "birthday": "2000-05-10"}, {"id": "d82fc695-5ac2-4fed-9387-a7d9c0fb0c4f", "firstName": "Ashley", "lastName": "Yu", "email": "ashleyyu@example.com", "birthday": "2003-12-24"}]
```

#### route GET /people/:id

The route `GET /people/:id` has a 200 response containing the requested person or a
404 response if the person does not exist.

For example:
```terminal
$ curl http://localhost:5000/people/bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de
{"id": "bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de", "firstName": "John", "lastName": "Doe", "email": "johndoe@example.com", "birthday": "1997-01-01"}

$ curl http://localhost:5000/people/qsdqsdqoisudoiaze
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
```

#### route GET /people/:id/age

The route `GET /people/:id/age` has a 200 response containing the age of the person on the current date, 
or a 404 response if the person does not exist.

For example (command ran on march 20th 2023):
```terminal
$ curl http://localhost:5000/people/bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de/age
26

$ curl http://localhost:5000/people/qsdqsdqoisudoiaze/age
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
```

#### route GET /people?name=:name

The route `GET /people?name=:name` has a 200 response that contains the people whose first or last name
meets the search criterial. If there are no results, an empty array is returned. if the parameter is provided
but empty, all the persons are returned.

For example:
```terminal
$ curl http://localhost:5000/people?name=j
[{"id": "bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de", "firstName": "John", "lastName": "Doe", "email": "johndoe@example.com", "birthday": "1997-01-01"}, {"id": "d5356358-b39f-4c6e-9690-2c965a607702", "firstName": "Jane", "lastName": "Doe", "email": "janedoe@example.com", "birthday": "1991-07-28"}]

$ curl http://localhost:5000/people?name=
[{"id": "bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de", "firstName": "John", "lastName": "Doe", "email": "johndoe@example.com", "birthday": "1997-01-01"}, {"id": "d5356358-b39f-4c6e-9690-2c965a607702", "firstName": "Jane", "lastName": "Doe", "email": "janedoe@example.com", "birthday": "1991-07-28"}, {"id": "cb2bfa60-e2ae-46ec-ad77-60cf7e8979fd", "firstName": "Brian", "lastName": "Smith", "email": "briansmith@example.com", "birthday": "2000-05-10"}, {"id": "d82fc695-5ac2-4fed-9387-a7d9c0fb0c4f", "firstName": "Ashley", "lastName": "Yu", "email": "ashleyyu@example.com", "birthday": "2003-12-24"}]

$ curl http://localhost:5000/people?name=sqdl
[]
```

#### route POST /people

The route `POST /people` creates a person and returns a 200 response with the created person if the creation is successful, or 400 response if there is a problem
with the data provided. Typically, a 400 response will be generated in the following cases:
- An `id` field is provided: It's not possible to change a person's id, it's unique.
- The `firstName` and/or `lastName` provided field has invalid format (empty, containing numbers or special characters, etc.).
- The `email` provided field has incorrect format (it must be like foo@bar.com).
- The `email` provided field has correct format but is already taken by another user.
- The `birthday` provided field has incorrect format (should be YYYY-MM-DD with a possible date).

Note that the data must be provided in a dictionary format with a mimetype `application/json`.
For example:
```terminal
$ curl -X POST http://localhost:5000/people -H "Content-Type: application/json" -d '{"id":"051dfab3-e834-4169-a67c-830da19af9d9", "firstName":"Matthew", "lastName":"Smith", "email":"mattewsmith@example.com", "birthday":"2000-03-01"}'
{"id": "051dfab3-e834-4169-a67c-830da19af9d9", "firstName": "Matthew", "lastName": "Smith", "email": "mattewsmith@example.com", "birthday": "2000-03-01"}
```

If you try to repeat the command, an error will be raised:
```terminal
Person with similar id already exist in database.
```

#### route PUT /people/:id

The route `PUT /people/:id` will update a person with the provided id. It returns a 200
response and the updated person on success, a 400 response if the provided information are incorrect,
 and a 404 response if the person is not found.

For example:
```terminal
$ curl -X PUT http://localhost:5000/people/bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de -H "Content-Type: application/json" -d '{"firstName":"Peter"}'
{"id": "bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de", "firstName": "Peter", "lastName": "Doe", "email": "johndoe@example.com", "birthday": "1997-01-01"}
```

#### route DELETE /people:id

The route `DELETE /people/:id` deletes a person with the provided id. It returns a 200 response and the deleted person
on success, or a 404 response if the person does not exists.
For example:
```terminal
curl -X DELETE http://localhost:5000/people/bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de
{"id": "bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de", "firstName": "Peter", "lastName": "Doe", "email": "johndoe@example.com", "birthday": "1997-01-01"}
```

You can verify the person is not anymore in the system with a GET request on `/people`.
```terminal
$ curl http://localhost:5000/people
[{"id": "d5356358-b39f-4c6e-9690-2c965a607702", "firstName": "Jane", "lastName": "Doe", "email": "janedoe@example.com", "birthday": "1991-07-28"}, {"id": "cb2bfa60-e2ae-46ec-ad77-60cf7e8979fd", "firstName": "Brian", "lastName": "Smith", "email": "briansmith@example.com", "birthday": "2000-05-10"}, {"id": "d82fc695-5ac2-4fed-9387-a7d9c0fb0c4f", "firstName": "Ashley", "lastName": "Yu", "email": "ashleyyu@example.com", "birthday": "2003-12-24"}, {"id": "051dfab3-e834-4169-a67c-830da19af9d9", "firstName": "Matthew", "lastName": "Smith", "email": "mattewsmith@example.com", "birthday": "2000-03-01"}]
```

### Tests

To make sure the API works in the way intended, many unit tests were written.
The unit tests are contained by files in the `tests` folder.
In order to execute them, run the following command.

```terminal
python3 -m unittest discover -s tests
```