import pandas as pd

data = {
    "Name": ["John", "Jane", "Doe", "Smith", "Emily", "Michael", "Sarah", "David", "Laura", "Chris"],
    "Age": [28, 34, 29, 42, 25, 30, 35, 40, 22, 31],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "San Diego", "Dallas", "Austin", "Seattle", "Denver"],
    "Salary": [70000, 80000, 60000, 90000, 50000, 75000, 85000, 95000, 55000, 65000],
    "Department": ["HR", "Finance", "IT", "Marketing", "Sales", "IT", "HR", "Finance", "Marketing", "Sales"],
    "Performance": [100, 95, 85, 90, 80, 75, 88, 92, 78, 84]
}

df = pd.DataFrame(data)

print(df)

#Inserting a single column in dataset which is added at the end of the dataset without defining the order of the column
df["Bonus"] = df["Salary"] * 0.1
print(f"Data with Bonus column added:\n", df)

# Inserting a column in dataset at a specific position
df.insert(0, "Employee_id", [1,2,3,4,5,6,7,8,9,10])
print(f"Data with Employee_id column added at specific position:\n", df)

# Updating an entry in dataset
df.loc[0,"City"] = "San Francisco"
print(f"Data with updated entry using loc:\n", df)

#Updating an entire column in dataset using specific condition
df.loc[df["Department"] == "IT", "Salary"] = df["Salary"] * 1.2
print(f"Data with updated Salary for IT department Using condition with loc:\n", df)
#or
df["Age"] = df["Age"] - 1
print(f"Data with updated Age without loc:\n", df)

#DROPPING A COLUMN
df.drop(["Performance", "City"],inplace=True, axis=1) # axis=1 means drop column, axis=0 means drop row, 
                                                    #inplace=True means modify the original dataframe

print(f"Data with Performance column dropped:\n", df)