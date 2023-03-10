# 【chapter1】 FlaskAPI作成 〜 Git管理

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
nothing to commit, working tree clean
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

- 今のブランチを確認する<br>

```
$ git status
On branch 1-editReadme
nothing to commit, working tree clean
```

- VSCodeで`README.md`を開く

```
$ ls
README.md
$ code .
```
- 適当に`README.md`を修正

- 今の状況を確認するのにも`status`は使える（こちらが主な使い道）<br>

```
$ git status
On branch 1-editReadme
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

`README.md`が編集されたことが示されている.

- addして変更を保存

```
$ git add README.md
```

上記ではファイルを指定してaddしているが, 全ての変更を保存するワイルドカードも以下のように使用できる.

```
$ git add .
```

- 今の状況を確認する

```
$ git status
On branch 1-editReadme
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md
```

`Changes to be committed`はcommitできるよって意味？（笑）

- commitする<br>commitには` -m`でメッセージがつけれる. イシュー番号をつけておくと後からどのイシューでの変更なのかが分かりやすい.

```
$ git commit -m "#1 edit raadme"
```

- 今の状況を確認する

```
$ git status
On branch 1-editReadme
nothing to commit, working tree clean
```

commitしてローカルリポジトリに保存済みのため, 変更なしと表示される.（リモートにpushする準備ができた）

- pushする

```
$ git push origin HEAD
```

HEADは最新にcommitしたブランチを指す（今回の例だと`1-editReadme`のこと）

### ④ pull Requestを作成（Github）

<a href="https://gyazo.com/065228bb341b41d766e2396177106c84"><img src="https://i.gyazo.com/065228bb341b41d766e2396177106c84.png" alt="Image from Gyazo" width="700"/></a><br>

<a href="https://gyazo.com/a9eacd38603de0ad4929d33f944c33c5"><img src="https://i.gyazo.com/a9eacd38603de0ad4929d33f944c33c5.png" alt="Image from Gyazo" width="700"/></a><br>

タイトルと説明を記入してCreateボタンを押下

<a href="https://gyazo.com/cfd92e717693597ba0846d17b521d160"><img src="https://i.gyazo.com/cfd92e717693597ba0846d17b521d160.png" alt="Image from Gyazo" width="700"/></a><br>

- 以下のような状態になったら完了！！おつかれさま :sparkles:<br>
Mergeボタンを押してmergeしたら, リモートに変更が反映される（業務ではコードを管理している人が確認して問題ないと判断されればmergeされるため, この項目はmerge Requestとも呼ばれる）.

<a href="https://gyazo.com/e71568b8272e1e8ffe5c03fb746e4021"><img src="https://i.gyazo.com/e71568b8272e1e8ffe5c03fb746e4021.png" alt="Image from Gyazo" width="700"/></a>