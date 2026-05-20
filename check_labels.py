import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("data/Thyroid_Diff.csv")

for col in df.select_dtypes(include='object').columns:

    le = LabelEncoder()

    df[col] = le.fit_transform(df[col])

    print("\n",col)

    for i,label in enumerate(le.classes_):
        print(i,"→",label)