import pandas as pd

# calculate overall total spent 
def total_spent(df):
    return df["Total Charged"].sum()

# calculate the average spent per order
def average_spent(df):
    return df["Total Charged"].mean()

# calculate the total sales tax spent
def sales_tax(df):
    return df["Tax Charged"].sum()

# find the largest amount spent on an order
def largest_order(df):
    return df["Total Charged"].max()

# find the smallest amount spent on an order
def smallest_order(df):
    return df["Total Charged"].min()
