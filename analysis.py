import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# LOAD DATA
# -------------------------
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

# -------------------------
# CLEAN DATA
# -------------------------
df = df.dropna()
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])
df = df.drop_duplicates()

print("Cleaned Shape:", df.shape)

# -------------------------
# KPI CALCULATIONS
# -------------------------

# Total Revenue
total_revenue = df["Sales"].sum()
print("\nTotal Revenue:", round(total_revenue, 2))

# Monthly Sales Trend
monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()

# Top 5 Products
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head()

# Most Profitable Category
category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)

# -------------------------
# ADVANCED ANALYSIS
# Profit vs Discount
# -------------------------
discount_profit = df.groupby("Discount")["Profit"].mean()

print("\nAverage Profit per Discount Level:\n")
print(discount_profit)

# -------------------------
# DASHBOARD VISUALS
# -------------------------

# Monthly Sales Trend
plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Category Sales
plt.figure()
df.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Sales")
plt.show()

# Region Share
plt.figure()
df.groupby("Region")["Sales"].sum().plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales Distribution by Region")
plt.ylabel("")
plt.show()

# Profit vs Discount
plt.figure()
discount_profit.plot(kind="line", marker="o")
plt.title("Profit vs Discount Relationship")
plt.xlabel("Discount")
plt.ylabel("Average Profit")
plt.show()

# Top Products Table
print("\nTop 5 Products by Sales:\n")
print(top_products)
