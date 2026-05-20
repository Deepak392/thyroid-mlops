import streamlit as st
import pandas as pd
import joblib
import time

model=joblib.load("models/model.pkl")

st.set_page_config(
    page_title="Thyroid Recurrence Predictor",
    page_icon="🩺",
    layout="wide"
)

st.markdown("""
<style>

.main{
padding-top:1rem;
}

.stButton>button{
width:100%;
height:3em;
font-size:18px;
border-radius:12px;
}

.prediction-box{
padding:20px;
border-radius:15px;
background-color:#f4f4f4;
}

</style>
""",unsafe_allow_html=True)


st.markdown("""
# 🩺 Thyroid Cancer Recurrence Prediction System

### AI-powered healthcare decision support system using Machine Learning + MLOps

This application predicts recurrence risk based on patient history and diagnostic indicators.
""")

col1,col2,col3=st.columns(3)

col1.metric(
label="Model",
value="Logistic Regression"
)

col2.metric(
label="ML Pipeline",
value="MLOps Enabled"
)

col3.metric(
label="Tracking",
value="MLflow"
)


with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2966/2966488.png",
        width=100
    )

    st.header("About")

    st.info("""
Built using:

✔ Streamlit  
✔ MLflow  
✔ Docker  
✔ Kubernetes  
✔ AWS S3  
✔ GitHub Actions
""")

    with st.expander("📘 Label Guide"):

        st.markdown("""

### Gender
F → Female  
M → Male  

### Smoking
No → No history  
Yes → History exists  

### Risk

Low → Low severity  
Intermediate → Medium  
High → High severity  

### Response

Excellent  
Indeterminate  
Structural Incomplete  
Biochemical Incomplete

""")


gender_map={"F":0,"M":1}

yes_no={"No":0,"Yes":1}

thyroid_map={
"Clinical Hyperthyroidism":0,
"Clinical Hypothyroidism":1,
"Euthyroid":2,
"Subclinical Hyperthyroidism":3,
"Subclinical Hypothyroidism":4
}

physical_map={
"Diffuse goiter":0,
"Multinodular goiter":1,
"Normal":2,
"Single nodular goiter-left":3,
"Single nodular goiter-right":4
}

adenopathy_map={
"Bilateral":0,
"Extensive":1,
"Left":2,
"No":3,
"Posterior":4,
"Right":5
}

pathology_map={
"Follicular":0,
"Hurthel cell":1,
"Micropapillary":2,
"Papillary":3
}

focality_map={
"Multi-Focal":0,
"Uni-Focal":1
}

risk_map={
"High":0,
"Intermediate":1,
"Low":2
}

t_map={
"T1a":0,
"T1b":1,
"T2":2,
"T3a":3,
"T3b":4,
"T4a":5,
"T4b":6
}

n_map={
"N0":0,
"N1a":1,
"N1b":2
}

m_map={
"M0":0,
"M1":1
}

stage_map={
"I":0,
"II":1,
"III":2,
"IVA":3,
"IVB":4
}

response_map={
"Biochemical Incomplete":0,
"Excellent":1,
"Indeterminate":2,
"Structural Incomplete":3
}


st.divider()

st.subheader("Patient Information")

c1,c2,c3=st.columns(3)

with c1:

    Age=st.slider(
        "Age",
        18,
        100,
        30
    )

    Gender=gender_map[
        st.selectbox(
            "Gender",
            gender_map.keys()
        )
    ]

    Smoking=yes_no[
        st.selectbox(
            "Smoking",
            yes_no.keys()
        )
    ]


with c2:

    Hx_Smoking=yes_no[
        st.selectbox(
            "Hx Smoking",
            yes_no.keys()
        )
    ]

    Hx_Radiothreapy=yes_no[
        st.selectbox(
            "Hx Radiotherapy",
            yes_no.keys()
        )
    ]

    Thyroid_Function=thyroid_map[
        st.selectbox(
            "Thyroid Function",
            thyroid_map.keys()
        )
    ]


with c3:

    Physical_Examination=physical_map[
        st.selectbox(
            "Physical Examination",
            physical_map.keys()
        )
    ]

    Adenopathy=adenopathy_map[
        st.selectbox(
            "Adenopathy",
            adenopathy_map.keys()
        )
    ]

    Pathology=pathology_map[
        st.selectbox(
            "Pathology",
            pathology_map.keys()
        )
    ]


st.subheader("Clinical Indicators")

x1,x2,x3=st.columns(3)

with x1:

    Focality=focality_map[
        st.selectbox(
            "Focality",
            focality_map.keys()
        )
    ]

    Risk=risk_map[
        st.selectbox(
            "Risk",
            risk_map.keys()
        )
    ]


with x2:

    T=t_map[
        st.selectbox(
            "Tumor Stage",
            t_map.keys()
        )
    ]

    N=n_map[
        st.selectbox(
            "Lymph Nodes",
            n_map.keys()
        )
    ]


with x3:

    M=m_map[
        st.selectbox(
            "Metastasis",
            m_map.keys()
        )
    ]

    Stage=stage_map[
        st.selectbox(
            "Cancer Stage",
            stage_map.keys()
        )
    ]

    Response=response_map[
        st.selectbox(
            "Treatment Response",
            response_map.keys()
        )
    ]


if st.button("🔍 Predict Recurrence Risk"):

    with st.spinner("Analyzing patient data..."):

        time.sleep(2)

        data=pd.DataFrame([{

        "Age":Age,
        "Gender":Gender,
        "Smoking":Smoking,
        "Hx Smoking":Hx_Smoking,
        "Hx Radiothreapy":Hx_Radiothreapy,
        "Thyroid Function":Thyroid_Function,
        "Physical Examination":Physical_Examination,
        "Adenopathy":Adenopathy,
        "Pathology":Pathology,
        "Focality":Focality,
        "Risk":Risk,
        "T":T,
        "N":N,
        "M":M,
        "Stage":Stage,
        "Response":Response

        }])

        pred=model.predict(data)

        st.divider()

        if pred[0]==1:

            st.error("""
🚨 High recurrence risk detected

Immediate medical review recommended.
""")

        else:

            st.success("""
✅ Low recurrence risk

Patient shows lower likelihood of recurrence.
""")