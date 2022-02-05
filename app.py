"""
app.py

メイン
* httpリクエストを受ける
* グローバル変数を持つ
"""


import sqlite3
import flask as f

app = f.Flask(__name__)

@app.route("/")
def app_route():
    return "<h1>This is test</h1>"

if __name__=="__main__":
    app.run(host = "0.0.0.0",port=3000)