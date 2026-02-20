import pandas as pd
import matplotlib.pyplot as plt

# 1. Load cleaned data
df = pd.read_csv("data/data_processed/retail_sales_clean.csv",
                 parse_dates=["Order Date", "Ship Date"])

# 2. Sales by Sub-Category
subcat_sales = (
    df.groupby("Sub-Category", as_index=False)["Sales"]
      .sum()
      .rename(columns={"Sales": "Total_Sales"})
      .sort_values("Total_Sales", ascending=False)
)

print("Sales by Sub-Category (top 10):")
print(subcat_sales.head(10))

plt.figure(figsize=(10, 5))
plt.bar(subcat_sales["Sub-Category"], subcat_sales["Total_Sales"])
plt.title("Total Sales by Sub-Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Top 10 Products by Sales
prod_sales = (
    df.groupby("Product Name", as_index=False)["Sales"]
      .sum()
      .rename(columns={"Sales": "Total_Sales"})
      .sort_values("Total_Sales", ascending=False)
)

print("\nTop 10 Products by Sales:")
print(prod_sales.head(10))