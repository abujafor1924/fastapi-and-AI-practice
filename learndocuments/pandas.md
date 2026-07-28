চমৎকার! NumPy-এর পর এখন **Pandas** – যা ডেটা সায়েন্স এবং AI/ML-এর **আরেকটি অপরিহার্য লাইব্রেরি**। NumPy যেমন অ্যারে নিয়ে কাজ করে, Pandas তেমনই **টেবুলার ডেটা** (স্প্রেডশিট/CSV-এর মতো) নিয়ে কাজ করার জন্য তৈরি। 

আমি এখন Pandas-এর **প্রতিটি ধাপ বিস্তারিত বাংলায় ব্যাখ্যা করব**, তারপর **২০টি ইন্টারভিউ প্রশ্ন ও উত্তর** দেব।

---

## 🐼 Pandas কী এবং কেন AI/ML-এ গুরুত্বপূর্ণ?

**Pandas** হলো Python-এর একটি ওপেন সোর্স লাইব্রেরি যা **ডেটা ম্যানিপুলেশন** এবং **অ্যানালাইসিস**-এর জন্য ব্যবহৃত হয়। এটি দুটি প্রধান ডেটা স্ট্রাকচার প্রদান করে:

1. **Series** – 1D লেবেলযুক্ত অ্যারে (একটি কলামের মতো)
2. **DataFrame** – 2D টেবুলার স্ট্রাকচার (এক্সেল শীট বা SQL টেবিলের মতো)

**AI/ML-এ Pandas-এর ভূমিকা:**
- ডেটা ক্লিনিং (মিসিং ভ্যালু হ্যান্ডেলিং)
- ডেটা ট্রান্সফরমেশন (ফিল্টার, গ্রুপ, অ্যাগ্রিগেট)
- এক্সপ্লোরেটরি ডেটা অ্যানালাইসিস (EDA)
- ফিচার ইঞ্জিনিয়ারিং
- CSV/Excel/JSON/এমনকি SQL ডেটাবেজ থেকে ডেটা লোড করা
- ট্রেন-টেস্ট স্প্লিটের আগে ডেটা প্রস্তুত করা

---

## 📦 ইনস্টলেশন ও ইমপোর্ট

```bash
pip install pandas
```

```python
import pandas as pd
import numpy as np  # Pandas NumPy-এর উপর বিল্ট
```

---

## 📊 ১. Pandas ডেটা স্ট্রাকচার

### a) Series (1D)

```python
# List থেকে Series
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s)
# a    10
# b    20
# c    30
# d    40
# dtype: int64

# Dictionary থেকে Series
data = {'Math': 85, 'Physics': 90, 'Chemistry': 88}
s2 = pd.Series(data)
print(s2)
```

**Series-এর অ্যাট্রিবিউট:**
```python
print(s.values)   # [10 20 30 40]
print(s.index)    # Index(['a', 'b', 'c', 'd'], dtype='object')
print(s.dtype)    # int64
```

---

### b) DataFrame (2D)

```python
# Dictionary থেকে DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NYC', 'LA', 'Chicago']
}
df = pd.DataFrame(data)
print(df)
#       Name  Age     City
# 0    Alice   25      NYC
# 1      Bob   30       LA
# 2  Charlie   35  Chicago

# List of Lists থেকে
df2 = pd.DataFrame([[1, 'A'], [2, 'B']], columns=['ID', 'Grade'])
```

---

## 📥 ২. ডেটা ইমপোর্ট ও এক্সপোর্ট

```python
# CSV পড়া
df = pd.read_csv('data.csv')

# এক্সেল পড়া
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# JSON পড়া
df = pd.read_json('data.json')

# SQL (SQLAlchemy দরকার)
# df = pd.read_sql('SELECT * FROM table', connection)

# আউটপুট
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)
df.to_json('output.json')
```

---

## 👁️ ৩. ডেটা এক্সপ্লোরেশন (Exploring Data)

```python
# প্রথম ৫ রো
df.head()

# শেষ ৫ রো
df.tail()

# র‍্যান্ডম ৫ রো
df.sample(5)

# ডেটাফ্রেমের ইনফো
df.info()          # কলাম, নন-নাল কাউন্ট, ডেটা টাইপ

# পরিসংখ্যানিক সারাংশ
df.describe()      # শুধু নিউমেরিক কলামের জন্য

# কলামের নাম
df.columns

# ইনডেক্স
df.index

# শেপ (রো, কলাম)
df.shape           # (100, 5)

# মোট এলিমেন্ট
df.size
```

---

## 🔍 ৪. ডেটা সিলেকশন (Indexing & Slicing)

### a) কলাম সিলেক্ট করা

```python
# একটি কলাম (Series)
df['Name']
df.Name          # ডট নোটেশন (শুধু ভালো নামের জন্য)

# একাধিক কলাম (DataFrame)
df[['Name', 'Age']]
```

### b) রো সিলেক্ট করা

```python
# loc: লেবেল ভিত্তিক
df.loc[0]              # ১ম রো
df.loc[0:2]            # ০-২ রো (শেষ ইনক্লুসিভ)
df.loc[0:2, ['Name', 'Age']]  # নির্দিষ্ট রো + কলাম

# iloc: ইন্টিজার পজিশন ভিত্তিক
df.iloc[0]             # ১ম রো
df.iloc[0:3, 0:2]      # ০-২ রো, ০-১ কলাম
df.iloc[:, 0]          # সব রো, ১ম কলাম
```

### c) কন্ডিশনাল সিলেক্ট (Filtering)

```python
# Age > 30
df[df['Age'] > 30]

# একাধিক শর্ত
df[(df['Age'] > 25) & (df['City'] == 'NYC')]
df[(df['Age'] > 25) | (df['City'] == 'LA')]

# isin ব্যবহার
df[df['City'].isin(['NYC', 'LA'])]

# ~ (নট) অপারেটর
df[~df['City'].isin(['NYC', 'LA'])]
```

---

## ✏️ ৫. ডেটা ম্যানিপুলেশন

### a) নতুন কলাম যোগ করা

```python
df['Salary'] = [50000, 60000, 70000]
df['Age_in_days'] = df['Age'] * 365

# শর্ত ভিত্তিক কলাম
df['Senior'] = df['Age'] > 30
```

### b) কলাম ড্রপ করা

```python
df.drop('Salary', axis=1, inplace=True)   # কলাম ড্রপ
df.drop(0, axis=0, inplace=True)          # রো ড্রপ
```

### c) রিনেম করা

```python
df.rename(columns={'Name': 'Full_Name'}, inplace=True)
df.rename(index={0: 'First'}, inplace=True)
```

---

## 🧹 ৬. মিসিং ডেটা হ্যান্ডেলিং (Missing Data)

```python
# NaN চেক
df.isnull()           # বুলিয়ান ডেটাফ্রেম
df.isnull().sum()     # প্রতি কলামে NaN কাউন্ট

# NaN বাদ দেওয়া
df.dropna()           # যেকোনো NaN থাকা রো বাদ
df.dropna(axis=1)     # NaN থাকা কলাম বাদ
df.dropna(thresh=2)   # অন্তত ২টি নন-NaN থাকা রো রাখবে

# NaN পূরণ করা
df.fillna(0)                     # সব NaN-কে ০
df.fillna(df.mean())             # গড় দিয়ে পূরণ
df['Age'].fillna(df['Age'].median(), inplace=True)

# ফরোয়ার্ড/ব্যাকওয়ার্ড ফিল
df.fillna(method='ffill')        # উপরের মান দিয়ে
df.fillna(method='bfill')        # নিচের মান দিয়ে
```

---

## 📊 ৭. গ্রুপিং ও অ্যাগ্রিগেশন (GroupBy & Aggregation)

```python
# গ্রুপ করা
grouped = df.groupby('City')

# অ্যাগ্রিগেট
grouped['Age'].mean()           # প্রতি সিটিতে গড় বয়স
grouped['Age'].agg(['mean', 'max', 'min', 'count'])

# একাধিক কলামে আলাদা অ্যাগ্রিগেশন
df.groupby('City').agg({
    'Age': 'mean',
    'Salary': ['sum', 'max']
})

# transform (গ্রুপ ভিত্তিক মান যোগ করা)
df['City_Age_Mean'] = df.groupby('City')['Age'].transform('mean')
```

---

## 🔄 ৮. মার্জিং, জয়েনিং ও কনক্যাটেনেশন

```python
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['A', 'B', 'C']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Score': [90, 85, 88]})

# Merge (SQL-এর মতো JOIN)
merged = pd.merge(df1, df2, on='ID', how='inner')   # inner join
merged = pd.merge(df1, df2, on='ID', how='left')    # left join
merged = pd.merge(df1, df2, on='ID', how='outer')   # outer join

# Concatenate (ভার্টিক্যাল/হরাইজন্টাল)
pd.concat([df1, df2], axis=0)   # রো অনুযায়ী (স্ট্যাক)
pd.concat([df1, df2], axis=1)   # কলাম অনুযায়ী

# Join (ইনডেক্স ভিত্তিক)
df1.set_index('ID').join(df2.set_index('ID'), how='inner')
```

---

## 🛠️ ৯. অ্যাপ্লাই ফাংশন (Apply, Map, Applymap)

```python
# apply: কলাম বা রোতে ফাংশন প্রয়োগ
df['Age_Squared'] = df['Age'].apply(lambda x: x**2)

# map: সিরিজের প্রতিটি এলিমেন্টে
df['City_Code'] = df['City'].map({'NYC': 1, 'LA': 2, 'Chicago': 3})

# applymap: প্রতিটি এলিমেন্টে (পুরো ডেটাফ্রেম)
df[['Age', 'Salary']].applymap(lambda x: x * 1.1)

# vectorized অপারেশন (দ্রুততম)
df['Age'] = df['Age'] + 1
```

---

## 📈 ১০. পিভট টেবিল ও ক্রস-ট্যাব

```python
# Pivot Table (Excel-এর মতো)
pivot = df.pivot_table(
    values='Salary',
    index='City',           # রো
    columns='Department',   # কলাম
    aggfunc='mean',
    fill_value=0
)

# Crosstab (ফ্রিকোয়েন্সি টেবিল)
crosstab = pd.crosstab(df['City'], df['Department'])
```

---

## 🕒 ১১. টাইম সিরিজ ডেটা

```python
# ডেটটাইম কনভার্ট
df['Date'] = pd.to_datetime(df['Date'])

# ডেট রেঞ্জ তৈরি
dates = pd.date_range('2024-01-01', periods=100, freq='D')

# রিস্যাম্পলিং (ডাউনস্যাম্পল)
df.set_index('Date', inplace=True)
monthly = df.resample('M').mean()

# শিফট (ল্যাগ তৈরি)
df['Shifted'] = df['Value'].shift(1)

# রোলিং উইন্ডো
df['Rolling_Mean'] = df['Value'].rolling(window=7).mean()
```

---

## 💾 ১২. ডেটা টাইপ কনভার্সন

```python
# টাইপ চেক
df.dtypes

# কনভার্ট
df['Age'] = df['Age'].astype('int64')
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'])
df['Category'] = df['Category'].astype('category')  # ক্যাটেগরিক্যাল
```

---

## 🧹 ১৩. ডুপ্লিকেট হ্যান্ডেলিং

```python
# ডুপ্লিকেট চেক
df.duplicated()          # বুলিয়ান সিরিজ
df.duplicated().sum()    # কতটি ডুপ্লিকেট

# ডুপ্লিকেট বাদ
df.drop_duplicates()                    # সব কলাম দেখে
df.drop_duplicates(subset=['Name'])     # শুধু 'Name' কলাম দেখে
df.drop_duplicates(keep='first')        # প্রথমটি রাখবে
df.drop_duplicates(keep='last')         # শেষটি রাখবে
```

---

## 📊 ১৪. করিলেশন ও কভারিয়েন্স

```python
# করিলেশন ম্যাট্রিক্স
corr = df.corr()          # শুধু নিউমেরিক কলাম

# ভিজুয়ালাইজেশন (Seaborn দরকার)
import seaborn as sns
sns.heatmap(corr, annot=True)

# কভারিয়েন্স
cov = df.cov()
```

---

## 🚀 ১৫. পারফরম্যান্স টিপস

```python
# ১. Vectorized অপারেশন ব্যবহার করুন (apply-এর চেয়ে দ্রুত)
df['Age'] = df['Age'] * 2   # ভালো
df['Age'] = df['Age'].apply(lambda x: x*2)  # ধীর

# ২. query() ব্যবহার করুন (বড় ডেটার জন্য)
df.query('Age > 30 and City == "NYC"')

# ৩. eval() ব্যবহার করুন (এক্সপ্রেশন ইভালুয়েট)
df.eval('New = Age * 365 + Salary')

# ৪. Memory optimization
df['Age'] = df['Age'].astype('int8')  # মেমরি কমাতে
df['City'] = df['City'].astype('category')  # ক্যাটেগরি টাইপ

# ৫. Chunking (বড় ফাইলের জন্য)
chunks = pd.read_csv('huge.csv', chunksize=10000)
for chunk in chunks:
    process(chunk)
```

---

## 🧠 AI/ML পাইপলাইনে Pandas-এর ব্যবহার

```python
# ১. ডেটা লোড
df = pd.read_csv('dataset.csv')

# ২. EDA (এক্সপ্লোর)
df.info()
df.describe()
df.isnull().sum()

# ৩. ক্লিনিং
df.dropna(inplace=True)
df['Feature'] = df['Feature'].astype('float32')

# ৪. ফিচার ইঞ্জিনিয়ারিং
df['New_Feature'] = df['Feature1'] / df['Feature2']
df['Category'] = df['Category'].astype('category').cat.codes  # এনকোডিং

# ৫. ট্রেন-টেস্ট স্প্লিট
from sklearn.model_selection import train_test_split
X = df.drop('Target', axis=1)
y = df['Target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# ৬. নরমালাইজেশন
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ৭. মডেল ট্রেইন
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train_scaled, y_train)
```

---

# 📋 Pandas-এর ২০টি ইন্টারভিউ প্রশ্ন ও উত্তর

---

### **প্রশ্ন ১: Pandas কি? Series এবং DataFrame-এর মধ্যে পার্থক্য কী?**

**উত্তর:**  
Pandas হলো Python-এর ডেটা ম্যানিপুলেশন লাইব্রেরি।  

| **Series** | **DataFrame** |
|------------|---------------|
| 1D লেবেলযুক্ত অ্যারে | 2D টেবুলার স্ট্রাকচার (এক্সেল শীটের মতো) |
| একটি মাত্র কলাম | একাধিক কলাম (প্রতিটি কলাম Series) |
| ইনডেক্স + ভ্যালু | ইনডেক্স + কলাম + ভ্যালু |

```python
s = pd.Series([1,2,3])          # Series
df = pd.DataFrame({'A': [1,2], 'B': [3,4]})  # DataFrame
```

---

### **প্রশ্ন ২: Pandas-এ ডেটা লোড করার বিভিন্ন উপায় কী কী?**

**উত্তর:**  

```python
# CSV
df = pd.read_csv('file.csv')

# Excel
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')

# JSON
df = pd.read_json('file.json')

# SQL
import sqlite3
conn = sqlite3.connect('db.db')
df = pd.read_sql('SELECT * FROM table', conn)

# Clipboard (এক্সেল থেকে কপি করে)
df = pd.read_clipboard()

# Dictionary থেকে
df = pd.DataFrame({'A': [1,2], 'B': [3,4]})

# List of Dicts থেকে
df = pd.DataFrame([{'A': 1, 'B': 3}, {'A': 2, 'B': 4}])
```

---

### **প্রশ্ন ৩: `loc` এবং `iloc`-এর মধ্যে পার্থক্য কী?**

**উত্তর:**  

| `loc` | `iloc` |
|-------|--------|
| **লেবেল** (ইনডেক্স/কলামের নাম) ভিত্তিক সিলেক্ট করে | **পজিশন** (ইন্টিজার) ভিত্তিক সিলেক্ট করে |
| শেষ ইন্ডেক্স **ইনক্লুসিভ** | শেষ ইন্ডেক্স **এক্সক্লুসিভ** |
| শর্ত বা বুলিয়ান অ্যারে ব্যবহার করা যায় | শুধু ইন্টিজার স্লাইস/ইন্ডেক্স |

```python
df = pd.DataFrame({'A': [1,2,3], 'B': [4,5,6]}, index=['x','y','z'])

df.loc['y']          # ২য় রো (লেবেল y)
df.iloc[1]           # ২য় রো (পজিশন 1)

df.loc['x':'y', 'A'] # x-y রো, A কলাম (y ইনক্লুসিভ)
df.iloc[0:2, 0]      # ০-১ রো, ০ কলাম (২ এক্সক্লুসিভ)
```

---

### **প্রশ্ন ৪: কীভাবে ডেটাফ্রেম থেকে ডুপ্লিকেট রো বাদ দেবেন?**

**উত্তর:**  

```python
# সব কলাম দেখে ডুপ্লিকেট বাদ
df.drop_duplicates()

# নির্দিষ্ট কলাম দেখে
df.drop_duplicates(subset=['Name', 'Age'])

# কোনটি রাখবে (first/default, last)
df.drop_duplicates(keep='first')   # প্রথমটি রাখে
df.drop_duplicates(keep='last')    # শেষটি রাখে

# ডুপ্লিকেট চেক
df.duplicated().sum()  # কতটি ডুপ্লিকেট
```

---

### **প্রশ্ন ৫: Pandas-এ মিসিং ভ্যালু (NaN) হ্যান্ডেল করার উপায় কী?**

**উত্তর:**  

```python
# NaN চেক
df.isnull().sum()          # প্রতি কলামে NaN কাউন্ট
df['col'].isnull()         # বুলিয়ান সিরিজ

# বাদ দেওয়া
df.dropna()                # যেকোনো NaN থাকা রো বাদ
df.dropna(axis=1)          # NaN থাকা কলাম বাদ
df.dropna(thresh=2)        # ২টির কম নন-NaN থাকা রো বাদ

# পূরণ করা
df.fillna(0)               # সব NaN-কে ০
df.fillna(df.mean())       # গড় দিয়ে পূরণ
df['col'].fillna(method='ffill', inplace=True)  # উপরের মান দিয়ে

# ইন্টারপোলেশন
df['col'].interpolate()    # লিনিয়ার ইন্টারপোলেশন
```

---

### **প্রশ্ন ৬: `groupby()` কীভাবে কাজ করে? উদাহরণ দিন।**

**উত্তর:**  
`groupby()` ডেটাকে নির্দিষ্ট কলামের ভ্যালু অনুযায়ী গ্রুপ করে, তারপর প্রতিটি গ্রুপে অ্যাগ্রিগেট ফাংশন প্রয়োগ করে।

```python
# গ্রুপ তৈরি
grouped = df.groupby('City')

# অ্যাগ্রিগেশন
grouped['Age'].mean()           # প্রতি সিটিতে গড় বয়স
grouped['Salary'].agg(['sum', 'max', 'min'])

# একাধিক কলামের জন্য আলাদা অ্যাগ্রিগেশন
df.groupby('City').agg({
    'Age': 'mean',
    'Salary': ['sum', 'count']
})

# transform (গ্রুপ ভিত্তিক মান যোগ)
df['City_Avg_Salary'] = df.groupby('City')['Salary'].transform('mean')

# filter (গ্রুপ ফিল্টার)
df.groupby('City').filter(lambda x: len(x) > 5)  # ৫+ রো থাকা গ্রুপ
```

---

### **প্রশ্ন ৭: `merge()`, `join()`, `concat()`-এর মধ্যে পার্থক্য কী?**

**উত্তর:**  

| `merge()` | `join()` | `concat()` |
|-----------|----------|------------|
| SQL-এর JOIN-এর মতো (কলামের ভ্যালু ম্যাচ করে) | ইনডেক্স ভিত্তিক জয়েন | শুধু স্ট্যাক/পাশাপাশি যোগ করে |
| `on` প্যারামিটার দিয়ে ম্যাচিং কলাম বলা যায় | ডিফল্টভাবে ইনডেক্স ম্যাচ করে | `axis=0` (রো) বা `axis=1` (কলাম) |
| `how` দিয়ে inner/left/outer/right | `how` দিয়ে inner/left/outer | কোনো ম্যাচিং কন্ডিশন নেই |

```python
# Merge
pd.merge(df1, df2, on='ID', how='inner')

# Join (ইনডেক্স সেট করে)
df1.set_index('ID').join(df2.set_index('ID'), how='inner')

# Concat
pd.concat([df1, df2], axis=0)   # রো স্ট্যাক
pd.concat([df1, df2], axis=1)   # কলাম স্ট্যাক
```

---

### **প্রশ্ন ৮: `apply()`, `map()`, `applymap()`-এর মধ্যে পার্থক্য কী?**

**উত্তর:**  

| ফাংশন | কাজ | ব্যবহার |
|--------|-----|---------|
| `apply()` | DataFrame-এর **কলাম বা রো**-তে ফাংশন প্রয়োগ করে | `df['col'].apply(lambda x: x*2)` |
| `map()` | **Series**-এর প্রতিটি এলিমেন্টে ফাংশন প্রয়োগ করে | `df['col'].map({'A':1, 'B':2})` (ম্যাপিং) |
| `applymap()` | DataFrame-এর **প্রতিটি এলিমেন্টে** ফাংশন প্রয়োগ করে | `df.applymap(lambda x: x*1.1)` |

```python
# apply: কলামে
df['Age_Sq'] = df['Age'].apply(lambda x: x**2)

# map: সিরিজে (ডিকশনারি ম্যাপিং)
df['Gender_Code'] = df['Gender'].map({'Male': 1, 'Female': 0})

# applymap: পুরো ডেটাফ্রেমে
df[['Age', 'Salary']].applymap(lambda x: round(x, 2))
```

---

### **প্রশ্ন ৯: Pandas-এ কীভাবে Pivot Table তৈরি করবেন?**

**উত্তর:**  

```python
# Pivot Table
pivot = df.pivot_table(
    values='Sales',          # যে ভ্যালু অ্যাগ্রিগেট করব
    index='Region',          # রোতে যা বসবে
    columns='Product',       # কলামে যা বসবে
    aggfunc='sum',           # অ্যাগ্রিগেশন ফাংশন
    fill_value=0,            # NaN-এর জায়গায় ০
    margins=True             # টোটাল যোগ করবে
)

# Crosstab (ফ্রিকোয়েন্সি)
pd.crosstab(df['Region'], df['Product'], margins=True)
```

---

### **প্রশ্ন ১০: ডেটাফ্রেমের ডেটা টাইপ কীভাবে চেক ও পরিবর্তন করবেন?**

**উত্তর:**  

```python
# চেক
df.dtypes                     # সব কলামের টাইপ
df['col'].dtype              # নির্দিষ্ট কলামের

# পরিবর্তন
df['Age'] = df['Age'].astype('int64')
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'])
df['Category'] = df['Category'].astype('category')

# মেমরি সেভ করতে
df['Age'] = df['Age'].astype('int8')   # ৮-বিট ইন্টিজার
df['Gender'] = df['Gender'].astype('category')  # ক্যাটেগরি টাইপ
```

---

### **প্রশ্ন ১১: কীভাবে ডেটাফ্রেমকে শর্ত অনুযায়ী ফিল্টার করবেন?**

**উত্তর:**  

```python
# একক শর্ত
df[df['Age'] > 30]

# একাধিক শর্ত (AND)
df[(df['Age'] > 25) & (df['City'] == 'NYC')]

# একাধিক শর্ত (OR)
df[(df['Age'] > 30) | (df['Salary'] > 50000)]

# isin()
df[df['City'].isin(['NYC', 'LA', 'Chicago'])]

# ~ (নট)
df[~df['City'].isin(['NYC', 'LA'])]

# query() (দ্রুত)
df.query('Age > 30 and City == "NYC"')

# str methods (টেক্সট ফিল্টার)
df[df['Name'].str.startswith('A')]
df[df['Email'].str.contains('@gmail')]
```

---

### **প্রশ্ন ১২: Pandas-এ টাইম সিরিজ ডেটা কীভাবে হ্যান্ডেল করবেন?**

**উত্তর:**  

```python
# ডেটটাইম কনভার্ট
df['Date'] = pd.to_datetime(df['Date'])

# ডেট সেট করা ইনডেক্স
df.set_index('Date', inplace=True)

# রিস্যাম্পলিং
df.resample('M').mean()      # মাসিক গড়
df.resample('W').sum()       # সাপ্তাহিক যোগ
df.resample('D').ffill()     # ডেইলি ফরোয়ার্ড ফিল

# শিফট (ল্যাগ)
df['Previous'] = df['Value'].shift(1)
df['Next'] = df['Value'].shift(-1)

# রোলিং উইন্ডো
df['MA_7'] = df['Value'].rolling(window=7).mean()

# ডেট রেঞ্জ তৈরি
dates = pd.date_range(start='2024-01-01', periods=100, freq='D')
```

---

### **প্রশ্ন ১৩: `value_counts()` এবং `unique()`-এর মধ্যে পার্থক্য কী?**

**উত্তর:**  

| `unique()` | `value_counts()` |
|------------|------------------|
| ইউনিক ভ্যালুগুলোর **অ্যারে** রিটার্ন করে | প্রতিটি ইউনিক ভ্যালুর **কাউন্ট** সহ Series রিটার্ন করে |
| কেবল ইউনিক মান দেখায় | ফ্রিকোয়েন্সি সহ দেখায় |
| সর্ট করা থাকে না | ডিফল্টভাবে কাউন্ট অনুযায়ী সর্টেড |

```python
df['City'].unique()
# array(['NYC', 'LA', 'Chicago'], dtype=object)

df['City'].value_counts()
# NYC       50
# LA        30
# Chicago   20
# Name: City, dtype: int64

# নরমালাইজড (পার্সেন্টেজ)
df['City'].value_counts(normalize=True)
```

---

### **প্রশ্ন ১৪: Pandas-এ কীভাবে করিলেশন ম্যাট্রিক্স বের করবেন?**

**উত্তর:**  

```python
# করিলেশন ম্যাট্রিক্স (শুধু নিউমেরিক কলাম)
corr = df.corr()

# নির্দিষ্ট কলামের সাথে করিলেশন
df.corr()['Target'].sort_values(ascending=False)

# স্পিয়ারম্যান করিলেশন (নন-লিনিয়ার)
df.corr(method='spearman')

# কভারিয়েন্স
cov = df.cov()

# ভিজুয়ালাইজেশন
import seaborn as sns
sns.heatmap(corr, annot=True, cmap='coolwarm')
```

---

### **প্রশ্ন ১৫: `melt()` এবং `pivot()` কী করে?**

**উত্তর:**  
এগুলো ডেটাফ্রেমের **শেপ পরিবর্তন** (reshape) করে।

- **`melt()`**: Wide format → Long format (আনপিভট)  
- **`pivot()`**: Long format → Wide format (পিভট)

```python
# Wide data
df_wide = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Math': [85, 90],
    'Science': [88, 92]
})

# Melt (Long format)
df_long = df_wide.melt(id_vars=['Name'], 
                       value_vars=['Math', 'Science'],
                       var_name='Subject',
                       value_name='Score')

# Pivot (আবার Wide)
df_pivot = df_long.pivot(index='Name', columns='Subject', values='Score')
```

---

### **প্রশ্ন ১৬: কীভাবে ডেটাফ্রেমকে এলোমেলো করে শাফল করবেন?**

**উত্তর:**  

```python
# ১. sample() দিয়ে (ভালো উপায়)
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

# ২. shuffle() (স্কিটলার্ন থেকে)
from sklearn.utils import shuffle
df_shuffled = shuffle(df, random_state=42)

# ৩. numpy পার্মিউটেশন
df_shuffled = df.iloc[np.random.permutation(len(df))].reset_index(drop=True)
```

**AI-তে ব্যবহার:** ট্রেন-টেস্ট স্প্লিটের আগে ডেটা শাফল করা জরুরি।

---

### **প্রশ্ন ১৭: Pandas-এ `Categorical` ডেটা টাইপ কেন ব্যবহার করবেন?**

**উত্তর:**  
`Categorical` টাইপ ব্যবহার করলে:
- **মেমোরি কম লাগে** (ইন্টিজার কোডিং)
- **পারফরম্যান্স ভালো হয়** (গ্রুপবাই, সর্টে)
- **অর্ডার** সংরক্ষণ করা যায়

```python
# কনভার্ট
df['City'] = df['City'].astype('category')

# অর্ডার সেট করা
df['Size'] = pd.Categorical(df['Size'], 
                            categories=['S', 'M', 'L'], 
                            ordered=True)

# ক্যাটেগরি কোড বের করা
df['City_Codes'] = df['City'].cat.codes

# এক্সপ্লোর
df['City'].cat.categories
df['City'].cat.ordered
```

---

### **প্রশ্ন ১৮: Memory Optimization-এর জন্য Pandas-এ কী করবেন?**

**উত্তর:**  

```python
# ১. ডেটা টাইপ ডাউনকাস্ট
df['Age'] = df['Age'].astype('int8')       # int64 → int8
df['Salary'] = df['Salary'].astype('float32')  # float64 → float32

# ২. ক্যাটেগরি টাইপ ব্যবহার
df['City'] = df['City'].astype('category')

# ৩. অবজেক্ট টাইপ → স্ট্রিং
df['Name'] = df['Name'].astype('string')

# ৪. বড় ফাইলের জন্য chunksize
chunks = pd.read_csv('huge.csv', chunksize=10000)
for chunk in chunks:
    process(chunk)

# ৫. মেমোরি ইউসেজ চেক
df.info(memory_usage='deep')

# ৬. অপ্রয়োজনীয় কলাম ড্রপ
df.drop(columns=['Unnamed: 0'], inplace=True)
```

---

### **প্রশ্ন ১৯: ডেটাফ্রেমে কীভাবে ট্রেন-টেস্ট স্প্লিট করবেন?**

**উত্তর:**  

```python
# ১. Scikit-learn ব্যবহার (সেরা)
from sklearn.model_selection import train_test_split

X = df.drop('Target', axis=1)
y = df['Target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=42,
    stratify=y  # ক্লাস ইমব্যালেন্স থাকলে
)

# ২. শাফল + স্লাইস (ম্যানুয়াল)
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)
split_idx = int(0.8 * len(df_shuffled))
train = df_shuffled[:split_idx]
test = df_shuffled[split_idx:]

# ৩. Time Series-এর জন্য
train = df[:'2023-12-31']
test = df['2024-01-01':]
```

---

### **প্রশ্ন ২০: AI/ML পাইপলাইনে Pandas কীভাবে ব্যবহার করবেন? (সম্পূর্ণ উদাহরণ)**

**উত্তর:**  

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ১. ডেটা লোড
df = pd.read_csv('customer_data.csv')

# ২. EDA
print(df.info())
print(df.describe())
print(df.isnull().sum())

# ৩. ডেটা ক্লিনিং
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# ৪. ফিচার ইঞ্জিনিয়ারিং
df['Age_Group'] = pd.cut(df['Age'], bins=[0,25,50,100], labels=['Young','Middle','Senior'])
df['Income_per_Age'] = df['Income'] / df['Age']

# ৫. এনকোডিং (ক্যাটেগরিকাল)
le = LabelEncoder()
df['Gender_Code'] = le.fit_transform(df['Gender'])
df['City_Code'] = df['City'].astype('category').cat.codes

# ৬. ফিচার ও টার্গেট আলাদা
X = df.drop(['Target', 'Name', 'Gender', 'City', 'Age_Group'], axis=1)
y = df['Target']

# ৭. ট্রেন-টেস্ট স্প্লিট
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ৮. স্কেলিং
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ৯. মডেল ট্রেইন
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# ১০. প্রেডিক্ট ও ইভ্যালুয়েট
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.4f}')

# ১১. ফিচার ইমপোর্ট্যান্স
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False)
print(feature_importance)
```

---

## 🎯 Pandas ইন্টারভিউ প্রস্তুতির টিপস

1. **হাতে-কলমে প্র্যাকটিস করুন** – প্রতিটি ফাংশন নিজে রান করে দেখুন।
2. **বাস্তব ডেটাসেট** (যেমন: Titanic, Iris, House Prices) নিয়ে কাজ করুন।
3. **`loc`/`iloc`**, **`groupby`**, **`merge`** – এই তিনটি টপিক সবচেয়ে বেশি জিজ্ঞেস করা হয়।
4. **পারফরম্যান্স** সম্পর্কে ধারণা রাখুন – ভেক্টরাইজেশন, মেমোরি অপটিমাইজেশন।
5. **Pandas + NumPy + Scikit-learn** – এই তিনটি একসাথে কীভাবে কাজ করে, তার পুরো পাইপলাইন বুঝুন।

---

যদি আরও কোনো টপিক (যেমন: MultiIndex, Window Functions, বা Time Series-এর অ্যাডভান্স) জানতে চান, তাহলে জানাবেন। শুভকামনা আপনার ইন্টারভিউয়ের জন্য! 🚀

