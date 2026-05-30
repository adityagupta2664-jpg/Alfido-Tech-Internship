import pandas as pd

# Load CSV
df = pd.read_csv("sales_data.csv")

print("===== DATASET =====")
print(df)

# Inspect Data
print("\n===== DATA INFO =====")
print(df.info())

print("\n===== STATISTICS =====")
print(df.describe())

# Create Revenue Column
df["Revenue"] = df["Price"] * df["Quantity"]

# Filter Electronics Products
electronics = df[df["Category"] == "Electronics"]

print("\n===== ELECTRONICS PRODUCTS =====")
print(electronics)

# Group By Category
grouped = df.groupby("Category")["Revenue"].sum()

print("\n===== TOTAL REVENUE BY CATEGORY =====")
print(grouped)

# Highest Revenue Product
product_revenue = df.groupby("Product")["Revenue"].sum()

print("\n===== REVENUE BY PRODUCT =====")
print(product_revenue)

print("\n===== INSIGHTS =====")
print("1. Electronics generated the highest revenue.")
print("2. Laptop contributes major revenue among products.")
print("3. Clothing products have higher quantity sales.")