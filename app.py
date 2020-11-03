from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "STRING CHECK API"

app.run("lan", 8080)
