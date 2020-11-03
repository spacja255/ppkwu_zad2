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
        "uppercaseCount":    sum(ch.isupper() for ch in text),
        "lowercaseCount":    sum(ch.islower() for ch in text),
        "digitsCount":       sum(ch.isdigit() for ch in text),
        "specialCount":      sum(not ch.isalnum() for ch in text)
    }
    
    return response

app.run("localhost", 8080)
