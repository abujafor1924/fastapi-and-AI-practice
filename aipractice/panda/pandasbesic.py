import pandas as pd

import sqlite3

number=pd.Series([1, 2, 3, 4, 5])

# print("Series:",number)
# print("First element:",number[0])
# print("Slice [1:4]:",number[1:4])
# print("Sum of slice:",number[1:4].sum())
# print("Mean of slice:",number[1:4].mean())
# print("Max of slice:",number[1:4].max())
# print("Min of slice:",number[1:4].min())
# print("Standard deviation of slice:",number[1:4].std())
# print("Variance of slice:",number[1:4].var())



data = {
    "Name": ["Jafor", "Rahim", "Karim"],
    "Age": [24, 22, 26],
    "Salary": [50000, 40000, 60000]
}

# df=pd.DataFrame(data)

# print("DataFrame:\n", df)
# print("First row:\n", df.iloc[0])
# print("First 3 rows:\n", df.iloc[:3])
# print("First 3 rows, first 2 columns:\n", df.iloc[:3, :2])
# print("Age > 25:\n", df[df["Age"] > 25])
# print("Multiple conditions (Age > 25 and Salary > 50000):\n", df[(df["Age"] > 25) & (df["Salary"] > 50000)])
# print("OR condition (Age > 25 or Salary > 50000):\n", df[(df["Age"] > 25) | (df["Salary"] > 50000)])
# print("isin() condition (Age in [22, 24]):\n", df[df["Age"].isin([22, 24])])
# print("Check missing values:\n", df.isnull())
# print("Count missing values:\n", df.isnull().sum()) 



# Read CSV
df = pd.read_csv("employees.csv")
print("CSV DataFrame:\n", df)

# ==========================
# Export to different formats
# ==========================

# CSV
df.to_csv("new.csv", index=False)

# Excel (requires: pip install openpyxl)
df.to_excel("new.xlsx", index=False)

# JSON
df.to_json("new.json", orient="records", indent=4)

# HTML
df.to_html("new.html", index=False)

# SQLite Database
conn = sqlite3.connect("database.db")
df.to_sql("employees", con=conn, if_exists="replace", index=False)

# Parquet (requires: pip install pyarrow)
df.to_parquet("new.parquet", index=False)

# Feather (requires: pip install pyarrow)
# Feather does NOT support index parameter
df.to_feather("new.feather")

# Stata
df.to_stata("new.dta", write_index=False)

# Pickle
df.to_pickle("new.pkl")

# HDF5 (requires: pip install tables)
# df.to_hdf("new.h5", key="employees", mode="w")

# ==========================
# Data Operations
# ==========================

# Save last rows to another SQL table
df.tail(2).to_sql(
    "employees_tail",
    con=conn,
    if_exists="replace",
    index=False
)

# Save random sample
df.sample(n=2).to_csv("sample.csv", index=False)

# Save DataFrame information
with open("info.txt", "w") as f:
    df.info(buf=f)

# Save descriptive statistics
df.describe().to_csv("describe.csv")

# Mean salary by department
df.groupby("Department")["Salary"].mean().to_csv(
    "department_salary_mean.csv"
)

# ==========================
# Basic Information
# ==========================

print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Data Types:\n", df.dtypes)

# Close database connection
conn.close()
