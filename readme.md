SQLAlchemyのサンプルコード
====

GoogleBooksAPIを使用して本の情報を取得してDBに格納する

# 準備
.env.dev → .env にリネームして適切なDB情報を記述する

# 実行
以下のコードで本の情報を収集し、DBに格納する処理を実行
```
python main/run.py "<検索するキーワード>"
```