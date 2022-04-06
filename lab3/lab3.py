from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("lab3_index.html")

@app.route("/login")
def login():
    return render_template("lab3_login.html")

@app.route("/profile/<username>")
def profile(username):
    return 'Динамический url вне шаблона: ' + url_for('profile', username=username) + ', ' + 'url вне шаблона: ' + url_for('login')

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Jane Doe'))

if __name__ == "__lab3__":
    app.run()
