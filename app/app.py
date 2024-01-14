#!/usr/bin/env python3

from flask import Flask, jsonify, request
from flask_migrate import Migrate

from models import db, Hero, Power, HeroPower

from views import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Heroes/powers/hero_powers</h1>'

#hero crud
app.register_blueprint(hero_bp)

app.register_blueprint(hero_power_bp)

app.register_blueprint(power_bp)




if __name__ == '__main__':
    app.run(port=5555, debug =True)
