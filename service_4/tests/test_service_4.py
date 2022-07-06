from flask_testing import TestCase
from application import app
from flask import url_for
from unittest.mock import patch
from application import routes

class TestBase(TestCase):
    def create_app(self):
        return app


class Test_service_4(TestBase):
    def test_count(self):
        response = self.client.post(url_for('damage'), json={"gun": "minigun", "body": "head"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'115', response.data)

    def test_count1(self):
        response = self.client.post(url_for('damage'), json={"gun": "pistol", "body": "arm"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'45', response.data)

    def test_count2(self):
        response = self.client.post(url_for('damage'), json={"gun": "rocket laucher", "body": "foot"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'80', response.data)

    def test_count3(self):
        response = self.client.post(url_for('damage'), json={"gun": "assault Rifle", "body": "shoulder"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'60', response.data)

    def test_count4(self):
        response = self.client.post(url_for('damage'), json={"gun": "knife", "body": "leg"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'35', response.data)

    def test_count5(self):
        response = self.client.post(url_for('damage'), json={"gun": "ray-gun", "body": "chest"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'146', response.data)