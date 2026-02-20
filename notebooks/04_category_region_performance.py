import pandas as pd
import matplotlib.pyplot as plt

# 1. Load cleaned data
df = pd.read_csv("data/data_processed/retail_sales_clean.csv",
                 parse_dates=["Order Date", "Ship Date"])

# 2. Category-level sales
cat_sales = (
    df.groupby("Category", as_index=False)["Sales"]
      .sum()
      .rename(columns={"Sales": "Total_Sales"})
      .sort_values("Total_Sales", ascending=False)
)

print("Category sales:")
print(cat_sales)

plt.figure(figsize=(6, 4))
plt.bar(cat_sales["Category"], cat_sales["Total_Sales"])
plt.title("Total Sales by Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

# 3. Region-level sales
reg_sales = (
    df.groupby("Region", as_index=False)["Sales"]
      .sum()
      .rename(columns={"Sales": "Total_Sales"})
      .sort_values("Total_Sales", ascending=False)
)

print("\nRegion sales:")
print(reg_sales)

plt.figure(figsize=(6, 4))
plt.bar(reg_sales["Region"], reg_sales["Total_Sales"])
plt.title("Total Sales by Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()