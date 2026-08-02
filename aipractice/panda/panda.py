import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


# Create DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [23, 30, 35, 28],
    "Salary": [50000, 70000, 90000, 65000],
    "City": ["Dhaka", "Dhaka", "Khulna", "Rajshahi"]
})

print(df)


# Read CSV file
df = pd.read_csv("students.csv")


# First 5 rows
df.head()

# Last 5 rows
df.tail()

# Dataset information
df.info()

# Statistical summary
df.describe()

# Shape (rows, columns)
df.shape

# Column names
df.columns


# Single column
df["Name"]

# Multiple columns
df[["Name", "Age"]]


# Label based
df.loc[0]

# Position based
df.iloc[0]

# First 3 rows
df.iloc[:3]

# First 3 rows and first 2 columns
df.iloc[:3, :2]


# Age greater than 30
df[df["Age"] > 30]

# Salary greater than 60000
df[df["Salary"] > 60000]

# Multiple conditions (AND)
df[(df["Age"] > 25) & (df["City"] == "Dhaka")]

# Multiple conditions (OR)
df[(df["Age"] > 30) | (df["Salary"] > 70000)]


# Sort by age
df.sort_values("Age")

# Descending
df.sort_values("Salary", ascending=False)

# Add new column
df["Bonus"] = df["Salary"] * 0.10

# Age in days
df["Age_Days"] = df["Age"] * 365

# Increase salary by 10%
df["Salary"] = df["Salary"] * 1.10

# Count missing values
df.isnull().sum()

# Fill missing values
df.fillna(0)

# Fill with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Drop missing rows
df.dropna()

# Count duplicates
df.duplicated().sum()

# Remove duplicates
df.drop_duplicates()


# Count duplicates
df.duplicated().sum()

# Remove duplicates
df.drop_duplicates()

# Count each city
df["City"].value_counts()

# Unique values
df["City"].unique()

# Average salary by city
df.groupby("City")["Salary"].mean()

# Multiple aggregation
df.groupby("City").agg({
    "Salary": "mean",
    "Age": "max"
})


# Square age
df["Age_Square"] = df["Age"].apply(lambda x: x ** 2)

# Convert city to numbers
df["City_Code"] = df["City"].map({
    "Dhaka": 1,
    "Khulna": 2,
    "Rajshahi": 3
})

# Check data types
df.dtypes

# Convert type
df["Age"] = df["Age"].astype("int64")

df1 = pd.DataFrame({
    "ID": [1,2,3],
    "Name": ["A","B","C"]
})

df2 = pd.DataFrame({
    "ID":[1,2,3],
    "Salary":[50000,60000,70000]
})

# Merge two tables
pd.merge(df1, df2, on="ID")

# Combine rows
pd.concat([df1, df2])

# Save dataset
df.to_csv("output.csv", index=False)



# Features
X = df.drop("Target", axis=1)

# Label
y = df["Target"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create new feature
df["Income_Per_Age"] = df["Salary"] / df["Age"]


# Create new feature
df["Income_Per_Age"] = df["Salary"] / df["Age"]


# Convert category into numbers
df["City"] = df["City"].astype("category")

# Category codes
df["City_Code"] = df["City"].cat.codes


import pandas as pd

# Load CSV
df = pd.read_csv("students.csv")

print(df)


# First 5 rows
df.head()

# Last 5 rows
df.tail()

# Dataset information
df.info()

# Statistics
df.describe()

# Single column
df["Name"]

# Multiple columns
df[["Name", "Age"]]


# Label based
df.loc[0]

# Position based
df.iloc[0]

# First 3 rows
df.iloc[:3]

# First 3 rows, first 2 columns
df.iloc[:3, :2]


# Age > 30
df[df["Age"] > 30]

# Multiple conditions
df[(df["Age"] > 25) & (df["Salary"] > 50000)]

# OR
df[(df["Age"] > 25) | (df["City"] == "Dhaka")]

# isin()
df[df["City"].isin(["Dhaka", "Khulna"])]

# Check missing values
df.isnull()

# Count missing values
df.isnull().sum()

# Fill missing values
df.fillna(0)

# Fill Age with average
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Remove missing rows
df.dropna()


# Count duplicates
df.duplicated().sum()

# Remove duplicates
df.drop_duplicates()

# Average salary by city
df.groupby("City")["Salary"].mean()

# Multiple aggregation
df.groupby("City").agg({
    "Age": "mean",
    "Salary": "max"
})

import pandas as pd

employee = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Alice","Bob","Charlie"]
})

salary = pd.DataFrame({
    "ID":[1,2,3],
    "Salary":[50000,70000,90000]
})

# Merge two DataFrames
result = pd.merge(employee, salary, on="ID")

print(result)

# apply()

df["Age_Square"] = df["Age"].apply(lambda x: x*x)

# map()

df["City_Code"] = df["City"].map({
    "Dhaka":1,
    "Khulna":2,
    "Rajshahi":3
})

# Check data type
df.dtypes

# Convert data type
df["Age"] = df["Age"].astype("int64")


# Count each city
df["City"].value_counts()

# Percentage
df["City"].value_counts(normalize=True)


# Ascending
df.sort_values("Age")

# Descending
df.sort_values("Salary", ascending=False)




X = df.drop("Target", axis=1)

y = df["Target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# New feature

df["Salary_Per_Age"] = df["Salary"] / df["Age"]

# Age in days
df["Age_Days"] = df["Age"] * 365

# Bonus
df["Bonus"] = df["Salary"] * 0.10