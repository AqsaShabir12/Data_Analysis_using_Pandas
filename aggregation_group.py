import pandas as pd

data = {
    "Name": ["John", "Jane", "Doe", "Smith", "Emily", "Michael", "Sarah", "David", "Laura", "Chris"],
    "Age": [28, 34, 29, 34, 25, 30, 28, 40, 22, 30],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Denver", "San Diego", "Chicago", "Houston", "Seattle", "Denver"],
    "Salary": [70000, 80000, 60000, 90000, 50000, 75000, 80000, 75000, 65000, 65000],
    "Department": ["HR", "Finance", "IT", "Marketing", "Sales", "IT", "HR", "Finance", "Marketing", "Sales"],
    "Performance": [100, 95, 85, 90, 80, 75, 88, 92, 78, 84]
}

df = pd.DataFrame(data)
print(df)

# Aggregation functions
agg = df["Age"].mean()
print(f"Avg of Age: {agg}")
ag = df["Salary"].sum()
print(f"Sum of Salary: {ag}")

# Aggregating using groupby for single column
groupby = df.groupby("Age")["Salary"].sum()
print(f"Grouping Age and summing Salary:\n", groupby)
# Aggregating using groupby for multiple columns
groupped = df.groupby(["Age","Department"])["Performance"].mean()
print(f"Grouping Age and Department and taking mean of Performance:\n", groupped)
