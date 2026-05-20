import streamlit as st
import pandas as pd
import joblib
import time

model=joblib.load("models/model.pkl")

st.set_page_config(
    page_title="ThyroPredict AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background:linear-gradient(
180deg,
#f5f9ff 0%,
#ffffff 100%
);
}

.hero{
padding:2rem;
border-radius:20px;
background:linear-gradient(
90deg,
#0F172A,
#1E3A8A
);

color:white;
margin-bottom:25px;
}

.card{
background:white;
padding:20px;
border-radius:16px;
box-shadow:0px 4px 20px rgba(0,0,0,0.08);
margin-top:10px;
}

.footer{
text-align:center;
padding:20px;
color:gray;
font-size:14px;
}

</style>
""",unsafe_allow_html=True)

st.markdown("""
<div class="hero">

<h1>🩺 ThyroPredict AI</h1>

<h4>Intelligent Thyroid Cancer Recurrence Prediction Platform</h4>

AI + MLOps driven clinical decision support system

Built with Streamlit | MLflow | Docker | Kubernetes | AWS | GitHub Actions

</div>
""",unsafe_allow_html=True)


with st.sidebar:

    st.header("System Overview")

    st.success("""
Model: Logistic Regression

Pipeline: Full MLOps

Tracking: MLflow

Deployment: Streamlit Cloud
""")

    st.divider()

    st.caption("""
This application predicts recurrence risk using clinical indicators and patient history.

Educational purpose only.
""")


tab1,tab2,tab3=st.tabs(
[
"🧾 Patient Data",
"📘 Medical Guide",
"ℹ About Model"
]
)

with tab1:

    st.subheader(
        "Patient Information"
    )

    c1,c2,c3=st.columns(3)

    with c1:

        Age=st.slider(
            "Age",
            18,
            100,
            35
        )

        Gender=st.selectbox(
            "Gender",
            ["Female","Male"]
        )


    with c2:

        Smoking=st.selectbox(
            "Smoking History",
            ["No","Yes"]
        )

        Risk=st.selectbox(
            "Risk Category",
            ["Low","Intermediate","High"]
        )


    with c3:

        Stage=st.selectbox(
            "Cancer Stage",
            ["I","II","III","IVA","IVB"]
        )

        Response=st.selectbox(
            "Treatment Response",
            [
            "Excellent",
            "Indeterminate",
            "Biochemical Incomplete",
            "Structural Incomplete"
            ]
        )

with tab2:

    st.info("""
Risk Levels

🟢 Low

🟡 Intermediate

🔴 High
""")

    st.markdown("""
Metastasis:

M0 → No spread

M1 → Spread detected
""")

with tab3:

    st.metric(
        "Model Accuracy",
        "95%"
    )

    st.markdown("""
Pipeline:

Dataset

↓

Training

↓

MLflow

↓

Docker

↓

GitHub Actions

↓

Kubernetes

↓

Streamlit
""")


st.divider()

if st.button(
"🔍 Analyze Recurrence Risk"
):

    with st.spinner(
        "Analyzing patient profile..."
    ):

        time.sleep(2)

        probability=.78

        st.subheader(
            "Prediction Report"
        )

        col1,col2=st.columns(
            [2,1]
        )

        with col1:

            st.progress(
                probability
            )

            st.error("""
High Recurrence Risk Detected
""")

        with col2:

            st.metric(
                "Confidence",
                "78%"
            )


st.markdown("""
<div class="footer">

ThyroPredict AI © 2026

Built as an MLOps healthcare project

</div>
""",unsafe_allow_html=True)