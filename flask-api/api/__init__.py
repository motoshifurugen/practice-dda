# 必要なモジュールをimport
from flask import Flask, make_response, jsonify
from .views.user import user_router

# app作成処理
def create_app():

    app = Flask(__name__)
    app.register_blueprint(user_router, url_prefix='/api')

    return app

app = create_app()