import pandas as pd

data = {
    "Name": ["John", "Jane", "Doe"],
    "Age": [28, 34, 29],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
df.to_csv("output.csv")