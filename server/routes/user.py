from crypt import methods

from flask import Blueprint, jsonify, Response

users_blueprint = Blueprint('users',__name__)

@users_blueprint.route('/users',methods={'GET'})
def get_all_users(**kwargs) -> Response:
    return jsonify(
        {'id':1,'name':'qwerty'},{'id':3}
    )


def get_user_by_id(id:int, **kwargs) -> Response:
    return jsonify(
        {
            'user': id,
        })
