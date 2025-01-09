import os
import pickle
import tempfile
import streamlit as st
from streamlit_option_menu import option_menu
import fitz  # PyMuPDF

# Set up the page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="🧑‍⚕️")

# Load pre-trained models (make sure the models are in the 'saved_models' folder)
working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

# Sidebar for disease selection
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Function to extract data from the uploaded PDF
def extract_data_from_pdf(pdf_file):
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(pdf_file.read())
        tmp_file_path = tmp_file.name

    # Open the saved PDF file using PyMuPDF
    doc = fitz.open(tmp_file_path)
    text = ""
    for page in doc:
        text += page.get_text()

    # Extract basic patient details using keywords and fixed structure
    name = "Not found"
    gender = "Not found"
    age = "Not found"
    glucose = "Not found"
    hemoglobin = "Not found"
    cholesterol = "Not found"

    if "Name" in text:
        name = text.split("Name")[1].split(":")[-1].split("\n")[0].strip()
    if "Gender" in text:
        gender = text.split("Gender")[1].split(":")[-1].split("\n")[0].strip()
    if "Age" in text:
        age = text.split("Age")[1].split(":")[-1].split("\n")[0].strip()
    if "GLUCOSE, RANDOM" in text:
        glucose = text.split("GLUCOSE, RANDOM")[1].split()[0].strip()
    if "Hemoglobin" in text:
        hemoglobin = text.split("Hemoglobin")[1].split()[0].strip()
    if "Serum Cholestoral" in text:
        cholesterol = text.split("Serum Cholestoral")[1].split()[0].strip()

    return {
        "Name": name,
        "Gender": gender,
        "Age": age,
        "Glucose": glucose,
        "Hemoglobin": hemoglobin,
        "Cholesterol": cholesterol
    }

# Display Patient Summary Box
def display_patient_summary(patient_data):
    st.subheader("Patient Information")
    st.write(f"**Name:** {patient_data.get('Name', 'N/A')}  ")
    st.write(f"**Gender:** {patient_data.get('Gender', 'N/A')}  ")
    st.write(f"**Age:** {patient_data.get('Age', 'N/A')}  ")

# UI for disease prediction
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    # Upload PDF file
    uploaded_file = st.file_uploader("Upload Patient Report (PDF)", type=["pdf"])

    patient_data = {}
    if uploaded_file:
        patient_data = extract_data_from_pdf(uploaded_file)
        display_patient_summary(patient_data)

    # Fill the form with extracted data or leave blank if not found
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', value="")
    with col2:
        Glucose = st.text_input('Glucose Level', value=patient_data.get('Glucose', ''))
    with col3:
        BloodPressure = st.text_input('Blood Pressure value', value="")

    with col1:
        SkinThickness = st.text_input('Skin Thickness value', value="")
    with col2:
        Insulin = st.text_input('Insulin Level', value="")
    with col3:
        BMI = st.text_input('BMI value', value="")

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', value="")
    with col2:
        Age = st.text_input('Age of the Person', value=patient_data.get('Age', ''))

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [
            Pregnancies if Pregnancies else 0,
            Glucose if Glucose else 0,
            BloodPressure if BloodPressure else 0,
            SkinThickness if SkinThickness else 0,
            Insulin if Insulin else 0,
            BMI if BMI else 0,
            DiabetesPedigreeFunction if DiabetesPedigreeFunction else 0,
            Age if Age else 0
        ]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic.'
        else:
            diab_diagnosis = 'The person is not diabetic.'

    st.success(diab_diagnosis)

if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    # Upload PDF file
    uploaded_file = st.file_uploader("Upload Patient Report (PDF)", type=["pdf"])

    patient_data = {}
    if uploaded_file:
        patient_data = extract_data_from_pdf(uploaded_file)
        display_patient_summary(patient_data)

    # Fill the form with extracted data or leave blank if not found
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.text_input('Age', value=patient_data.get('Age', ''))
    with col2:
        Gender = st.text_input('Gender', value=patient_data.get('Gender', ''))
    with col3:
        Cholesterol = st.text_input('Cholesterol Level', value=patient_data.get('Cholesterol', ''))

    with col1:
        RestingBP = st.text_input('Resting Blood Pressure', value="")
    with col2:
        MaxHR = st.text_input('Maximum Heart Rate Achieved', value="")
    with col3:
        ExerciseInducedAngina = st.text_input('Exercise Induced Angina', value="")

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [
            Age if Age else 0,
            Gender if Gender else 0,
            Cholesterol if Cholesterol else 0,
            RestingBP if RestingBP else 0,
            MaxHR if MaxHR else 0,
            ExerciseInducedAngina if ExerciseInducedAngina else 0
        ]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person has heart disease.'
        else:
            heart_diagnosis = 'The person does not have heart disease.'

    st.success(heart_diagnosis)

if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    # Upload PDF file
    uploaded_file = st.file_uploader("Upload Patient Report (PDF)", type=["pdf"])

    patient_data = {}
    if uploaded_file:
        patient_data = extract_data_from_pdf(uploaded_file)
        display_patient_summary(patient_data)

    # Fill the form with extracted data or leave blank if not found
    col1, col2, col3 = st.columns(3)
    with col1:
        MDVP_Fo = st.text_input('MDVP:Fo(Hz)', value="")
    with col2:
        MDVP_Fhi = st.text_input('MDVP:Fhi(Hz)', value="")
    with col3:
        MDVP_Flo = st.text_input('MDVP:Flo(Hz)', value="")

    with col1:
        MDVP_Jitter = st.text_input('MDVP:Jitter(%)', value="")
    with col2:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer', value="")
    with col3:
        HNR = st.text_input('HNR', value="")

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        user_input = [
            MDVP_Fo if MDVP_Fo else 0,
            MDVP_Fhi if MDVP_Fhi else 0,
            MDVP_Flo if MDVP_Flo else 0,
            MDVP_Jitter if MDVP_Jitter else 0,
            MDVP_Shimmer if MDVP_Shimmer else 0,
            HNR if HNR else 0
        ]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease."
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease."

    st.success(parkinsons_diagnosis)
