import pandas as pd

# open properly named csv file
def open_csv():
    return pd.read_csv('amazon-orders.csv')

# remove dollar signs and convert data to floats
def data_clean(df):
    df = df.fillna(0)
    df["Total Charged"] = df["Total Charged"].str.replace('$','').astype(float)
    df["Tax Charged"] = df["Tax Charged"].str.replace('$','').astype(float)
    return df