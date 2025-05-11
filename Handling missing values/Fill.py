import pandas as pd

data = {
    "Name": ["John", None, "Doe", "Smith", "Emily", "Michael", "Sarah", "David", "Laura", "Chris"],
    "Age": [28, None, 29, 42, 25, 30, 35, 40, 22, 31],
    "City": ["New York", None, "Chicago", "Houston", "Phoenix", "San Diego", "Dallas", "Austin", "Seattle", "Denver"],
    "Salary": [70000, None, 60000, 90000, 50000, 75000, 85000, 95000, 55000, 65000],
    "Experience": [5, None, 3, 10, 2, 6, 8, 12, 1, 4],
    "Department": ["HR", None, "IT", "Marketing", "Sales", "IT", "HR", "Finance", "Marketing", "Sales"],
    "Performance": [100, None, 85, 90, 80, 75, 88, 92, 78, 84]
}

df = pd.DataFrame(data)
print(df)
# Filling out missing values with a specific value

# df_filled = df.fillna(0, inplace= True)
# print(f"Data with missing values filled with 0:\n", df)

# Filling out missing values with mean of the column
# df["Salary"].fillna(df["Salary"].mean(), inplace=True)
# print(f"Data with missing values filled with mean of salary:\n", df)

# df["Age"].fillna(df["Age"].mean(), inplace=True)
# print(df)


#Interpolating missing values
# Interpolation is a method of estimating unknown values that fall between known values.
# It is commonly used in time series data to fill in missing values based on the surrounding data points. However, its disadvantage is that it can introduce bias if the data is not evenly distributed or if there are outliers. Also cannot work on the object data type.
# Many types of interpolation methods are available, including linear, polynomial, and spline interpolation. The choice of method depends on the nature of the data and the desired level of accuracy.
df["Age"] = df["Age"].interpolate(method = "polynomial", order = 2)
df["Salary"] = df["Salary"].interpolate(method = "linear")
df["Experience"] = df["Experience"].fillna(method="bfill").fillna(df["Experience"].mean())
df["Performance"].fillna(df["Performance"].mean(), inplace=True)
df["City"].fillna("Unknown", inplace=True)
df["Department"].fillna("Unknown", inplace=True)
df["Name"].fillna("Unknown", inplace=True)
print(f"Data with missing values filled with Interpolation:\n", df)


# Sorting values in ascending order
df.sort_values(by = "Salary", ascending= True, inplace = True) # Ascending = True means sort in ascending order, ascending = False means sort in descending order
print(f"Data with missing values filled with Interpolation and sorted Salary:\n", df)
df.sort_values(by = ["Age", "Performance"], ascending= [True, False], inplace = True) 
print(f"Data with missing values filled with Interpolation and sorted by multiple columns:\n", df)