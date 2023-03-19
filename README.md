# REST API

This REST API is written in Python with the Flask framework and uses SQLite to store
information in memory.

## How to use ?

### Run the server

```terminal
python3 main.py
````

### Call the API

Using `curl`, the following can be done:

Return a 200 response that contains all people in the system.
```terminal
curl -v http://localhost:5000/people/
```

### Tests

To make sure the API works in the way intended, many unit tests were written.
The unit tests are contained by files in the `tests` folder.
In order to execute them, run the following command.

```terminal
python3 -m unittest discover -s tests
```