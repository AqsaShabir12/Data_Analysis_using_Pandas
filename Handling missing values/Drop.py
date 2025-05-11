import pandas as pd

data = {
    "Name": ["John", None, "Doe", "Smith", "Emily", "Michael", "Sarah", "David", "Laura", "Chris"],
    "Age": [28, None, 29, 42, 25, 30, 35, 40, 22, 31],
    "City": ["New York", None, "Chicago", "Houston", "Phoenix", "San Diego", "Dallas", "Austin", "Seattle", "Denver"],
    "Salary": [70000, None, 60000, 90000, 50000, 75000, 85000, 95000, 55000, 65000],
    "Department": ["HR", None, "IT", "Marketing", "Sales", "IT", "HR", "Finance", "Marketing", "Sales"],
    "Performance": [100, None, 85, 90, 80, 75, 88, 92, 78, 84]
}

df = pd.DataFrame(data)

# Dropping rows with missing values
df_dropped = df.dropna(inplace= True)
print(f"Data with missing values dropped:\n", df)