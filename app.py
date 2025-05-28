from flask import Flask, render_template, jsonify, request
import joblib
import pandas as pd
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# Load model
model = joblib.load('random_forest_model.joblib')

# Define feature names in exact order as used during training
FEATURE_NAMES = ['Gender', 'AGE', 'Urea', 'Cr', 'HbA1c', 'Chol', 'TG', 'HDL', 'LDL', 'VLDL', 'BMI']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        # Extract features in order
        features = [
            data['Gender'], data['AGE'], data['Urea'], data['Cr'],
            data['HbA1c'], data['Chol'], data['TG'], data['HDL'],
            data['LDL'], data['VLDL'], data['BMI']
        ]
        
        # Create DataFrame
        features_df = pd.DataFrame([features], columns=FEATURE_NAMES)
        
        # Predict
        prediction = model.predict(features_df)[0]
        
        # Get probability
        confidence = 0.8  # Default confidence
        if hasattr(model, 'predict_proba'):
            probabilities = model.predict_proba(features_df)[0]
            confidence = float(probabilities[1] if prediction == 1 else probabilities[0])
        
        return jsonify({
            'prediction': int(prediction),
            'confidence': confidence,
            'features_used': FEATURE_NAMES,
            'input_values': features
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'prediction': 0,
            'confidence': 0
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
