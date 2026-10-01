import pandas as pd

data = {
    "Order_ID": [1, 2, 3, 4, 5],
    "Customer": ["Amit", "Neha", "Rahul", "Sneha", "Priya"],
    "Product": ["Laptop", "Mobile", "Monitor", "Keyboard", "Tablet"],
    "Quantity": [2, 3, 2, 5, 1],
    "Price": [50000, 20000, 15000, 2000, 30000],
    "Discount": [5000, 2000, 1000, 500, 3000]
}

df = pd.DataFrame(data)

df["Final_Amount"] = (df["Quantity"] * df["Price"]) - df["Discount"]

print("All Orders:")
print(df)

print("\nOrders above 5000:")
print(df[df["Final_Amount"] > 5000])

print("\nHighest-value order:")
print(df.loc[df["Final_Amount"].idxmax()])

print("\nAverage Order Value:")
print(df["Final_Amount"].mean())