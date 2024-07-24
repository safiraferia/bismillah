import pickle
import streamlit as st

# Membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Judul web
st.title('Prediksi Diabetes Sekarang, Yuk!')
# Gaya CSS untuk elemen dengan garis tepi oval
st.markdown("""
    <style>
        .input-container, .output-container {
            border-radius: 25px;
            border: 2px solid #888;
            padding: 10px;
            background-color: #f9f9f9;
            margin-bottom: 15px;
        }
        .output-container {
            text-align: center;
            background-color: #f0f0f5;
        }
    </style>
""", unsafe_allow_html=True)
# Membagi kolom
col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input('Input Angka Kehamilan')

with col2:
    Glucose = st.text_input('Input Nilai Glukosa')

with col1:
    BloodPressure = st.text_input('Input Angka Tekanan Darah')

with col2:
    SkinThickness = st.text_input('Input Angka Ketebalan Lipatan Kulit')

with col1:
    Insulin = st.text_input('Input Angka Insulin')

with col2:
    BMI = st.text_input('Input Angka BMI')

with col1:
    DiabetesPedigreeFunction = st.text_input('Input Indikator Riwayat Diabetes')

with col2:
    Age = st.text_input('Input Umur')

# Kode untuk prediksi
diab_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_prediction[0] == 1):
        diab_diagnosis = 'Pasien terkena Diabetes'
    else:
        diab_diagnosis = 'Pasien tidak terkena Diabetes'

# Menampilkan hasil dengan garis tepi oval
st.markdown(f"""
    <div style='text-align: center; background-color: #f0f0f5; padding: 10px; border-radius: 25px; border: 2px solid #888;'>
        {diab_diagnosis}
    </div>
    """, unsafe_allow_html=True)
