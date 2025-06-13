import streamlit as st
import pandas as pd
import joblib
import numpy as np
import requests
import io
import altair as alt
import matplotlib.pyplot as plt

# =======================
# Warna
dropout_color = '#f781bf'
enrolled_color = '#f768a1'
graduate_color = '#ae017e'
pie_colors = [dropout_color, graduate_color]

# =======================
# Load data dari GitHub
@st.cache_data
def load_data():
    url = 'https://raw.githubusercontent.com/yrraaaaaaa/Proyek-Akhir/main/data/data_bersih.csv'
    df = pd.read_csv(url, sep=';')
    df.columns = df.columns.str.strip().str.lower()

    df['status'] = df['status'].str.strip().str.capitalize()
    df['nationality'] = df['nationality'].str.strip().str.capitalize()
    df['course'] = df['course'].str.strip()
    df['scholarship'] = df['scholarship'].str.strip().str.lower()
    df['marital_status'] = df['marital_status'].str.strip().str.capitalize()

    df = df[df['status'].isin(['Dropout', 'Enrolled', 'Graduate'])]
    df = df[df['nationality'].isin(['Portuguese', 'Brazilian', 'Santomean'])]
    return df

# =======================
# Load model dan scaler dari GitHub
model_url = "https://raw.githubusercontent.com/yrraaaaaaa/Proyek-Akhir/main/model/rf_model.joblib"
scaler_url = "https://raw.githubusercontent.com/yrraaaaaaa/Proyek-Akhir/main/model/scaler.pkl"

@st.cache_resource
def load_model_and_scaler():
    model_response = requests.get(model_url)
    model_bytes = io.BytesIO(model_response.content)
    model = joblib.load(model_bytes)

    scaler_response = requests.get(scaler_url)
    scaler_bytes = io.BytesIO(scaler_response.content)
    scaler = joblib.load(scaler_bytes)

    return model, scaler

model, scaler = load_model_and_scaler()

def predict_status(inputs):
    input_array = np.array(inputs).reshape(1, -1)
    input_array = scaler.transform(input_array)
    prediction = model.predict(input_array)
    return prediction

# =======================
# Sidebar Navigation
st.sidebar.title("Dashboard Navigation")
page = st.sidebar.radio("Pilih Halaman", ["📊 Visualisasi Data", "🔮 Prediksi Status Mahasiswa"])

# =======================
# 📊 Visualisasi Data
if page == "📊 Visualisasi Data":
    st.title("Institute Student Performance Dashboard")

    try:
        df = load_data()

        col1, col2, col3 = st.columns(3)
        col1.metric("Enrolled", df[df['status'] == 'Enrolled'].shape[0])
        col2.metric("Graduate", df[df['status'] == 'Graduate'].shape[0])
        col3.metric("Dropout", df[df['status'] == 'Dropout'].shape[0])

        st.subheader("Country of Student Status")
        country_status = df.groupby(['nationality', 'status']).size().reset_index(name='count')
        chart_country = alt.Chart(country_status).mark_bar().encode(
            x='nationality:N',
            y='count:Q',
            color=alt.Color('status:N', scale=alt.Scale(domain=['Dropout', 'Enrolled', 'Graduate'],
                                                        range=[dropout_color, enrolled_color, graduate_color]))
        ).properties(height=300)
        st.altair_chart(chart_country, use_container_width=True)

        st.subheader("Most Student Courses (Dropout Only)")
        dropout_courses = df[df['status'] == 'Dropout']['course'].value_counts().head(5).reset_index()
        dropout_courses.columns = ['course', 'count']
        course_chart = alt.Chart(dropout_courses).mark_bar(color=graduate_color).encode(
            x=alt.X('count:Q', title='Dropout Count'),
            y=alt.Y('course:N', sort='-x')
        ).properties(height=250)
        st.altair_chart(course_chart, use_container_width=True)

        st.subheader("Scholarship Dropout")
        sch_drop = df[df['status'] == 'Dropout']['scholarship'].value_counts()
        fig1, ax1 = plt.subplots()
        ax1.pie(sch_drop, labels=sch_drop.index, autopct='%1.1f%%', startangle=90, colors=pie_colors)
        ax1.axis('equal')
        st.pyplot(fig1)

        st.subheader("Graduation vs Dropout")
        grad_vs_drop = df[df['status'].isin(['Graduate', 'Dropout'])]['status'].value_counts()
        fig2, ax2 = plt.subplots()
        ax2.pie(grad_vs_drop, labels=grad_vs_drop.index, autopct='%1.1f%%', startangle=90, colors=pie_colors)
        ax2.axis('equal')
        st.pyplot(fig2)

        st.subheader("Scholarship Graduate")
        sch_grad = df[df['status'] == 'Graduate']['scholarship'].value_counts()
        fig3, ax3 = plt.subplots()
        ax3.pie(sch_grad, labels=sch_grad.index, autopct='%1.1f%%', startangle=90, colors=pie_colors)
        ax3.axis('equal')
        st.pyplot(fig3)

        st.subheader("Marital Status")
        marital_status = df.groupby(['marital_status', 'status']).size().reset_index(name='count')
        marital_chart = alt.Chart(marital_status).mark_bar().encode(
            x='marital_status:N',
            y='count:Q',
            color=alt.Color('status:N', scale=alt.Scale(domain=['Dropout', 'Enrolled', 'Graduate'],
                                                        range=[dropout_color, enrolled_color, graduate_color]))
        ).properties(height=300)
        st.altair_chart(marital_chart, use_container_width=True)

    except Exception as e:
        st.error(f"Gagal memuat data dari GitHub: {e}")

# =======================
# 🔮 Halaman Prediksi
elif page == "🔮 Prediksi Status Mahasiswa":
    st.title('Student Dropout Prediction')

    # Input fields
    curricular_units_2nd_sem_approved = st.number_input('Curricular Units 2nd Semester Approved', min_value=0, max_value=30, value=15)
    curricular_units_2nd_sem_grade = st.number_input('Curricular Units 2nd Semester Grade', min_value=0, max_value=20, value=15)
    curricular_units_1st_sem_approved = st.number_input('Curricular Units 1st Semester Approved', min_value=0, max_value=30, value=15)
    curricular_units_1st_sem_grade = st.number_input('Curricular Units 1st Semester Grade', min_value=0, max_value=20, value=15)
    tuition_fees_up_to_date = st.selectbox('Tuition Fees Up to Date', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    scholarship_holder = st.selectbox('Scholarship Holder', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    curricular_units_2nd_sem_enrolled = st.number_input('Curricular Units 2nd Semester Enrolled', min_value=0, max_value=30, value=20)
    curricular_units_1st_sem_enrolled = st.number_input('Curricular Units 1st Semester Enrolled', min_value=0, max_value=30, value=20)
    admission_grade = st.slider('Admission Grade', min_value=0.0, max_value=200.0, value=5.0, step=0.1)
    displaced = st.selectbox('Displaced', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')

    input_data = [
        curricular_units_2nd_sem_approved,
        curricular_units_2nd_sem_grade,
        curricular_units_1st_sem_approved,
        curricular_units_1st_sem_grade,
        tuition_fees_up_to_date,
        scholarship_holder,
        curricular_units_2nd_sem_enrolled,
        curricular_units_1st_sem_enrolled,
        admission_grade,
        displaced
    ]

    if st.button('Predict'):
        prediction = predict_status(input_data)

        status_dict = {
            0: 'Dropout',
            1: 'Enrolled',
            2: 'Graduate'
        }

        predicted_status_index = int(np.ravel(prediction)[0])
        predicted_status = status_dict[predicted_status_index]

        st.success(f"The model predicts that the student is likely to be: **{predicted_status}**")
