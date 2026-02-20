import pandas as pd

# 1. Load cleaned data
df = pd.read_csv("data/data_processed/retail_sales_clean.csv",
                 parse_dates=["Order Date", "Ship Date"])

# 2. Time helper columns
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["YearMonth"] = df["Order Date"].dt.to_period("M").astype(str)

# 3. Monthly sales (for YoY / MoM in Excel)
monthly_sales = (
    df.groupby(["Year", "Month", "YearMonth"], as_index=False)["Sales"]
      .sum()
      .rename(columns={"Sales": "Total_Sales"})
      .sort_values(["Year", "Month"])
)

# 4. Category sales
category_sales = (
    df.groupby("Category", as_index=False)["Sales"]
      .sum()
      .rename(columns={"Sales": "Total_Sales"})
      .sort_values("Total_Sales", ascending=False)
)

# 5. Region sales
region_sales = (
    df.groupby("Region", as_index=False)["Sales"]
      .sum()
      .rename(columns={"Sales": "Total_Sales"})
      .sort_values("Total_Sales", ascending=False)
)

# 6. Write to Excel (multi-sheet)
output_path = "excel/Retail_KPI_Model.xlsx"
with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
    monthly_sales.to_excel(writer, sheet_name="Monthly_Sales", index=False)
    category_sales.to_excel(writer, sheet_name="Category_Sales", index=False)
    region_sales.to_excel(writer, sheet_name="Region_Sales", index=False)

print(f"KPI source file created: {output_path}")