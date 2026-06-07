import matplotlib.pyplot as plt
import seaborn as sns


def plot_distribution(df, column):

    plt.figure(figsize=(8, 5))

    sns.histplot(
        df[column],
        kde=True
    )

    plt.title(column)

    plt.show()


def plot_class_distribution(df, target):

    sns.countplot(
        x=target,
        data=df
    )

    plt.show()