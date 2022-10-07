from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return 'Index page'
@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"