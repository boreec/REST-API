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