from sklearn.preprocessing import LabelEncoder

def preprocess(df):

    le=LabelEncoder()

    for col in df.select_dtypes(include='object').columns:

        df[col]=le.fit_transform(df[col])

    X=df.iloc[:,:-1]

    y=df.iloc[:,-1]

    return X,y