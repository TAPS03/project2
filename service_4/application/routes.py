from application import app
from flask import Flask, request, Response
import pdb

@app.route('/damage_taken', methods=['POST'])
def damage():
    count = 0

    damage_total = request.get_json()
    
    if damage_total['gun'] == 'pistol':
        count += 15
    if damage_total['gun'] == 'assault Rifle':
        count += 40
    if damage_total['gun'] == 'knife':
        count += 5
    if damage_total['gun'] == 'minigun':
        count += 55
    if damage_total['gun'] == 'rocket laucher':
        count += 70
    if damage_total['gun'] == 'ray-gun':
        count += 96

    if damage_total['body'] == 'head':
        count += 60
    if damage_total['body'] == 'chest':
        count += 50
    if damage_total['body'] == 'arm':
        count += 30
    if damage_total['body'] == 'leg':
        count += 30
    if damage_total['body'] == 'shoulder':
        count += 20
    if damage_total['body'] == 'foot':
        count += 10

    return str(count)