#!/usr/bin/env python
"""Unit test for api module GraphQL queries."""
import requests
import unittest


class TestApi(unittest.TestCase):
    """Class to execute unit tests for api.py."""

    @classmethod
    def setUpClass(self):
        """Set up function called when class is consructed."""
        self.base_url = 'http://127.0.0.1:5000/graphql'
        self.headers = {'content-type': 'application/json'}

    def test_query_people(self):
        # Get batch list
        payload = '{"query": "{people(id:\\"UGVvcGxlOjE=\\"){name}}"}'
        response = requests.post(self.base_url, headers=self.headers, data=payload)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json['data']['people']['name'], 'Luke Skywalker')

    def test_query_people_list(self):
        # Get batch list
        payload = '{"query": "{peopleList{edges{node{id}}}}"}'
        response = requests.post(self.base_url, headers=self.headers, data=payload)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(json['data']['peopleList']['edges']), 0)

    def test_query_planet(self):
        # Get batch list
        payload = '{"query": "{planet(id:\\"UGxhbmV0OjE=\\"){name}}"}'
        response = requests.post(self.base_url, headers=self.headers, data=payload)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json['data']['planet']['name'], 'Tatooine')

    def test_query_planet_list(self):
        # Get batch list
        payload = '{"query": "{planetList{edges{node{id}}}}"}'
        response = requests.post(self.base_url, headers=self.headers, data=payload)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(json['data']['planetList']['edges']), 0)

    def test_create_person(self):
        # Get batch list
        payload = '{"query": "mutation{createPerson(input:{name:\\"Alexis ROLLAND\\"}){person{name}}}"}'
        response = requests.post(self.base_url, headers=self.headers, data=payload)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json['data']['createPerson']['person']['name'], 'Alexis ROLLAND')

    def test_update_person(self):
        # Get batch list
        payload = '{"query": "mutation{updatePerson(input:{id:\\"UGVvcGxlOjI=\\",height:\\"170\\"}){person{height}}}"}'
        response = requests.post(self.base_url, headers=self.headers, data=payload)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json['data']['updatePerson']['person']['height'], '170')

    def test_create_planet(self):
        # Get batch list
        payload = '{"query": "mutation{createPlanet(input:{name:\\"Earth\\"}){planet{name}}}"}'
        response = requests.post(self.base_url, headers=self.headers, data=payload)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json['data']['createPlanet']['planet']['name'], 'Earth')

    def test_update_planet(self):
        # Get batch list
        payload = '{"query": "mutation{updatePlanet(input:{id:\\"UGxhbmV0OjE=\\",rotationPeriod:\\"24\\"}){planet{rotationPeriod}}}"}'
        response = requests.post(self.base_url, headers=self.headers, data=payload)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json['data']['updatePlanet']['planet']['rotationPeriod'], '24')

    @classmethod
    def tearDownClass(self):
        """Tear down function called when class is deconstructed."""
        pass


if __name__ == '__main__':
    # Test api endpoints
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApi)
    unittest.TextTestRunner(verbosity=2).run(suite)
