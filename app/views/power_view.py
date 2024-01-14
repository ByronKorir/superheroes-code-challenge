from models import db, HeroPower,Hero,Power
from flask import jsonify, request,Blueprint

power_bp = Blueprint('power_bp', __name__)




# get all powers  
@power_bp.route('/powers')
def powers():
    powers =  [
        {
            "id":power.id,
            "name":power.name,
            "description":power.description
        }
        for power in Power.query.all()

    ]

    response = jsonify({"powers":powers}),200
    return response
    


# get single power  
@power_bp.route('/powers/<int:id>')
def powers_by_id(id):
    power = Power.query.get(id)
    if not power:
        response = jsonify({"error": "power not found"}),404
    else:
        # response = jsonify(power.to_dict()),200
        response_body = {
            "id": power.id,
            "name": power.name,
            "description": power.description
        }
        response = jsonify({"power":response_body}), 200

        
    return response

# patching power  
@power_bp.route('/powers/<int:id>', methods = ['PATCH'])
def update_powers_by_id(id):
    data = request.form
    power = Power.query.get(id)
    if power:
        description = data.get('description')
        if description is not None:
            power.description = description
            db.session.commit()

            response_body = {
                "id": power.id,
                "name": power.name,
                "description": power.description
            }
            response = jsonify({"power":response_body}), 200
        else:
            response = jsonify({"errors": ["validation errors"]}),400
    
    elif not power:
        response = jsonify({"error": "Power not found"}),404

    return response
