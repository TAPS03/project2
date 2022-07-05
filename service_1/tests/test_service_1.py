from flask_testing import TestCase
from application import app
from flask import url_for
from unittest.mock import patch
from application import routes
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app

class TestFront(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as m:
            m.get('http://service_2:5000/random_gun', text='minigun')
            m.get('http://service_3:5000/body_location', text='head')
            m.post('http://service_4:5000/damage_taken', text='115')
            response=self.client.get(url_for('main'))
            self.assert200(response)
            self.assertIn(b'minigun', response.data)
            self.assertIn(b'head', response.data)
            self.assertIn(b'115', response.data)