from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "STRING CHECK API"

@app.route("/check/<text>")
def rev(text):
    response = {
        "containsUppercase": any(ch.isupper() for ch in text),
        "containsLowercase": any(ch.islower() for ch in text),
        "containsDigits":    any(ch.isdigit() for ch in text),
        "containsSpecial":   any(not ch.isalnum() for ch in text),
        "uppercaseCount":    0,
        "lowercaseCount":    0,
        "digitsCount":       0,
        "specialCount":      0
    }
    
    return response

app.run("lan", 8080)
