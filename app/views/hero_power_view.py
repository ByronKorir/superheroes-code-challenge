from models import db, HeroPower,Hero
from flask import jsonify, request,Blueprint

hero_power_bp = Blueprint('hero_power_bp', __name__)



### POST /hero_powers
@hero_power_bp.route('/hero_powers', methods = ['POST'])
def post_hero_powers():
    data = request.form
    
    strength = data.get('strength')
    power_id = data.get('power_id')
    hero_id = data.get('hero_id')
    
    # validating hero and power 
    check_hero = Hero.query.get(hero_id)
    check_power = Power.query.get(power_id)
    strengths =["weak","strong","average"]

    if check_power and check_hero and strength.lower() in strengths:
        
        new_data = HeroPower(
            strength=strength.title(),
            power_id=power_id,
            hero_id=hero_id,
            )
        db.session.add(new_data)
        db.session.commit()

        hero = Hero.query.get(hero_id)
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
        response = jsonify({"success":response_body}), 201

    
    else:
        response = jsonify({"errors": ["validation errors"]}),404
    
    return response