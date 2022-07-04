from application import app
from flask import Flask, request, Response, jsonify
import random

@app.route('/body_location', methods=['GET'])
def body():
    body_location = ["head", "chest", "arm", "leg", "shoulder", "foot"]
    return random.choice(body_location)