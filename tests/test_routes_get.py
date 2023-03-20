# Author: Cyprien Borée boreec@tuta.io

import unittest
import json
from app import app
from core.routes import *
from datetime import date


class TestRoutesGET(unittest.TestCase):
    """
    A test class for the GET routes of the API.
    """

    def setUp(self):
        """
        Initialize the test client and sets the testing flag to True.
        """
        self.client = app.test_client()
        self.client.testing = True

    def test_get_people(self):
        """
        Tests that the `/people` endpoint returns a status code of 200
        and the list of people.
        """
        result = self.client.get("/people")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(4, len(json.loads(result.data)))

    def test_get_person_by_id_404(self):
        """
        Tests that the `/people/{id}` endpoint returns a 404 error when an
        unknown ID is provided.
        """
        result = self.client.get("/people/unknown-id")
        self.assertEqual(result.status_code, 404)

    def test_get_person_by_id_200(self):
        """
        Tests that the ``/people/{id}` endpoint returns a status code of 200
        and the correct person when a valid ID is provided.
        """
        result = self.client.get("/people/bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(
            "bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de", json.loads(result.data)["id"]
        )

    def test_get_person_age_404(self):
        """
        Tests that the `/people/{id}/age` endpoint returns a 404 error when
        an unknown ID is provided.
        """
        result = self.client.get("/people/unknown-id/age")
        self.assertEqual(result.status_code, 404)

    def test_get_person_age_200(self):
        """
        Tests that the `/people/{id}/age` endpoint returns a status code of 200
        when a valid ID is provided.
        """
        result = self.client.get("/people/bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de/age")
        self.assertEqual(result.status_code, 200)

    def test_get_person_age_200_correct_age(self):
        """
        Tests that the `/people/{id}/age` endpoint returns the correct age for a
        person when a valid ID is provided.
        """
        result = self.client.get("/people/bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de/age")
        self.assertEqual(date.today().year - 1997, int(result.data))

    def test_get_people_with_name_starting_with_j(self):
        """
        Tests that the `/people?name=j` endpoint returns a status code of 200 and a list of
        2 people whose first names start with "J".
        """
        result = self.client.get("/people?name=j")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(2, len(json.loads(result.data)))
        self.assertTrue(json.loads(result.data)[0]["firstName"] == "John")
        self.assertTrue(json.loads(result.data)[1]["firstName"] == "Jane")

    def test_get_people_with_name_starting_with_ja(self):
        """
        Tests that the `/people?name=ja` endpoint returns a status code of 200 and a list of
        1 person whose first name starts with "Ja".
        """
        result = self.client.get("/people?name=ja")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(1, len(json.loads(result.data)))
        self.assertTrue(json.loads(result.data)[0]["firstName"] == "Jane")

    def test_get_people_with_name_starting_with_empty_prefix(self):
        """
        Tests that the `/people?name=`` endpoint returns a status code of 200 and a list of
        everyone in the database.
        """
        result = self.client.get("/people?name=")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(4, len(json.loads(result.data)))
        self.assertTrue(json.loads(result.data)[0]["firstName"] == "John")
        self.assertTrue(json.loads(result.data)[1]["firstName"] == "Jane")
        self.assertTrue(json.loads(result.data)[2]["firstName"] == "Brian")
        self.assertTrue(json.loads(result.data)[3]["firstName"] == "Ashley")

    def test_get_people_with_name_starting_with_unknown_prefix(self):
        """
        Tests that the `/people?name=` endpoint returns a status code of 200 and an
        empty list when the parameter name is set to an unknown prefix.
        """
        result = self.client.get("/people?name=unknown_prefix")
        self.assertEqual(result.status_code, 200)
        self.assertTrue(json.loads(result.data) == [])


if __name__ == "__main__":
    unittest.main()
