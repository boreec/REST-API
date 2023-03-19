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

The API has the following endpoints:

The route GET `/people` has a 200 response that contains all people in the system
as a JSON format.

For example:
```terminal
$ curl http://localhost:5000/people
[{"id": "bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de", "firstName": "John", "lastName": "Doe", "email": "johndoe@example.com", "birthday": "1997-01-01"}, {"id": "d5356358-b39f-4c6e-9690-2c965a607702", "firstName": "Jane", "lastName": "Doe", "email": "janedoe@example.com", "birthday": "1991-07-28"}, {"id": "cb2bfa60-e2ae-46ec-ad77-60cf7e8979fd", "firstName": "Brian", "lastName": "Smith", "email": "briansmith@example.com", "birthday": "2000-05-10"}, {"id": "d82fc695-5ac2-4fed-9387-a7d9c0fb0c4f", "firstName": "Ashley", "lastName": "Yu", "email": "ashleyyu@example.com", "birthday": "2003-12-24"}]
```

The route GET `/people/:id` has a 200 response containing the requested person or a
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

### Tests

To make sure the API works in the way intended, many unit tests were written.
The unit tests are contained by files in the `tests` folder.
In order to execute them, run the following command.

```terminal
python3 -m unittest discover -s tests
```