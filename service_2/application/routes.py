from application import app
import random

@app.route('/random_gun',methods=['GET'])
def gun():
    gun_types = ["pistol", "assault Rifle", "knife", "minigun", "rocket laucher", "ray-gun"]
    gun = random.choice(gun_types)
    return gun
