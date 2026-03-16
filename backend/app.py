from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Get base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load model and scaler from model folder
model = pickle.load(open(os.path.join(BASE_DIR, "model/breast_cancer_model.pkl"), "rb"))
scaler = pickle.load(open(os.path.join(BASE_DIR, "model/scaler.pkl"), "rb"))


@app.route("/")
def home():
    return "Breast Cancer Prediction API Running"


@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.json["features"]

        # Convert to numpy array
        features = np.array(data).reshape(1, -1)

        # Scale data
        features_scaled = scaler.transform(features)

        # Predict
        prediction = model.predict(features_scaled)

        result = int(prediction[0])

        return jsonify({
            "prediction": result
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)