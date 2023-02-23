# 必要なモジュールをimport
from flask import Flask, make_response, jsonify
from .views.user import user_router

# app作成処理
def create_app():

    app = Flask(__name__) # インスタンス作成
    app.register_blueprint(user_router, url_prefix='/api') # Blueprintをappに登録

    return app

# appを作成
app = create_app()