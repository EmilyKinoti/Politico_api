from flask import make_response, jsonify, request, Blueprint
from app.v1.models.office import Political_Office, office

officeB = Blueprint('office', 'views',  url_prefix='/api/v1')

@officeB.route('/offices', methods=["POST"])
def create_office():
    data = request.get_json()
    if len(office) == 0:
        _id = 1
    else:
        _id = office[-1]['id'] + 1

    if data['name'] == '' or data['type'] == '':
         return make_response(jsonify({
        "status":400,
        "error": 'office name or type cannot be empty'
    }), 400)
    else:
        try:
            new_office = {
                "id":_id,
                "type": data['type'],
                "name": data['name'],
            }
            res = Political_Office().save_office(new_office)
        except RuntimeError:
            return make_response(jsonify({
                "status":500,
                "error": 'An error occured while processing your request'
            }), 500)


    return make_response(jsonify({
        "status":201,
        "data": [res]
    }), 201)

