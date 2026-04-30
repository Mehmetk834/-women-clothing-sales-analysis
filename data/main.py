import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/women_clothing_ecommerce_sales.csv")

df["order_date"] = pd.to_datetime(df["order_date"])
df["size"] = df["size"].fillna("Unknown")
df["month"] = df["order_date"].dt.month

print(df["revenue"].sum())
print(df["revenue"].mean())

top_products = df.groupby("sku")["revenue"].sum().sort_values(ascending=False)
print(top_products.head())


top_products.head(10).plot(kind="bar")
plt.title("Top Products by Revenue")
plt.xlabel("Product (SKU)")
plt.ylabel("Total Revenue")
plt.show()


print(df["color"].value_counts())
print(df.groupby("color")["revenue"].sum().sort_values(ascending=False))


df["color"].value_counts().plot(kind="bar")
plt.title("Color Distribution")
plt.xlabel("Color")
plt.ylabel("Count")
plt.show()


print(df["size"].value_counts())

combo = df.groupby(["color","size"])["revenue"].sum().sort_values(ascending=False)
print(combo.head(10))


monthly = df.groupby("month")["revenue"].sum()
print(monthly)


monthly.plot(kind="bar")
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.show()


print(df.groupby(["month","color"])["revenue"].sum().sort_values(ascending=False).head(10))

print(df.groupby("unit_price")["quantity"].sum().head())