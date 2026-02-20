import pandas as pd
import matplotlib.pyplot as plt

# 1. Load cleaned data
df = pd.read_csv("data/data_processed/retail_sales_clean.csv",
                 parse_dates=["Order Date", "Ship Date"])

# 2. Sales by Segment
seg_sales = (
    df.groupby("Segment", as_index=False)["Sales"]
      .sum()
      .rename(columns={"Sales": "Total_Sales"})
      .sort_values("Total_Sales", ascending=False)
)

print("Sales by Segment:")
print(seg_sales)

plt.figure(figsize=(6, 4))
plt.bar(seg_sales["Segment"], seg_sales["Total_Sales"])
plt.title("Total Sales by Customer Segment")
plt.ylabel("Total Sales")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# 3. Segment x Region (top combos)
seg_reg_sales = (
    df.groupby(["Region", "Segment"], as_index=False)["Sales"]
      .sum()
      .rename(columns={"Sales": "Total_Sales"})
      .sort_values("Total_Sales", ascending=False)
)

print("\nTop Segment x Region combinations:")
print(seg_reg_sales.head(10))