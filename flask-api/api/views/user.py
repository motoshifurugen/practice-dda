# 必要なモジュールをimport
from flask import Blueprint, request, make_response, jsonify

# ルーティング設定(Blueprint使用)
user_router = Blueprint('user_router', __name__)

# get_user_list関数をくっつけてルーティング
@user_router.route('/users', methods=['GET']) # @はデコレータ
def get_user_list():
    return make_response(jsonify({
        'users': [
            {
                'id': 1,
                'name': 'John'
            }
        ]
    }))