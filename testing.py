import requests

url = "http://127.0.0.1:5000/predict"
test_data = [
    {
        "Rotational speed [rpm]": 1400,
        "Torque [Nm]": 50,
        "Tool wear [min]": 200,
        "Air temperature [K]": 300,
        "Process temperature [K]": 310,
        "Type_L": 0,
        "Type_M": 1,
        "TWF": 0,
        "HDF": 0,
        "PWF": 0,
        "OSF": 0,
        "RNF": 0
    },
    {
        "Rotational speed [rpm]": 1300,
        "Torque [Nm]": 70,
        "Tool wear [min]": 300,
        "Air temperature [K]": 320,
        "Process temperature [K]": 330,
        "Type_L": 1,
        "Type_M": 0,
        "TWF": 1,
        "HDF": 1,
        "PWF": 1,
        "OSF": 0,
        "RNF": 0
    }
]

response = requests.post(url, json=test_data)
print("Response:", response.json())
