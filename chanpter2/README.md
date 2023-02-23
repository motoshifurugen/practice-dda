# 【chapter2】 Vueフロント作成 〜 Git管理

## 参考記事

[はじめてのVuetify(ログインページ作成で使い方学ぶ)](https://reffect.co.jp/vue/vuetify-first-time)

http://localhost:8080/ で以下のように表示されたら完了

## アプリ作成準備

### リモートリポジトリ作成（Github）

フロントエンドのソース管理用のリポジトリを新しく作成する.

### Vueアプリを開発するためのフォルダを作成（VScode）

APIのリポジトリで管理しているフォルダの外に作成する

```
$ mkdir dda-front
$ cd dda-front
$ git status
```

### Vueのインストール

色んな方法があるが, 今回はyarnを使ってVueをインストールしていく.<br>
（yarn：JavaScriptのパッケージマネージャー）

まず, Homebrewがあるか確認
```
$ brew --version
Homebrew 3.6.21
```

yarnをインストール（一応あるか確認）
```
$ yarn -v
1.22.19
$ brew install yarn
```

VueCLIをインストール<br>
（VueCLI：コマンドを使用してVueアプリ開発を行うためのツール）
```
$ yarn global add @vue/cli
$ vue -V
@vue/cli 5.0.8
```

vueコマンドが使えなければ以下の記事を参考にパスを通す.<br>
https://webrandum.net/zsh-command-not-found-vue/

## アプリ作成

Vueアプリを作成<br>
（dda-frontの部分は任意）

```
$ vue create dda-front
```

配下にアプリの型が作成される.

起動して確認
```
$ ls
$ cd dda-front
$ yarn serve
```

<a href="https://gyazo.com/d8a4dbc98a84198c251145c41a78cce1"><img src="https://i.gyazo.com/d8a4dbc98a84198c251145c41a78cce1.png" alt="Image from Gyazo" width="500"/></a>

Vuetifyを導入
```
$ vue add vuetify
$ yarn serve
```

<a href="https://gyazo.com/764bade13ba9b9c60cc8bbdf04c7da96"><img src="https://i.gyazo.com/764bade13ba9b9c60cc8bbdf04c7da96.jpg" alt="Image from Gyazo" width="500"/></a>

## Git管理（VScode）
リモートリポジトリに変更を反映する.