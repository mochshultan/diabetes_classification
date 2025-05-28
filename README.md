# SMOTE-Random Forest Diabetes Prediction Web Application

A web-based application for predicting diabetes risk using a SMOTE-balanced Random Forest model. This application provides an intuitive interface for healthcare professionals to input patient data and receive instant diabetes risk predictions.

## Features

- **Interactive Dashboard**: Clean, modern interface for easy data input
- **Real-time Predictions**: Get instant diabetes risk assessment
- **Model Confidence**: View prediction confidence scores
- **Responsive Design**: Works on both desktop and mobile devices
- **Secure**: All processing happens client-side after model loading

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd smote-rf-diabetes/web_app
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask backend server:
   ```bash
   python backend.py
   ```

2. Open `webapp_noinput.html` in your web browser or use a local web server.

## Usage

1. Enter the patient's information in the input fields:
   - Gender (0 for Female, 1 for Male)
   - Age (years)
   - Urea (mg/dL)
   - Creatinine (mg/dL)
   - HbA1c (%)
   - Cholesterol (mg/dL)
   - Triglycerides (mg/dL)
   - HDL (mg/dL)
   - LDL (mg/dL)
   - VLDL (mg/dL)
   - BMI (kg/m²)

2. Click the "Predict Diabetes Risk" button.
3. View the prediction result and confidence score.

## Model Details

- **Algorithm**: Random Forest Classifier
- **Balancing**: SMOTE (Synthetic Minority Over-sampling Technique)
- **Features Used**: 11 clinical parameters
- **Output**: Binary classification (0: No Diabetes, 1: Diabetes)

## API Endpoints

- `POST /predict`: Accepts patient data and returns prediction
- `GET /health`: Health check endpoint

## Example Request

```json
{
  "Gender": 1,
  "AGE": 45,
  "Urea": 25,
  "Cr": 0.8,
  "HbA1c": 6.2,
  "Chol": 200,
  "TG": 150,
  "HDL": 50,
  "LDL": 120,
  "VLDL": 30,
  "BMI": 27.5
}
```

## Example Response

```json
{
  "prediction": 1,
  "confidence": 0.92,
  "features_used": ["Gender", "AGE", "Urea", "Cr", "HbA1c", "Chol", "TG", "HDL", "LDL", "VLDL", "BMI"],
  "input_values": [1, 45, 25, 0.8, 6.2, 200, 150, 50, 120, 30, 27.5]
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Flask and scikit-learn
- Uses Bootstrap for responsive design
- Model trained using SMOTE for handling class imbalance
