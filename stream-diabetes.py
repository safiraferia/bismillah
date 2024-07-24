import pickle
import streamlit as st

# Membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Judul web
st.title('Data Mining Prediksi Diabetes')
st.write('Aplikasi ini membantu dalam memprediksi kemungkinan diabetes berdasarkan parameter medis yang Anda masukkan.')

# Membagi kolom
col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input('Input nilai Pregnancies')

with col2:
    Glucose = st.text_input('Input nilai Glucose')

with col1:
    BloodPressure = st.text_input('Input nilai Blood Pressure')

with col2:
    SkinThickness = st.text_input('Input nilai Skin Thickness')

with col1:
    Insulin = st.text_input('Input nilai Insulin')

with col2:
    BMI = st.text_input('Input nilai BMI')

with col1:
    DiabetesPedigreeFunction = st.text_input('Input nilai Diabetes Pedigree Function')

with col2:
    Age = st.text_input('Input nilai Age')

# Kode untuk prediksi
diab_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_prediction[0] == 1):
        diab_diagnosis = 'Pasien terkena Diabetes'
    else:
        diab_diagnosis = 'Pasien tidak terkena Diabetes'

# Menampilkan hasil di tengah
st.markdown(f"<div style='text-align: center;'>{diab_diagnosis}</div>", unsafe_allow_html=True)
