import pandas as pd


def create_time_since_signup(df):

    df["time_since_signup"] = (
        df["purchase_time"]
        - df["signup_time"]
    ).dt.total_seconds()

    return df


def create_hour_of_day(df):

    df["hour_of_day"] = (
        df["purchase_time"]
        .dt.hour
    )

    return df


def create_day_of_week(df):

    df["day_of_week"] = (
        df["purchase_time"]
        .dt.dayofweek
    )

    return df


def create_transaction_count(df):

    df["transaction_count"] = (
        df.groupby("user_id")
        ["user_id"]
        .transform("count")
    )

    return df


def create_device_transaction_count(df):

    df["device_transaction_count"] = (
        df.groupby("device_id")
        ["device_id"]
        .transform("count")
    )

    return df