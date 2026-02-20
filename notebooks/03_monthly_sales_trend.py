import pandas as pd
import matplotlib.pyplot as plt

# 1. Load cleaned data
df = pd.read_csv("data/data_processed/retail_sales_clean.csv",
                 parse_dates=["Order Date", "Ship Date"])

# 2. Ensure helper columns exist (in case you re-run from clean)
df["Order_YearMonth"] = df["Order Date"].dt.to_period("M").astype(str)

# 3. Aggregate monthly sales
monthly_sales = (
    df.groupby("Order_YearMonth", as_index=False)["Sales"]
      .sum()
      .rename(columns={"Sales": "Total_Sales"})
)

# 4. Create a proper datetime column for plotting
monthly_sales["YearMonth_dt"] = pd.to_datetime(monthly_sales["Order_YearMonth"] + "-01")

print("Monthly sales (first 5 rows):")
print(monthly_sales.head())

print("\nTime range in monthly data:")
print(monthly_sales["YearMonth_dt"].min(), "->", monthly_sales["YearMonth_dt"].max())

# 5. Plot monthly sales trend
plt.figure(figsize=(12, 5))
plt.plot(monthly_sales["YearMonth_dt"], monthly_sales["Total_Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()