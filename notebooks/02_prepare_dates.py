import pandas as pd

# 1. Load data (no parse_dates yet)
df = pd.read_csv("data/data_raw/retail_sales_raw.csv")

# 2. Convert date columns explicitly (day-first format)
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True, errors="coerce")

# 3. Check dtypes for dates
print("Date dtypes:")
print(df[["Order Date", "Ship Date"]].dtypes)

# 4. Check for any conversion issues
print("\nNaT counts (failed date parses):")
print(df[["Order Date", "Ship Date"]].isna().sum())

# 5. Basic time range
print("\nOrder Date range:")
print("Min:", df["Order Date"].min())
print("Max:", df["Order Date"].max())

# 6. Create helper time columns
df["Order_Year"] = df["Order Date"].dt.year
df["Order_Month"] = df["Order Date"].dt.month
df["Order_YearMonth"] = df["Order Date"].dt.to_period("M").astype(str)

print("\nSample of time columns:")
print(df[["Order Date", "Order_Year", "Order_Month", "Order_YearMonth"]].head())

# 7. Save cleaned dataset
output_path = "data/data_processed/retail_sales_clean.csv"
df.to_csv(output_path, index=False)

print(f"\nCleaned data saved to: {output_path}")