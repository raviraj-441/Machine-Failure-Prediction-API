# Machine Failure Prediction API

## **Overview**
The **Machine Failure Prediction API** is designed to predict the likelihood of machine failure based on various sensor readings and operational data. The API leverages a trained machine learning model to provide predictions and probabilities of failure, assisting in proactive maintenance and decision-making.

---

## **Features**
- Accepts JSON input for real-time predictions.
- Provides probabilities and predictions for machine failures.
- User-friendly RESTful API endpoint.

---

## **Setup Instructions**

### **Prerequisites**
- Python 3.8 or higher
- Installed libraries:
  - Flask
  - pandas
  - scikit-learn
  - joblib

### **Installation**
1. Clone this repository:
   ```bash
   git clone https://github.com/raviraj-441/Machine-Failure-Prediction-API.git
   cd Machine-Failure-Prediction-API
   ```
2. Install the required dependencies
   
4. Ensure the trained model file (`best_rf_model.pkl`) is in the project directory.

### **Running the API**
Start the Flask server:
```bash
python app.py
```
The server will run locally at:
```
http://127.0.0.1:5000
```

---

## **Usage**
### **Endpoint**: `/predict`
#### **Method**: POST

### **Input Format**
Send a JSON payload in the following format:
```json
[
  {
    "Air temperature [K]": 298.2,
    "Process temperature [K]": 308.7,
    "Rotational speed [rpm]": 1408,
    "Torque [Nm]": 46.3,
    "Tool wear [min]": 3,
    "TWF": 0,
    "HDF": 0,
    "PWF": 0,
    "OSF": 0,
    "RNF": 0,
    "Type_L": 1,
    "Type_M": 0
  }
]
```

### **Response Format**
The API returns predictions and probabilities in JSON format:
```json
{
  "predictions": [
    0
  ],
  "probabilities": [
    [
      0.95,
      0.05
    ]
  ]
}
```
- `predictions`: The predicted class (0 = No failure, 1 = Failure).
- `probabilities`: Probability of each class.

### **Example**
#### **Input**:
```json
[
  {
    "Air temperature [K]": 298.2,
    "Process temperature [K]": 308.7,
    "Rotational speed [rpm]": 1408,
    "Torque [Nm]": 46.3,
    "Tool wear [min]": 3,
    "TWF": 0,
    "HDF": 0,
    "PWF": 0,
    "OSF": 0,
    "RNF": 0,
    "Type_L": 1,
    "Type_M": 0
  }
]
```

#### **Response**:
```json
{
  "predictions": [
    0
  ],
  "probabilities": [
    [
      0.95,
      0.05
    ]
  ]
}
```

---

## **Sample Data**
Use the following data for testing:
| Air temperature [K] | Process temperature [K] | Rotational speed [rpm] | Torque [Nm] | Tool wear [min] | TWF | HDF | PWF | OSF | RNF | Type_L | Type_M |
|----------------------|--------------------------|-------------------------|-------------|----------------|-----|-----|-----|-----|-----|--------|--------|
| 298.2               | 308.7                   | 1408                    | 46.3        | 3              | 0   | 0   | 0   | 0   | 0   | 1      | 0      |

---

## **Acknowledgments**
- Dataset: [AI4I 2020 dataset](https://archive.ics.uci.edu/ml/datasets/AI4I+2020+Predictive+Maintenance+Dataset)
- Libraries: Flask, scikit-learn, pandas

---

## **License**
This project is licensed under the MIT License.

