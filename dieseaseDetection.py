import pickle
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

# Page Configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="🧑‍⚕️")

# Load Models
diabetes_model = pickle.load(open('saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('saved_models/parkinsons_model.sav', 'rb'))

# Sidebar Menu
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# CSV Upload Section
st.sidebar.subheader("Upload Patient Data CSV")
uploaded_file = st.sidebar.file_uploader("Upload your CSV file for autofill", type=['csv'])

if uploaded_file:
    patient_data = pd.read_csv(uploaded_file)
    st.sidebar.success("CSV file uploaded successfully!")
else:
    patient_data = pd.DataFrame()  # Empty DataFrame if no file is uploaded

# Autofill Function
def autofill_data(selected_name):
    data_row = patient_data[patient_data['Name'] == selected_name]
    if not data_row.empty:
        return data_row.iloc[0].to_dict()
    return {}

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    if not patient_data.empty:
        st.sidebar.subheader("Autofill Options")
        name_selection = st.sidebar.selectbox("Select Name", patient_data['Name'].unique())
        autofill_values = autofill_data(name_selection)
    else:
        st.warning("No patient data uploaded. Please upload a CSV file.")
        autofill_values = {}

    # Input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', value=autofill_values.get('Pregnancies', ''))
        SkinThickness = st.text_input('Skin Thickness value', value=autofill_values.get('SkinThickness', ''))
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', value=autofill_values.get('DiabetesPedigreeFunction', ''))
    with col2:
        Glucose = st.text_input('Glucose Level', value=autofill_values.get('Glucose', ''))
        Insulin = st.text_input('Insulin Level', value=autofill_values.get('Insulin', ''))
        Age = st.text_input('Age of the Person', value=autofill_values.get('Age', ''))
    with col3:
        BloodPressure = st.text_input('Blood Pressure value', value=autofill_values.get('BloodPressure', ''))
        BMI = st.text_input('BMI value', value=autofill_values.get('BMI', ''))

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        try:
            user_input = [float(x) for x in [Pregnancies, Glucose, BloodPressure, SkinThickness,
                                             Insulin, BMI, DiabetesPedigreeFunction, Age]]
            diab_prediction = diabetes_model.predict([user_input])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic. Suggestion: Stay hydrated, eat vegetables, and consult a doctor.'
            else:
                diab_diagnosis = 'The person is not diabetic.'
        except ValueError:
            diab_diagnosis = "Please enter valid numerical values."
    st.success(diab_diagnosis)

# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    if not patient_data.empty:
        st.sidebar.subheader("Autofill Options")
        name_selection = st.sidebar.selectbox("Select Name", patient_data['Name'].unique())
        autofill_values = autofill_data(name_selection)
    else:
        st.warning("No patient data uploaded. Please upload a CSV file.")
        autofill_values = {}

    # Input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age', value=autofill_values.get('Age', ''))
        trestbps = st.text_input('Resting Blood Pressure', value=autofill_values.get('RestingBloodPressure', ''))
        restecg = st.text_input('Resting Electrocardiographic results', value=autofill_values.get('RestingECG', ''))
        oldpeak = st.text_input('ST depression induced by exercise', value=autofill_values.get('Oldpeak', ''))
        thal = st.text_input('Thal (0=normal; 1=fixed defect; 2=reversible defect)', value=autofill_values.get('Thal', ''))
    with col2:
        sex = st.text_input('Sex', value=autofill_values.get('Sex', ''))
        chol = st.text_input('Serum Cholesterol (mg/dl)', value=autofill_values.get('Cholesterol', ''))
        thalach = st.text_input('Maximum Heart Rate achieved', value=autofill_values.get('Thalach', ''))
        slope = st.text_input('Slope of the peak exercise ST segment', value=autofill_values.get('Slope', ''))
    with col3:
        cp = st.text_input('Chest Pain type', value=autofill_values.get('ChestPain', ''))
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1=True; 0=False)', value=autofill_values.get('FastingBloodSugar', ''))
        exang = st.text_input('Exercise Induced Angina (1=Yes; 0=No)', value=autofill_values.get('ExerciseAngina', ''))
        ca = st.text_input('Number of Major Vessels (0-3) colored by fluoroscopy', value=autofill_values.get('MajorVessels', ''))

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        try:
            user_input = [float(x) for x in [age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                                             exang, oldpeak, slope, ca, thal]]
            heart_prediction = heart_disease_model.predict([user_input])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person has heart disease. Suggestion: Exercise regularly, get enough sleep, and consult a doctor.'
            else:
                heart_diagnosis = 'The person does not have heart disease.'
        except ValueError:
            heart_diagnosis = "Please enter valid numerical values."
    st.success(heart_diagnosis)

# Parkinson's Disease Prediction
if selected == 'Parkinsons Prediction':
    st.title("Parkinson's Disease Prediction using ML")

    if not patient_data.empty:
        st.sidebar.subheader("Autofill Options")
        name_selection = st.sidebar.selectbox("Select Name", patient_data['Name'].unique())
        autofill_values = autofill_data(name_selection)
    else:
        st.warning("No patient data uploaded. Please upload a CSV file.")
        autofill_values = {}

    # Input fields
    col1, col2 = st.columns(2)
    with col1:
        MDVP_Fo = st.text_input('MDVP:Fo (Fundamental Frequency)', value=autofill_values.get('MDVP_Fo', ''))
        MDVP_Fhi = st.text_input('MDVP:Fhi (Maximum Frequency)', value=autofill_values.get('MDVP_Fhi', ''))
        MDVP_Flo = st.text_input('MDVP:Flo (Minimum Frequency)', value=autofill_values.get('MDVP_Flo', ''))
        HNR = st.text_input('HNR (Harmonic-to-Noise Ratio)', value=autofill_values.get('HNR', ''))
    with col2:
        MDVP_Jitter = st.text_input('MDVP:Jitter (%)', value=autofill_values.get('MDVP_Jitter', ''))
        MDVP_Shimmer = st.text_input('MDVP:Shimmer', value=autofill_values.get('MDVP_Shimmer', ''))
        RPDE = st.text_input('RPDE (Recurrence Period Density Entropy)', value=autofill_values.get('RPDE', ''))
        DFA = st.text_input('DFA (Detrended Fluctuation Analysis)', value=autofill_values.get('DFA', ''))

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        try:
            user_input = [float(x) for x in [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Shimmer, HNR, RPDE, DFA]]
            parkinsons_prediction = parkinsons_model.predict([user_input])
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease. Suggestion: Consult a neurologist for further evaluation."
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease."
        except ValueError:
            parkinsons_diagnosis = "Please enter valid numerical values."
    st.success(parkinsons_diagnosis)
