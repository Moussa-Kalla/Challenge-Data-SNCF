import pandas as pd

def load_data():
    x_train = pd.read_csv("data/raw/x_train_final.csv")
    y_train = pd.read_csv("data/raw/y_train_final_j5KGWWK.csv")
    x_test = pd.read_csv("data/raw/x_test_final.csv")
    x_train = x_train.drop(columns=["Unnamed: 0", "Unnamed: 0.1"], errors='ignore')
    x_test = x_test.drop(columns=["Unnamed: 0"], errors='ignore')
    y_train = y_train.drop(columns=["Unnamed: 0"], errors='ignore')
    return x_train, y_train, x_test