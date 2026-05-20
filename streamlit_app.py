import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/model.pkl")

st.set_page_config(page_title="Thyroid Recurrence Predictor")

st.title("🩺 Thyroid Recurrence Prediction")
st.write("Enter patient details below.")

with st.expander("📘 Label Guide"):
    st.markdown("""
**Gender**
- F = Female
- M = Male

**Smoking / Hx Smoking / Hx Radiotherapy**
- Yes = Positive
- No = Negative

**Risk**
- Low → Less severe
- Intermediate → Moderate severity
- High → Higher severity

**M**
- M0 → No distant metastasis
- M1 → Distant metastasis exists

**N**
- N0 → No lymph node involvement
- N1a / N1b → Lymph node involvement

**Recurred**
- No → Cancer did not recur
- Yes → Cancer recurred
""")

# Mapping dictionaries

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

Age=st.number_input("Age",18,100,30)

Gender=gender_map[
st.selectbox("Gender",gender_map.keys())
]

Smoking=yes_no[
st.selectbox("Smoking",yes_no.keys())
]

Hx_Smoking=yes_no[
st.selectbox("Hx Smoking",yes_no.keys())
]

Hx_Radiothreapy=yes_no[
st.selectbox("Hx Radiotherapy",yes_no.keys())
]

Thyroid_Function=thyroid_map[
st.selectbox(
"Thyroid Function",
thyroid_map.keys())
]

Physical_Examination=physical_map[
st.selectbox(
"Physical Examination",
physical_map.keys())
]

Adenopathy=adenopathy_map[
st.selectbox(
"Adenopathy",
adenopathy_map.keys())
]

Pathology=pathology_map[
st.selectbox(
"Pathology",
pathology_map.keys())
]

Focality=focality_map[
st.selectbox(
"Focality",
focality_map.keys())
]

Risk=risk_map[
st.selectbox(
"Risk",
risk_map.keys())
]

T=t_map[
st.selectbox(
"T",
t_map.keys())
]

N=n_map[
st.selectbox(
"N",
n_map.keys())
]

M=m_map[
st.selectbox(
"M",
m_map.keys())
]

Stage=stage_map[
st.selectbox(
"Stage",
stage_map.keys())
]

Response=response_map[
st.selectbox(
"Response",
response_map.keys())
]

if st.button("Predict"):

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

    if pred[0]==1:
        st.error("⚠ High chance of recurrence")
    else:
        st.success("✅ Low recurrence risk")