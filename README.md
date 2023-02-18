# API Flaskアプリ開発

## 動作環境

MacBook Air<br>
macOS Monterey(バージョン 12.5)

`$ flask --version`

- Python 3.10.4
- Flask 2.2.2
- Werkzeug 2.2.2

# 【1】flaskAPI作成〜Git管理まで

## 参考記事

[【Python】Flask + MySQL + SQLAlchemyでAPIを開発してみよう](https://swallow-incubate.com/archives/blog/20190819)

http://127.0.0.1:5000/api/users で以下のように表示されたら完了

```
{
  users: [
    {
      id: 1,
      name: "John"
    }
  ]
}
```

## :star: ポイント :star:

### ■ インデント

スペースによるインデントかタブによるインデントかを区別させることが多い.
また, スペースの場合は2つ分か4つ分かでも区別される.

### ■ 構造

```
flask-api
├── app.py
└── api
    ├── __init__.py
    └── views
         └── user.py
```

### ■ デコレータについて

[【Python】”@(アットマーク)”から始まる行はどういう意味？【デコレータ】](https://keymaso.com/programemory/python/decorator/)

### ■ .gitignore

gitで管理しなくていいファイルなどを指定できる.

### ■ リモートにpush

```
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/motoshifurugen/practice-dda.git
git push origin main
```
