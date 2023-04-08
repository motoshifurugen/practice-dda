# 【chapter4】 DB作成

## MySQLのインストール

```bash
$ mysql --version
```

入ってなかったらインストール
```bash
$ brew install mysql
```

起動
```
$ mysql.server start
```

ログイン
```bash
$ mysql -uroot
```

## FlaskSQLAlchemy

【公式ドキュメント】https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/

Flaskでデータベースを操作できるようにするためのライブラリ

参考記事：https://qiita.com/shirakiya/items/0114d51e9c189658002e


