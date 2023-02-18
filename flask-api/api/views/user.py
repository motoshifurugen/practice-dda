# 必要なモジュールをimport
from flask import Blueprint, request, make_response, jsonify

# user_routerなるものを定義（Blueprintを使用）
user_router = Blueprint('user_router', __name__)

# user_routerにルーティングと処理を設定
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