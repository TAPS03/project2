from flask_testing import TestCase 
from application import app , routes
from flask import url_for
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self): 
        return app


class Test_service_1(TestBase):
    def test_gun(self):
        with patch('random.choice') as x:
            x.return_value = "minigun"
            response = self.client.get(url_for('gun'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'minigun', response.data)