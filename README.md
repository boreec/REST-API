# REST API

This REST API is written in Python with the Flask framework and uses SQLite to store
information in memory.

## How to use ?

### Run the server

```terminal
(user) $ python3 main.py
````

### Call the API

Using `curl`, the following can be done:

Return a 200 response that contains all people in the system.
```terminal
curl -v http://localhost:5000/people/
```

### Tests

To make sure the API works in the way intended, many unit tests were written.
In order to execute unit tests, run the following command.

```terminal
(user) $ ~ python3 -m unittest
```