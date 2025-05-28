from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load your trained model
model = joblib.load('random_forest_model.joblib')

# Define feature names in exact order as used during training
FEATURE_NAMES = ['Gender', 'AGE', 'Urea', 'Cr', 'HbA1c', 'Chol', 'TG', 'HDL', 'LDL', 'VLDL', 'BMI']

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        print(f"Received data: {data}")
        
        # Extract features in exact order with proper feature names
        features = [
            data['Gender'], data['AGE'], data['Urea'], data['Cr'],
            data['HbA1c'], data['Chol'], data['TG'], data['HDL'],
            data['LDL'], data['VLDL'], data['BMI']
        ]
        
        # Create DataFrame with proper feature names (this fixes the warning)
        features_df = pd.DataFrame([features], columns=FEATURE_NAMES)
        print(f"Features DataFrame:\n{features_df}")
        
        # Predict using DataFrame (preserves feature names)
        prediction = model.predict(features_df)[0]
        
        # Get probability if available
        if hasattr(model, 'predict_proba'):
            probabilities = model.predict_proba(features_df)[0]
            if prediction == 1:
                confidence = float(probabilities[1])  # Confidence for positive class
            else:
                confidence = float(probabilities[0])  # Confidence for negative class
        
        
        result = {
            'prediction': int(prediction),
            'confidence': confidence,
            'features_used': FEATURE_NAMES,
            'input_values': features
        }
        
        print(f"Prediction result: {result}")
        return jsonify(result)
        
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        return jsonify({
            'error': str(e),
            'prediction': 0,
            'confidence': 0
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None,
        'feature_names': FEATURE_NAMES
    })

if __name__ == '__main__':
    print("Starting ML Prediction Server...")
    print(f"Feature names: {FEATURE_NAMES}")
    print("Server running on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)