# 🐼 Pandas

This repository contains a collection of hands-on practice scripts for learning and mastering **Pandas**, one of the most powerful Python libraries for data manipulation and analysis.

Each script demonstrates a key functionality or workflow in data cleaning, transformation, grouping, joining, and missing data handling.

---

## Folder Overview

### Handling missing values

- **Drop.py**  
  Drops rows with missing values using `dropna()`.

- **Fill.py**  
  Demonstrates filling missing values with means, constants, and interpolation (linear, polynomial, etc.), and sorting.

- **missing.py**  
  Detects missing values using `isnull()` and counts them with `sum()`.

---

## Project Scripts

### aggregation_group.py  
Demonstrates:
- Basic aggregation functions (`mean()`, `sum()`)
- Grouping by one or more columns (`groupby`)
- Aggregating grouped results

### joins.py  
Explains how to:
- Merge DataFrames using different join types (`inner`, `outer`, `left`, `right`, `cross`)
- Concatenate DataFrames using `concat()`
- Save the merged result to a CSV

### app.py  
Covers:
- Reading CSV files using Pandas
- Viewing, describing, and summarizing the dataset
- Selecting single/multiple columns
- Filtering rows using logical conditions

### app2.py  
Illustrates:
- Adding new columns (e.g., calculated bonus)
- Inserting columns at specific positions
- Updating entries (both single and entire columns)
- Dropping specific columns

### save.py  
(Assumed to handle saving cleaned/transformed DataFrames to file)

---

## Sample Datasets

Included for hands-on practice with real data:

- `sales_data_sample.csv`  
- `merged_data.csv`  
- `output.csv`  
- `sample_Data.json`  
- `SampleSuperstore.xlsx`

These files are used across different scripts for cleaning, joining, aggregation, and export demonstrations.

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/aqsashabir12/pandas.git
   cd pandas
    ```
2. Install Pandas (if not installed):
   ```bash
   pip install pandas
    ```
3. Run any script. For Example:
   ```bash
   python aggregation_group.py
    ```
