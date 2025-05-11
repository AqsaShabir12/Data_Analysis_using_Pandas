import pandas as pd
# Importing the datafile using pandas
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
# Displaying the entire data
print(df)
# Displaying the first 5 rows of the data
print("Printing First 5 rows of data", df.head())
# Printing the last 5 rows of data
print("Printing Last 5 rows of data", df.tail())
# Summarizing the data
print(df.info()) 
#Descriptive statistics of your numerical columns
print(df.describe())
# printing the shape of the data
print(f"Shape of the data is {df.shape}")
# Printing the columns of the data  
print(f"Columns of the data are {df.columns}")

# Selecting Single column
quantity = df["QUANTITYORDERED"]
print(f"Selecting Single column",quantity)
# printing first 5 rows of a single column
print(f"Printing first 5 rows of a single column", quantity.head())
# Selecting Multiple columns
quantity_price = df[["QUANTITYORDERED","PRICEEACH"]]
print(f"Selecting Multiple columns",quantity_price)

#Filtering out specific rows
subset = df[df["QUANTITYORDERED"] > 50][["QUANTITYORDERED","PRICEEACH"]]  #Filtering out specific rows with specific columns but priting different columns
print(f"Filtering out specific rows",subset)

#Filtering out multiple rows with and condition
multiple_subset = df[(df["QUANTITYORDERED"] > 50) & (df["PRICEEACH"] < 60)]
print(f"Filtering out multiple rows",multiple_subset)

#Filtering out multiple rows with or condition
Filtered = df[(df["COUNTRY"] == "USA") | (df["PRICEEACH"] < 60)]
print(f"Filtering out multiple rows using OR condition",Filtered)