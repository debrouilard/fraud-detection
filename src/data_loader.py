import pandas as pd

def load_fraud_data(path):
    return pd.read_csv(path)

def load_creditcard_data(path):
    return pd.read_csv(path)

def load_ip_data(path):
    return pd.read_csv(path)