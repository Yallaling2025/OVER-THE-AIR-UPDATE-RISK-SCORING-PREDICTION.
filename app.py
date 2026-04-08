from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    features = [
        float(request.form["type"]),
        float(request.form["air_temp"]),
        float(request.form["process_temp"]),
        float(request.form["rpm"]),
        float(request.form["torque"]),
        float(request.form["tool_wear"]),
        float(request.form["twf"]),
        float(request.form["hdf"]),
        float(request.form["pwf"]),
        float(request.form["osf"]),
        float(request.form["rnf"])
    ]

    prediction = model.predict([features])

    if prediction[0] == 1:
        result = "⚠ High Risk of OTA Update Failure"
    else:
        result = "✅ Low Risk of OTA Update"

    return render_template("index.html", prediction_text=result)


if __name__ == "__main__":
    app.run(debug=True)