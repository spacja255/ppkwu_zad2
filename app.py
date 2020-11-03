from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "STRING CHECK API"

@app.route("/check/<text>")
def rev(text):
    response = {
        "containsUppercase": False,
        "containsLowercase": False,
        "containsDigits":    False,
        "containsSpecial":   False,
        "uppercaseCount":    0,
        "lowercaseCount":    0,
        "digitsCount":       0,
        "specialCount":      0
    }
    
    return response

app.run("lan", 8080)
