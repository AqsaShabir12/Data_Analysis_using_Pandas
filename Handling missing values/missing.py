import pandas as pd

data = {
    "Name": ["John", None, "Doe", "Smith", "Emily", "Michael", "Sarah", "David", "Laura", "Chris"],
    "Age": [28, None, 29, 42, 25, 30, 35, 40, 22, 31],
    "City": ["New York", None, "Chicago", "Houston", "Phoenix", "San Diego", "Dallas", "Austin", "Seattle", "Denver"],
    "Salary": [70000, None, 60000, 90000, 50000, 75000, 85000, 95000, 55000, 65000],
    "Department": ["HR", None, "IT", "Marketing", "Sales", "IT", "HR", "Finance", "Marketing", "Sales"],
    "Performance": [100, None, 85, 90, 80, 75, 88, 92, 78, 84]
}

#Nan - Not a Number
#None - Object null value

df = pd.DataFrame(data)
print(df)

# Checking out if there are any missing values in the dataset
print(df.isnull())

# Checking out the total number of missing values in the dataset
print(df.isnull().sum())


