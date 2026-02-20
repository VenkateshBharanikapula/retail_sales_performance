import pandas as pd

# 1. Load cleaned data
df = pd.read_csv(
    "data/data_processed/retail_sales_clean.csv",
    parse_dates=["Order Date", "Ship Date"]
)

# 2. Keep only the original 18 columns, in the correct order
cols = [
    "Row ID",
    "Order ID",
    "Order Date",
    "Ship Date",
    "Ship Mode",
    "Customer ID",
    "Customer Name",
    "Segment",
    "Country",
    "City",
    "State",
    "Postal Code",
    "Region",
    "Product ID",
    "Category",
    "Sub-Category",
    "Product Name",
    "Sales",
]

df_out = df[cols].copy()

# 3. Save to a SQL-friendly CSV (ISO dates)
output_path = "data/data_processed/retail_sales_for_sql.csv"
df_out.to_csv(output_path, index=False, date_format="%Y-%m-%d")

print(f"Saved for SQL: {output_path}")