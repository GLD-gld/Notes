from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = "Hello World"
    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    # 不加host，则只会监听本地回环网卡
    app.run(host='0.0.0.0')