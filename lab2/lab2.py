from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/hello")
def hello():
    return render_template("lab2_hello.html")

@app.route("/")
def index():
    return render_template("lab2_index.html")

if __name__ == "__lab2__":
    app.run()
