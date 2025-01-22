from flask import Flask, request, jsonify
import pandas as pd
import joblib


app = Flask(__name__)


model = joblib.load('best_rf_model.pkl')


@app.route('/')
def home():
    return "Welcome to the Machine Failure Prediction API!"


@app.route('/predict', methods=['POST'])
def predict():
    try:
        
        data = request.json
        df = pd.DataFrame(data)

        
        print("Expected features by the model:", model.feature_names_in_)

        
        required_columns = model.feature_names_in_.tolist()  

        
        for col in required_columns:
            if col not in df.columns:
                df[col] = 0  
        df = df[required_columns]  

        
        predictions = model.predict(df)
        probabilities = model.predict_proba(df)  

        return jsonify({
            "predictions": predictions.tolist(),
            "probabilities": probabilities.tolist()
        })
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
