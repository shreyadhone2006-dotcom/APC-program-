import pandas as pd

data = {
    "Product_ID": [101, 102, 103, 104, 105],
    "Product_Name": ["Laptop", "Mobile", "Keyboard", "Mouse", "Monitor"],
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories", "Electronics"],
    "Price": [50000, 30000, 1500, 800, 12000],
    "Quantity": [2, 3, 10, 15, 5]
}

df = pd.DataFrame(data)

df["Total_Amount"] = df["Price"] * df["Quantity"]

print("DataFrame:")
print(df)

print("\nProduct having highest total sales:")
print(df.loc[df["Total_Amount"].idxmax()])