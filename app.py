from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Trained model load
model = joblib.load("phishing_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        features = [
            float(request.form["url_length"]),
            float(request.form["valid_url"]),
            float(request.form["at_symbol"]),
            float(request.form["sensitive_word"]),
            float(request.form["path_length"]),
            float(request.form["isHttps"]),
            float(request.form["nb_dots"]),
            float(request.form["nb_hyphen"]),
            float(request.form["nb_and"]),
            float(request.form["nb_or"]),
            float(request.form["nb_www"]),
            float(request.form["nb_com"]),
            float(request.form["nb_unders"])
        ]

        prediction = model.predict([features])

        if prediction[0] == 1:
            result = "Safe URL"
        else:
            result = "Phishing URL"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)