from models import db, Hero
from flask import jsonify, request,Blueprint

hero_bp = Blueprint('hero_bp', __name__)


# get all heroes  
@hero_bp.route('/heroes')
def get_heroes():
    heroes = [
        { "id": hero.id, 
        "name": hero.name, 
        "super_name": hero.super_name
        }
        for hero in Hero.query.all()
    ]
    return (jsonify({"heroes":heroes}),200)


# get single hero  
@hero_bp.route('/heroes/<int:id>')
def heroes_by_id(id):
    hero = Hero.query.get(id)
    if not hero:
        response = jsonify({"error": "Hero not found"}),404
   
    else:
         
        powers_data = [
            {
                "id": hero_power.power.id,
                "name": hero_power.power.name,
                "description": hero_power.power.description
            }
            
            for hero_power in hero.hero_powers   
        ]

        response_body = {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
            "powers": powers_data
        }
        response = jsonify({"single_hero":response_body}), 200

    return response
