# Disease Prediction System

This repository contains a **Disease Prediction System** built using Streamlit, which predicts the likelihood of three medical conditions:

1. **Diabetes**
2. **Heart Disease**
3. **Parkinson's Disease**

## Features

- **CSV Upload for Autofill**: Users can upload a CSV file containing patient data for automatic population of input fields.
- **User-Friendly Interface**: The app features a sidebar for navigation and clear instructions for input.
- **Interactive Predictions**: Predictions are made instantly using pre-trained machine learning models.

## Technologies Used

- **Streamlit**: For building the web application.
- **Scikit-learn**: For training the machine learning models.
- **Pandas**: For data manipulation.
- **Python**: Core programming language.

## How to Use

1. Clone the repository.
2. Ensure that the `saved_models` directory contains the trained models:
    - `diabetes_model.sav`
    - `heart_disease_model.sav`
    - `parkinsons_model.sav`
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run disease_detection_app.py
   ```
5. Upload a CSV file with patient data to autofill fields or manually enter the data.
6. Select the condition you want to predict from the sidebar menu.

## Models Overview

### 1. Diabetes Model
- **Input Features**:
  - Number of pregnancies
  - Glucose level
  - Blood pressure
  - Skin thickness
  - Insulin level
  - BMI
  - Diabetes pedigree function
  - Age
- **Output**: Binary prediction (Diabetic or Not Diabetic).
- **Model Type**: Logistic Regression or Random Forest (trained on Pima Indian Diabetes Dataset).

### 2. Heart Disease Model
- **Input Features**:
  - Age, Sex, and Chest Pain Type
  - Resting blood pressure and cholesterol levels
  - Resting ECG results
  - Maximum heart rate achieved
  - Exercise-induced angina and other relevant features
- **Output**: Binary prediction (Heart Disease Present or Not).
- **Model Type**: Decision Tree or Random Forest (trained on UCI Heart Disease Dataset).

### 3. Parkinson's Disease Model
- **Input Features**:
  - Various vocal attributes such as MDVP:Fo(Hz), MDVP:RAP, Shimmer, etc.
  - Measures of frequency variation and vocal amplitude.
- **Output**: Binary prediction (Parkinson's Present or Not).
- **Model Type**: Support Vector Machine (trained on UCI Parkinson's Dataset).

## File Structure

```
project/
├── disease_detection_app.py   # Main application script
├── saved_models/              # Directory containing trained models
│   ├── diabetes_model.sav
│   ├── heart_disease_model.sav
│   └── parkinsons_model.sav
├── data/                      # Directory for storing sample CSV files (optional)
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation
```

## Example CSV File Format

For autofill functionality, ensure the uploaded CSV file follows this structure:

| Name   | Gender | Age | Pregnancies | Glucose | BloodPressure | SkinThickness | Insulin | BMI  | DiabetesPedigreeFunction | RestingBP | Cholesterol | MaxHR | ExerciseInducedAngina | MDVP_Fo | MDVP_Fhi | MDVP_Flo | MDVP_Jitter | MDVP_Shimmer | HNR |
|--------|--------|-----|-------------|---------|---------------|---------------|---------|------|--------------------------|-----------|-------------|-------|-----------------------|---------|----------|----------|-------------|--------------|-----|
| Ram    | Male   | 30  | 0           | 85      | 70            | 25            | 0       | 22.5 | 0.1                      | 120       | 180         | 160   | 0                     | 120     | 150      | 100      | 0.005       | 0.01         | 30  |
| Raman  | Male   | 55  | 2           | 200     | 85            | 30            | 130     | 35.0 | 0.8                      | 110       | 150         | 140   | 1                     | 110     | 140      | 90       | 0.015       | 0.04         | 15  |
| Rashid | Male   | 65  | 0           | 95      | 85            | 20            | 0       | 23.0 | 0.2                      | 160       | 240         | 100   | 1                     | 100     | 130      | 80       | 0.010       | 0.03         | 20  |

Include all required columns as expected by the respective prediction model.

## Suggestions
- Ensure the input values are valid and within realistic ranges.
- Consult medical professionals for detailed insights based on predictions.

## License
This project is licensed under the MIT License.

