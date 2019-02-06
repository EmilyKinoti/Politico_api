from flask import make_response, jsonify, request, Blueprint
from app.v1.models.parties import Political_Party, parties

api = Blueprint('parties', 'views',  url_prefix='/api/v1')

@api.route('/parties', methods=["POST"])
def create_party():
    data = request.get_json()
    if len(parties) == 0:
        _id = 1
    else:
        _id = parties[-1]['id'] + 1

    if data['name'] == '' or data['address'] == '' or data['logo'] == '':
         return make_response(jsonify({
        "status":400,
        "error": 'party name or hqadress or logo cannot be empty'
    }), 400)
    else:
        try:
            new_party = {
                "id":_id,
                "name": data['name'],
                "hqAddress": data['address'],
                "logoUrl": data['logo']
            }
            res = Political_Party().save_party(new_party)
        except RuntimeError:
            return make_response(jsonify({
                "status":500,
                "error": 'An error occured while processing your request'
            }), 500)


    return make_response(jsonify({
        "status":201,
        "data": [res]
    }), 201)

@api.route("/parties", methods=['GET'])
def get_all_parties():
    try:
        parties = Political_Party().get_all_parties()
    except RuntimeError:
        return make_response(jsonify({
            "status":500,
            "error": 'An error occured while processing your request'
        }), 500)
    
    return make_response(jsonify({
        "status":200,
        "data": parties
    }), 200)



