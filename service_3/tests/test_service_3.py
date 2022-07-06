from flask_testing import TestCase
from application import app
from flask import url_for
from unittest.mock import patch
from application import routes

class TestBase(TestCase):
    def create_app(self):
        return app


class Test_service_2(TestBase):
    def test_body(self):
        with patch('random.choice') as x:
            x.return_value = "head"
            response = self.client.get(url_for('body'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'head', response.data)