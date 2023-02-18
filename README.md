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

## 【課題】README.md編集

### ① イシュー作成（Github）

<a href="https://gyazo.com/ce3c486738dd1d7f1a15d6a80df4dee1"><img src="https://i.gyazo.com/ce3c486738dd1d7f1a15d6a80df4dee1.png" alt="Image from Gyazo" width="700"/></a><br>

<a href="https://gyazo.com/680457c07f4498ce5d6a22ec84354146"><img src="https://i.gyazo.com/680457c07f4498ce5d6a22ec84354146.png" alt="Image from Gyazo" width="700"/></a><br>

タイトルと説明を記入後, submitボタン押下<br>

<a href="https://gyazo.com/4c308a39b5c10f821ece740a3fb2bad3"><img src="https://i.gyazo.com/4c308a39b5c10f821ece740a3fb2bad3.png" alt="Image from Gyazo" width="700"/></a>

イシュー番号を確認（ブランチを切る際に使用する）<br>

<a href="https://gyazo.com/68a6ffbc745375586c78dc15948af77e"><img src="https://i.gyazo.com/68a6ffbc745375586c78dc15948af77e.png" alt="Image from Gyazo" width="700"/></a>

### ② ブランチを切る（VSCode）

- 今のブランチを確認する<br>
※ git管理しているフォルダにいることを事前に確認する

```
$ git status
```

例えば, mainブランチにいる場合は以下のように表示される.

```
On branch main
```

- リモートのmainを取り込む（同期させるため）

```
$ git pull origin main
```

- ブランチを切る<br>
命名規則はいろいろ考えられるが, イシュー番号を付けると分かりやすい.

```
$ git checkout -b 1-editReadme
```

### ③ コード修正（VSCode）

- VSCodeでREADME.mdを開く

```
$ ls
README.md
$ code .
```
- 適当にREADME.mdを修正