from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)


model = joblib.load('best_rf_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@app.route("/predict", methods=["POST"])
def predict():

    data = [
        float(request.form.get("air_temp")),
        float(request.form.get("process_temp")),
        float(request.form.get("rot_speed")),
        float(request.form.get("torque")),
        float(request.form.get("tool_wear")),
        int(request.form.get("twf") == "on"),
        int(request.form.get("hdf") == "on"),
        int(request.form.get("pwf") == "on"),
        int(request.form.get("osf") == "on"),
        int(request.form.get("rnf") == "on"),
        int(request.form.get("type_l") == "on"),
        int(request.form.get("type_m") == "on"),
    ]

    prediction = model.predict([data])[0]
    probabilities = model.predict_proba([data])[0]
    status = "Failure" if prediction == 1 else "Machine is Fine"
    return render_template(
        "index.html",
        prediction=status,
        probabilities=[f"{prob:.2f}" for prob in probabilities]
    )


if __name__ == '__main__':
    app.run(debug=True)
