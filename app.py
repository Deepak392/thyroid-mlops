from src.data_ingestion import load_data
from src.preprocess import preprocess
from src.train import train_model
from src.evaluate import evaluate

import mlflow


mlflow.set_experiment(
    "thyroid_prediction"
)

with mlflow.start_run():

    df=load_data()

    X,y=preprocess(df)

    model,X_test,y_test=\
    train_model(X,y)

    evaluate(
        model,
        X_test,
        y_test
    )