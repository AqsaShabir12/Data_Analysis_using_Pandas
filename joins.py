import pandas as pd

customer_data = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4, 5],
    "CustomerName": ["John Doe", "Jane Smith", "Emily Davis", "Michael Brown", "Sarah Wilson"],
    "Country": ["USA", "Canada", "USA", "Canada", "USA"],
    "Age": [28, 34, 29, 42, 25],
    "City": ["New York", "Toronto", "Chicago", "Vancouver", "Phoenix"]
})

order_data = pd.DataFrame({
    "OrderID": [101, 102, 103, 104, 105],
    "CustomerID": [1, 2, 4, 6, 8],
    "Product": ["Laptop", "Smartphone", "Tablet", "Monitor", "Keyboard"],
    "Quantity": [1, 2, 1, 3, 5],
    "Price": [1200.00, 800.00, 300.00, 400.00, 50.00]
})

merged = pd.merge(customer_data, order_data, on = "CustomerID", how = "inner")
print("Inner Join:")
print(merged)
print("------------------------------------------------")
merged = pd.merge(customer_data, order_data, on = "CustomerID", how = "outer")
print("Outer Join:")
print(merged)
print("------------------------------------------------")
merged = pd.merge(customer_data, order_data, on = "CustomerID", how = "left")
print("Left Join:")
print(merged)
print("------------------------------------------------")
merged = pd.merge(customer_data, order_data, on = "CustomerID", how = "right")
print("Right Join:")
print(merged)
print("------------------------------------------------")
merged = pd.merge(customer_data, order_data, how = "cross")
print("Cross Join:")
print(merged)
print("------------------------------------------------")

concatenated = pd.concat([customer_data, order_data], axis=0, ignore_index=True) # Concatenate along rows
print("Concatenated DataFrame:")
print(concatenated)
print("------------------------------------------------")

# save the merged DataFrame to a CSV file
merged.to_csv("merged_data.csv", index=False)
