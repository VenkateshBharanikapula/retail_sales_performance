import pandas as pd

# 1. Load data
df = pd.read_csv("data/data_raw/retail_sales_raw.csv")

# 2. Basic structure
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nDtypes:")
print(df.dtypes)

print("\nHead:")
print(df.head())

print("\nMissing value % (top 15):")
nulls = df.isna().mean().sort_values(ascending=False)
print(nulls.head(15))

print("\nNumeric describe:")
print(df.describe())