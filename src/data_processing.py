import pandas as pd

def load_data():
    x_train = pd.read_csv("/Users/moussa-kalla/Challenge Data SNCF/data/raw/x_train_final.csv")
    y_train = pd.read_csv("d/Users/moussa-kalla/Challenge Data SNCF/data/raw/y_train_final_j5KGWWK.csv")
    x_test = pd.read_csv("/Users/moussa-kalla/Challenge Data SNCF/data/raw/x_test_final.csv")
    return x_train, y_train, x_test