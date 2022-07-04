from application import app
from flask import Flask, request, render_template, url_for
import requests, json



@app.route('/')
def main():
    gun = requests.get('http://service_2:5000/random_gun').text
    body = requests.get('http://service_3:5000/body_location').text
    damage = requests.post('http://service_4:5000/damage_taken', json= dict (gun=gun, body=body))

    
    return render_template('home.html', gun=gun, body=body, damage=damage.text)