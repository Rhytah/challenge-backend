import os
import unittest
import json
from api import create_app as app


class InuTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app()
        self.client = self.app.test_client

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_index(self):
        response = self.client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_users(self):
        response = self.client().get('api/v1/users')
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('You are viewing registered users',
                      str(response_out['message']))
        self.assertEqual(response.status_code, 200)

    def test_get_dogs(self):
        response = self.client().get('api/v1/dogs')
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('You are viewing registered dogs',
                      str(response_out['message']))
        self.assertEqual(response.status_code, 200)

    def test_add_dogs(self):
        new_dog = {
            "name": "Drogon",
            "breed": "Maltese",
            "age": "8"
        }
        response = self.client().post('api/v1/dogs',
                                      data=json.dumps(new_dog),
                                      content_type='application/json')
        response_out = json.loads(response.data.decode())
        self.assertIn('Added dog successfully',
                      str(response_out['message']))
        self.assertEqual(response.status_code, 201)

    def test_add_user(self):
        new_user = {
            "firstname": "Alex",
            "lastname": "Maximus",
            "city": "Kampala",
            "email": "hey3@world.com"
        }
        response = self.client().post('api/v1/users',
                                      data=json.dumps(new_user),
                                      content_type='application/json')
        response_out = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertIn('Registration successful',
                      str(response_out['message']))


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
