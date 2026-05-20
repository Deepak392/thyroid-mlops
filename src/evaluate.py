from sklearn.metrics import accuracy_score
import mlflow

def evaluate(model,X_test,y_test):


    pred=model.predict(X_test)

    acc=accuracy_score(
        y_test,
        pred
    )

    mlflow.log_metric(
        "accuracy",
        acc
    )

    print("Accuracy:",acc)