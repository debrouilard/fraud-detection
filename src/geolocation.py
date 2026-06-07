import pandas as pd
import numpy as np


def prepare_ip_data(ip_df):

    ip_df["lower_bound_ip_address"] = (
        ip_df["lower_bound_ip_address"]
        .astype(np.int64)
    )

    ip_df["upper_bound_ip_address"] = (
        ip_df["upper_bound_ip_address"]
        .astype(np.int64)
    )

    return ip_df


def prepare_fraud_ip(fraud_df):

    fraud_df["ip_address"] = (
        fraud_df["ip_address"]
        .astype(np.int64)
    )

    return fraud_df


def merge_country(fraud_df, ip_df):

    fraud_df = fraud_df.sort_values(
        "ip_address"
    )

    ip_df = ip_df.sort_values(
        "lower_bound_ip_address"
    )

    merged = pd.merge_asof(
        fraud_df,
        ip_df,
        left_on="ip_address",
        right_on="lower_bound_ip_address",
        direction="backward"
    )

    merged = merged[
        merged["ip_address"]
        <= merged["upper_bound_ip_address"]
    ]

    return merged