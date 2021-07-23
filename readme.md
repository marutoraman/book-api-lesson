SQLAlchemyのサンプルコード
====

GoogleBooksAPIを使用して本の情報を取得してDBに格納する

# 準備
.env.dev → .env にリネームして適切なDBサーバー情報を記述する
DBサーバーにbook-dbという名称でDBを作成する
以下を実行してテーブルを作成
```
python commands/migrate.py
```
# 実行
以下のコードで本の情報を収集し、DBに格納する処理を実行
```
python main/run.py "<検索するキーワード>"
```
