# 必要なモジュールをimport
from api import app

# 起動
if __name__ == '__main__': # 直接呼び出し時, グローバル変数__name__には'__main__'が格納される.
    app.run() # 読み込んだapiのappを起動する