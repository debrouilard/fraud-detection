import pandas as pd

def clean_data(df):
    """
    Remove duplicates.
    """

    df = df.drop_duplicates()

    return df


def convert_datetime_columns(df):

    if "signup_time" in df.columns:
        df["signup_time"] = pd.to_datetime(df["signup_time"])

    if "purchase_time" in df.columns:
        df["purchase_time"] = pd.to_datetime(df["purchase_time"])

    return df


def missing_value_report(df):

    report = pd.DataFrame({
        "missing_count": df.isnull().sum(),
        "percentage":
            (df.isnull().sum() / len(df)) * 100
    })

    return report