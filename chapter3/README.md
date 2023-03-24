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

- ① main.js

    ↓
- ② App.vue

    ↓
- ③ componentたち

### 例）デフォルト画面

<a href="https://gyazo.com/fd0133cf617ad670b3cbdf61dce9e54a"><img src="https://i.gyazo.com/fd0133cf617ad670b3cbdf61dce9e54a.jpg" alt="Image from Gyazo" width="600"/></a>

※ 実際のコードを見ながら追う

## Flaskの構造


