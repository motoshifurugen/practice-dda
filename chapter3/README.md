# 【chapter3】 Vueの構造・動き方 ~ Flaskの構造・動き方

## Vueの構造

ファイル構成は以下のようになっており、開発では主にsrcフォルダ配下を使用する。

```
dda-front
├── node_modules
├── public
├── src（ ※ ここを主に使用する）
│   ├── assets
│   │    └── （画像ファイルなど）
│   ├── components
│   │    └── （アプリで使用する部品など）
│   ├── plugins
│   │    └── （追加で導入する拡張機能など）
│   ├── App.vue（各ページのベースとなる部分）
│   └── main.js（土台）
├── .gitignore（管理対象外のファイルを記述）
├── babel.config.js
├── jsconfig.json
├── package.json
├── README.md
├── vue.config.js
└── yarn.lock
```

## Vueの動き方

- ① main.js を呼んでJavaScriptを起動

    ↓
- ② App.vue を呼んでVueを起動

    ↓
- ③ componentたち が描写される

### 例）デフォルト画面

<a href="https://gyazo.com/fd0133cf617ad670b3cbdf61dce9e54a"><img src="https://i.gyazo.com/fd0133cf617ad670b3cbdf61dce9e54a.jpg" alt="Image from Gyazo" width="600"/></a>

※ 実際のコードを見ながら追う

## Flaskの構造

参考：https://swallow-incubate.com/archives/blog/20190819

ファイル構成は以下のようにする。

```
dda-api
├── app.py（起動ファイル）
├── config.py（設定ファイル）
└── api
    ├── __init__.py（土台）
    ├── database.py（DB情報）
    ├── models
    │    └── （モデル群）
    └── controllers
         └── （コントローラー群）
```

- モデルでデータの定義を行う
- コントローラーでメソッドの定義を行う
  - あるURLにアクセスしたら、所定のデータを返すというメソッドを定義することで、APIとなる（具体的には以下のようなJSON形式でデータを渡す）


## Flaskの動き方（API）

- ① app.py を実行してFlaskを起動する

    ↓
- ② URLにアクセスすると、URLごとに定義しておいたメソッドが実行される

    ↓
- ③ メソッドでモデルと操作してデータを返す

例）https://dda/api/getUser/1
```
{
  "user": [
   {
     "id": 1,
     "name": "John"
   }
  ]
}
```

