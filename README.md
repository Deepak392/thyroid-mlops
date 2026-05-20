# 🩺 ThyroPredict AI — Thyroid Cancer Recurrence Prediction using MLOps

An end-to-end Machine Learning + MLOps project that predicts the likelihood of thyroid cancer recurrence using patient clinical data and diagnostic indicators.

This project demonstrates a complete MLOps workflow including:

- Machine Learning model training
- MLflow experiment tracking
- GitHub version control
- Docker containerization
- Kubernetes deployment
- AWS S3 artifact storage
- GitHub Actions CI/CD
- Streamlit Cloud deployment

---

## 🚀 Live Demo

🌐 Streamlit App: [Add your Streamlit link here]

📂 GitHub Repository: [Add your GitHub repo link here]

---

## 📌 Problem Statement

Thyroid cancer recurrence prediction is an important healthcare task. Early identification of recurrence risk can assist clinicians in improving monitoring and treatment strategies.

This system uses machine learning to predict recurrence risk based on:

- Patient history
- Clinical indicators
- Cancer stage
- Pathology information
- Treatment response

---

## 🧠 Machine Learning Workflow

Dataset  
↓  
Data Preprocessing  
↓  
Feature Encoding  
↓  
Train/Test Split  
↓  
Model Training  
↓  
MLflow Experiment Tracking  
↓  
Model Serialization  
↓  
Docker Containerization  
↓  
AWS S3 Storage  
↓  
Kubernetes Deployment  
↓  
GitHub Actions Automation  
↓  
Streamlit Deployment  

---

## 📊 Dataset Information

Dataset: Thyroid_Diff.csv

Target Variable:

```txt
Recurred

0 → No
1 → Yes
```

Features used:

```txt
Age
Gender
Smoking
Hx Smoking
Hx Radiothreapy
Thyroid Function
Physical Examination
Adenopathy
Pathology
Focality
Risk
T
N
M
Stage
Response
```

---

## 📁 Project Structure

```txt
thyroid-mlops/
│
├── data/
│   └── Thyroid_Diff.csv
│
├── src/
│   ├── data_ingestion.py
│   ├── preprocess.py
│   ├── train.py
│   └── evaluate.py
│
├── notebooks/
│   └── ML_phase3_deepakkumarpatro.ipynb
│
├── models/
│   └── model.pkl
│
├── .github/
│   └── workflows/
│       └── mlops.yml
│
├── streamlit_app.py
├── Dockerfile
├── kubernetes.yaml
├── requirements.txt
├── app.py
├── README.md
└── .gitignore
```

---

## ⚙️ Technologies Used

### Machine Learning

- Python
- Scikit-learn
- Pandas
- NumPy

### MLOps

- MLflow
- GitHub
- GitHub Actions
- Docker
- Kubernetes
- AWS S3

### Deployment

- Streamlit Cloud

---

## 📈 MLflow Tracking

MLflow is used to:

- Track experiments
- Log metrics
- Compare runs
- Store model artifacts

Run locally:

```bash
mlflow ui
```

Open:

```txt
http://localhost:5000
```

---

## 🐳 Docker Setup

Build Docker image:

```bash
docker build -t thyroidml .
```

Run container:

```bash
docker run thyroidml
```

---

## ☸ Kubernetes Deployment

Apply deployment:

```bash
kubectl apply -f kubernetes.yaml
```

Check status:

```bash
kubectl get pods

kubectl get svc
```

---

## ⚡ GitHub Actions CI/CD

GitHub Actions automatically:

✔ Installs dependencies  
✔ Validates project structure  
✔ Runs ML pipeline  
✔ Builds Docker image

Workflow location:

```txt
.github/workflows/mlops.yml
```

---

## 🌐 Streamlit Deployment

Run locally:

```bash
streamlit run streamlit_app.py
```

Deploy on Streamlit Cloud:

1. Push project to GitHub
2. Login to Streamlit Cloud
3. Select repository
4. Select:

```txt
streamlit_app.py
```

5. Deploy

---

## 📷 Screenshots

Add screenshots here:

- MLflow dashboard
- Streamlit UI
- Docker containers
- Kubernetes pods
- GitHub Actions
- AWS S3 bucket

---

## 📌 Future Improvements

- Deep Learning models
- SHAP explainability
- Real-time API deployment
- Automated retraining
- Continuous monitoring

---

## 👨‍💻 Author

Deepak Kumar Patro

B.Tech Computing & Data Science  
Sai University

GitHub: https://github.com/yourusername

---

## ⚠ Disclaimer

This project is intended for educational and research purposes only and should not be used as a substitute for professional medical diagnosis.
