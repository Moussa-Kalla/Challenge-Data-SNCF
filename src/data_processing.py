import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_process_and_encode_data():
    label_encoder = LabelEncoder()

    x_train = pd.read_csv("data/x_train_final.csv")
    x_train['date'] = pd.to_datetime(x_train['date'])
    x_train['date'] = x_train['date'].map(pd.Timestamp.toordinal)
    x_train[["gare"]] = x_train[["gare"]].apply(label_encoder.fit_transform)
    x_train = x_train.drop(columns=["Unnamed: 0", "Unnamed: 0.1", "train", "date","gare"], errors='ignore')

    x_test = pd.read_csv("data/x_test_final.csv")
    x_test['date'] = pd.to_datetime(x_test['date'])
    x_test['date'] = x_test['date'].map(pd.Timestamp.toordinal)
    x_test[["gare"]] = x_test[["gare"]].apply(label_encoder.fit_transform)
    x_test = x_test.drop(columns=["Unnamed: 0","train", "date","gare"], errors='ignore')

    y_train = pd.read_csv("data/y_train_final_j5KGWWK.csv")
    y_train = y_train.drop(columns=["Unnamed: 0"], errors='ignore')
    return x_train, y_train, x_test