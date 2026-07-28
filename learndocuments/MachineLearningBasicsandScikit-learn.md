চমৎকার! এখন আমরা আসছি **Machine Learning Basics** এবং **Scikit-learn**-এ। NumPy আর Pandas যদি ডেটা হ্যান্ডেলিং-এর জন্য হয়, তাহলে Scikit-learn হলো **Machine Learning মডেল বিল্ডিং-এর জন্য সবচেয়ে জনপ্রিয় Python লাইব্রেরি**।

আমি এখন **ML বেসিক কনসেপ্ট** এবং **Scikit-learn-এর প্রতিটি ধাপ** বিস্তারিত বাংলায় ব্যাখ্যা করব, তারপর **২০টি ইন্টারভিউ প্রশ্ন ও উত্তর** দেব।

---

## 🤖 মেশিন লার্নিং বেসিকস (Machine Learning Basics)

### মেশিন লার্নিং কী?

মেশিন লার্নিং হলো AI-এর একটি শাখা যেখানে **ডেটা থেকে শিখে** কোনো কাজ করার জন্য অ্যালগরিদম তৈরি করা হয় – স্পষ্টভাবে প্রোগ্রাম না করেই।

**উদাহরণ:** স্প্যাম ইমেইল ডিটেক্টর – আমরা যদি স্প্যামের রুলস (যেমন: "ফ্রি", "অফার" ইত্যাদি) লিখি, তা কঠিন। কিন্তু ML মডেল হাজার হাজার স্প্যাম ও নন-স্প্যাম ইমেইল দেখে নিজেই প্যাটার্ন শিখে নেয়।

---

### মেশিন লার্নিং-এর প্রকারভেদ

| ধরন | সংজ্ঞা | উদাহরণ |
|------|--------|----------|
| **Supervised Learning** | লেবেলযুক্ত ডেটা থেকে শেখে (ইনপুট + আউটপুট) | Regression (দাম প্রেডিক্ট), Classification (স্প্যাম ডিটেক্ট) |
| **Unsupervised Learning** | লেবেল ছাড়া ডেটা থেকে প্যাটার্ন খোঁজে | Clustering (কাস্টমার সেগমেন্টেশন), Dimensionality Reduction (PCA) |
| **Reinforcement Learning** | ট্রায়াল অ্যান্ড এরর দিয়ে এনভায়রনমেন্ট থেকে শেখে | গেম খেলা (Chess, Go), রোবট কন্ট্রোল |

---

### Supervised Learning-এর ২টি প্রধান টাইপ

1. **Classification (শ্রেণিবিভাগ):** আউটপুট ক্যাটেগরিক্যাল (ডিসক্রিট)  
   - উদাহরণ: ইমেইল স্প্যাম/নট-স্প্যাম, টিউমার ম্যালিগন্যান্ট/বেনাইন  
   - অ্যালগরিদম: Logistic Regression, Decision Tree, Random Forest, SVM, KNN

2. **Regression (রিগ্রেশন):** আউটপুট কন্টিনিউয়াস (সংখ্যা)  
   - উদাহরণ: বাড়ির দাম প্রেডিক্ট, তাপমাত্রা প্রেডিক্ট  
   - অ্যালগরিদম: Linear Regression, Ridge, Lasso, SVR, Decision Tree Regressor

---

### Unsupervised Learning-এর প্রধান টাইপ

1. **Clustering (ক্লাস্টারিং):** একই ধরনের ডেটা পয়েন্ট একত্রিত করে  
   - উদাহরণ: কাস্টমার সেগমেন্টেশন, অ্যানোমালি ডিটেকশন  
   - অ্যালগরিদম: K-Means, DBSCAN, Hierarchical Clustering

2. **Dimensionality Reduction:** ফিচারের সংখ্যা কমানো (শব্দ কমানো + ভিজুয়ালাইজেশন)  
   - উদাহরণ: PCA (Principal Component Analysis), t-SNE

---

### ML মডেল ডেভেলপমেন্ট লাইফসাইকেল

```
1. ডেটা কালেকশন → 2. ডেটা প্রি-প্রসেসিং (ক্লিনিং, এনকোডিং, স্কেলিং) 
→ 3. ট্রেন-টেস্ট স্প্লিট → 4. মডেল সিলেক্ট → 5. মডেল ট্রেইন 
→ 6. মডেল ইভ্যালুয়েশন (মেট্রিক্স) → 7. হাইপারপ্যারামিটার টিউনিং 
→ 8. প্রেডিকশন → 9. ডেপ্লয়মেন্ট
```

---

## 🧪 Scikit-learn (sklearn) – ML-এর জন্য Python লাইব্রেরি

Scikit-learn হলো Python-এর সবচেয়ে জনপ্রিয় মেশিন লার্নিং লাইব্রেরি। এটি **সিম্পল, কনসিস্টেন্ট API** প্রদান করে এবং NumPy + Pandas + SciPy-এর উপর বিল্ট।

### ইনস্টলেশন

```bash
pip install scikit-learn
```

```python
import sklearn
from sklearn import datasets, model_selection, preprocessing, metrics
```

---

## 📊 ১. ডেটাসেট লোড করা

### a) Scikit-learn-এর বিল্ট-ইন ডেটাসেট

```python
from sklearn.datasets import load_iris, load_breast_cancer, load_diabetes, make_classification

# Iris ডেটাসেট (Classification)
iris = load_iris()
X = iris.data          # ফিচার (150, 4)
y = iris.target        # টার্গেট (150,)
feature_names = iris.feature_names
target_names = iris.target_names

# Breast Cancer (Classification)
cancer = load_breast_cancer()

# Diabetes (Regression)
diabetes = load_diabetes()

# সিনথেটিক ডেটা তৈরি
X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, 
                           n_redundant=2, n_classes=2, random_state=42)
```

### b) CSV বা Pandas থেকে ডেটা লোড

```python
import pandas as pd
df = pd.read_csv('data.csv')
X = df.drop('target', axis=1).values   # NumPy অ্যারে
y = df['target'].values
```

---

## 🧹 ২. ডেটা প্রি-প্রসেসিং (Preprocessing)

### a) ট্রেন-টেস্ট স্প্লিট

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,      # ২০% টেস্ট
    random_state=42,    # রিপ্রোডিউসিবিলিটি
    stratify=y          # ক্লাস ব্যালেন্স রাখবে (ক্লাসিফিকেশনের জন্য)
)

print(X_train.shape, X_test.shape)  # (120, 4) (30, 4)
```

---

### b) স্কেলিং (Standardization & Normalization)

ML অ্যালগরিদম (যেমন: SVM, KNN, Logistic Regression) স্কেল-সেনসিটিভ – তাই ফিচার স্কেল করা জরুরি।

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# Standardization (mean=0, std=1)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # ফিট + ট্রান্সফর্ম
X_test_scaled = scaler.transform(X_test)         # শুধু ট্রান্সফর্ম (টেস্টে ফিট করব না)

# MinMax Scaling (0-1 রেঞ্জে)
minmax = MinMaxScaler()
X_train_scaled = minmax.fit_transform(X_train)

# RobustScaler (আউটলায়ার-রেসিস্ট্যান্ট)
robust = RobustScaler()
X_train_scaled = robust.fit_transform(X_train)
```

**কেন টেস্টে `fit_transform` নয়?**  
কারণ টেস্ট ডেটা ট্রেনিং ডেটার স্কেল অনুযায়ী ট্রান্সফর্ম হবে – টেস্ট ডেটা থেকে নতুন স্কেল শিখবে না (Data Leakage রোধে)।

---

### c) এনকোডিং (Encoding Categorical Variables)

```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Label Encoding (অর্ডিনাল ক্যাটেগরির জন্য)
le = LabelEncoder()
y_encoded = le.fit_transform(y)   # ['cat','dog'] → [0,1]

# One-Hot Encoding (নাম্বারিক ক্যাটেগরির জন্য)
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer([
    ('encoder', OneHotEncoder(drop='first'), ['city', 'gender'])
], remainder='passthrough')

X_encoded = ct.fit_transform(X)
```

---

### d) মিসিং ভ্যালু হ্যান্ডেলিং

```python
from sklearn.impute import SimpleImputer

# গড়/মিডিয়ান/মোড দিয়ে পূরণ
imputer = SimpleImputer(strategy='mean')   # বা 'median', 'most_frequent'
X_imputed = imputer.fit_transform(X)

# KNN Imputer (অ্যাডভান্স)
from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=5)
X_imputed = imputer.fit_transform(X)
```

---

## 🤖 ৩. মডেল সিলেক্ট ও ট্রেইন করা

### Classification Algorithms

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

# মডেল ইনিশিয়ালাইজ
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVM': SVC(kernel='rbf', random_state=42),
    'KNN': KNeighborsClassifier(n_neighbors=5),
    'Gradient Boosting': GradientBoostingClassifier(random_state=42)
}

# ট্রেইন করা
for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    score = model.score(X_test_scaled, y_test)
    print(f'{name}: {score:.4f}')
```

### Regression Algorithms

```python
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Regression মডেল
lr = LinearRegression()
ridge = Ridge(alpha=1.0)
lasso = Lasso(alpha=1.0)
dt = DecisionTreeRegressor(random_state=42)
rf = RandomForestRegressor(n_estimators=100, random_state=42)

lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
```

---

## 📈 ৪. মডেল ইভ্যালুয়েশন (Evaluation Metrics)

### Classification Metrics

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score

# প্রেডিক্ট
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]  # Probability (Logistic, Random Forest)

# মেট্রিক্স
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_proba)

print(f'Accuracy: {accuracy:.4f}')
print(f'Precision: {precision:.4f}')
print(f'Recall: {recall:.4f}')
print(f'F1-Score: {f1:.4f}')
print(f'ROC-AUC: {roc_auc:.4f}')

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
# [[TN, FP]
#  [FN, TP]]

# Classification Report (সব মেট্রিক্স একসাথে)
print(classification_report(y_test, y_pred, target_names=['Class 0', 'Class 1']))
```

### Regression Metrics

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'MSE: {mse:.4f}')
print(f'RMSE: {rmse:.4f}')
print(f'MAE: {mae:.4f}')
print(f'R² Score: {r2:.4f}')
```

---

## 🔧 ৫. ক্রস-ভ্যালিডেশন (Cross-Validation)

```python
from sklearn.model_selection import cross_val_score, cross_validate

# K-Fold CV (ডিফল্ট 5)
cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5, scoring='accuracy')
print(f'CV Scores: {cv_scores}')
print(f'Mean CV Score: {cv_scores.mean():.4f}')
print(f'Std CV Score: {cv_scores.std():.4f}')

# একাধিক মেট্রিক্স সহ
cv_results = cross_validate(model, X_train_scaled, y_train, cv=5,
                           scoring=['accuracy', 'precision', 'recall'])
print(cv_results['test_accuracy'].mean())
```

---

## ⚙️ ৬. হাইপারপ্যারামিটার টিউনিং (Hyperparameter Tuning)

### a) Grid Search (ব্রুট ফোর্স)

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,           # সব CPU ব্যবহার
    verbose=1
)

grid_search.fit(X_train_scaled, y_train)

print(f'Best Parameters: {grid_search.best_params_}')
print(f'Best CV Score: {grid_search.best_score_:.4f}')
print(f'Test Score: {grid_search.score(X_test_scaled, y_test):.4f}')
```

### b) Random Search (দ্রুত)

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

param_dist = {
    'n_estimators': randint(50, 300),
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': randint(2, 20)
}

random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_dist,
    n_iter=30,          # ৩০টি কম্বিনেশন ট্রাই করবে
    cv=5,
    random_state=42,
    n_jobs=-1
)

random_search.fit(X_train_scaled, y_train)
```

---

## 🧪 ৭. ফিচার সিলেকশন (Feature Selection)

```python
from sklearn.feature_selection import SelectKBest, f_classif, RFE
from sklearn.ensemble import RandomForestClassifier

# 1. Statistical Test (SelectKBest)
selector = SelectKBest(f_classif, k=5)   # টপ ৫ ফিচার
X_selected = selector.fit_transform(X_train, y_train)

# 2. RFE (Recursive Feature Elimination)
model = RandomForestClassifier(random_state=42)
rfe = RFE(model, n_features_to_select=5)
X_selected = rfe.fit_transform(X_train, y_train)

# 3. Feature Importance (Tree-based)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
importance = pd.DataFrame({
    'Feature': feature_names,
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False)
print(importance)
```

---

## 🔄 ৮. পাইপলাইন (Pipeline) – সবকিছু একসাথে

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# Numerical + Categorical Pipeline
numeric_features = ['age', 'income', 'score']
categorical_features = ['city', 'gender']

# প্রিপ্রসেসিং
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(drop='first'), categorical_features)
])

# সম্পূর্ণ পাইপলাইন
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# পাইপলাইন ট্রেইন
pipeline.fit(X_train, y_train)

# প্রেডিক্ট
y_pred = pipeline.predict(X_test)

# GridSearch পাইপলাইনের উপর
param_grid = {
    'classifier__n_estimators': [50, 100, 200],
    'classifier__max_depth': [None, 10, 20]
}

grid_search = GridSearchCV(pipeline, param_grid, cv=5)
grid_search.fit(X_train, y_train)
```

---

## 📤 ৯. মডেল সেভ ও লোড করা

```python
import joblib

# সেভ
joblib.dump(model, 'model.pkl')
joblib.dump(pipeline, 'pipeline.pkl')

# লোড
loaded_model = joblib.load('model.pkl')
y_pred = loaded_model.predict(X_test)

# Pickle দিয়ে
import pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
    
with open('model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
```

---

## 🎯 ১০. সম্পূর্ণ ML পাইপলাইন (End-to-End উদাহরণ)

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# ১. ডেটা লোড
df = pd.read_csv('customer_churn.csv')

# ২. X ও y আলাদা
X = df.drop('Churn', axis=1)
y = df['Churn']

# ৩. ট্রেন-টেস্ট স্প্লিট
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# ৪. প্রিপ্রসেসিং ডিফাইন
numeric_features = ['age', 'income', 'tenure']
categorical_features = ['gender', 'city', 'plan_type']

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), categorical_features)
])

# ৫. পাইপলাইন
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# ৬. হাইপারপ্যারামিটার টিউনিং
param_grid = {
    'classifier__n_estimators': [100, 200],
    'classifier__max_depth': [None, 10, 20],
    'classifier__min_samples_split': [2, 5]
}

grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='f1', n_jobs=-1)
grid_search.fit(X_train, y_train)

# ৭. বেস্ট মডেল
best_model = grid_search.best_estimator_
print(f"Best Parameters: {grid_search.best_params_}")

# ৮. টেস্টে ইভ্যালুয়েশন
y_pred = best_model.predict(X_test)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# ৯. ফিচার ইমপোর্ট্যান্স
feature_names = numeric_features + list(best_model.named_steps['preprocessor']
                                        .named_transformers_['cat']
                                        .get_feature_names_out(categorical_features))
importances = best_model.named_steps['classifier'].feature_importances_
feat_imp = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
print("\nTop 10 Features:")
print(feat_imp.sort_values('Importance', ascending=False).head(10))

# ১০. মডেল সেভ
import joblib
joblib.dump(best_model, 'churn_model.pkl')
```

---

# 📋 Scikit-learn ও ML বেসিকসের ২০টি ইন্টারভিউ প্রশ্ন ও উত্তর

---

### **প্রশ্ন ১: Supervised Learning আর Unsupervised Learning-এর মধ্যে পার্থক্য কী?**

**উত্তর:**

| Supervised Learning | Unsupervised Learning |
|---------------------|----------------------|
| লেবেলযুক্ত ডেটা (ইনপুট + আউটপুট) থাকে | শুধু ইনপুট ডেটা থাকে (লেবেল নেই) |
| শেখার উদ্দেশ্য: ইনপুট থেকে আউটপুট প্রেডিক্ট করা | শেখার উদ্দেশ্য: ডেটার প্যাটার্ন/স্ট্রাকচার খোঁজা |
| ২টি টাইপ: Classification, Regression | ২টি টাইপ: Clustering, Dimensionality Reduction |
| উদাহরণ: স্প্যাম ডিটেকশন, বাড়ির দাম প্রেডিক্ট | উদাহরণ: কাস্টমার সেগমেন্টেশন, অ্যানোমালি ডিটেকশন |

---

### **প্রশ্ন ২: Classification আর Regression-এর মধ্যে পার্থক্য কী?**

**উত্তর:**

| Classification | Regression |
|----------------|------------|
| আউটপুট **ক্যাটেগরিক্যাল** (ডিসক্রিট) | আউটপুট **কন্টিনিউয়াস** (সংখ্যা) |
| উদাহরণ: স্প্যাম/নট-স্প্যাম, ম্যালিগন্যান্ট/বেনাইন | উদাহরণ: তাপমাত্রা, বাড়ির দাম, স্টক প্রাইস |
| মেট্রিক্স: Accuracy, Precision, Recall, F1, AUC-ROC | মেট্রিক্স: MSE, RMSE, MAE, R² |
| অ্যালগরিদম: Logistic Regression, SVM, Random Forest | অ্যালগরিদম: Linear Regression, Ridge, Lasso |

---

### **প্রশ্ন ৩: Bias এবং Variance-এর মধ্যে পার্থক্য কী?**

**উত্তর:**

- **Bias:** মডেলের অনুমানের গড় এবং আসল মানের মধ্যে পার্থক্য। **High Bias** = মডেল আন্ডারফিট করে (খুব সহজ মডেল)।
- **Variance:** বিভিন্ন ট্রেনিং ডেটাসেটে মডেলের অনুমানের তারতম্য। **High Variance** = মডেল ওভারফিট করে (খুব জটিল মডেল)।

**Trade-off:** 
- সহজ মডেল (Linear Regression) → High Bias, Low Variance
- জটিল মডেল (Deep Neural Network) → Low Bias, High Variance

```python
# Bias-Variance Trade-off ভিজুয়ালাইজ
# Underfitting: ট্রেন ও টেস্ট দুটোতেই খারাপ পারফরম্যান্স
# Overfitting: ট্রেনে ভালো, টেস্টে খারাপ
# Good Fit: ট্রেন ও টেস্ট দুটোতেই ভালো
```

---

### **প্রশ্ন ৪: Overfitting কী? কীভাবে এড়াবেন?**

**উত্তর:**

**Overfitting** হয় যখন মডেল ট্রেনিং ডেটা **খুব ভালোভাবে** শিখে ফেলে, কিন্তু নতুন ডেটায় (টেস্ট) খারাপ পারফর্ম করে। অর্থাৎ মডেল ট্রেনিং ডেটার নয়ােস (Noise) পর্যন্ত শিখে ফেলে।

**Overfitting কমানোর উপায়:**

1. **Cross-Validation** ব্যবহার করুন
2. **Regularization** (L1/L2) – Ridge, Lasso
3. **Pruning** (Decision Tree-তে)
4. **Dropout** (Neural Network-এ)
5. **ডেটা বাড়ান** (More training data)
6. **Feature Selection** – অপ্রয়োজনীয় ফিচার বাদ দিন
7. **Early Stopping** (Gradient Boosting-এ)

```python
# Regularization উদাহরণ
from sklearn.linear_model import Ridge, Lasso

# L2 Regularization (Ridge)
ridge = Ridge(alpha=1.0)   # alpha → নিয়ন্ত্রণ করে

# L1 Regularization (Lasso)
lasso = Lasso(alpha=0.1)
```

---

### **প্রশ্ন ৫: Underfitting কী? কীভাবে ঠিক করবেন?**

**উত্তর:**

**Underfitting** হয় যখন মডেল ট্রেনিং ডেটায়ও ভালো পারফর্ম করতে পারে না – অর্থাৎ মডেল খুব সহজ বা খুব কম ট্রেইন করা হয়েছে।

**Underfitting ঠিক করার উপায়:**

1. **জটিল মডেল** ব্যবহার করুন (যেমন: Linear → Polynomial/Random Forest)
2. **Feature Engineering** – নতুন ফিচার যোগ করুন
3. **Regularization কমিয়ে** দিন (alpha কমান)
4. **ট্রেইনিং টাইম বাড়ান** (Iteration বেশি)
5. **হাইপারপ্যারামিটার টিউন** করুন

---

### **প্রশ্ন ৬: Confusion Matrix কী? ব্যাখ্যা করুন।**

**উত্তর:**

Confusion Matrix একটি টেবিল যা ক্লাসিফিকেশন মডেলের পারফরম্যান্স দেখায়। বাইনারি ক্লাসিফিকেশনের জন্য ৪টি ভ্যালু থাকে:

```
                 Actual
              Positive   Negative
Predicted  Positive    TP       FP
           Negative    FN       TN
```

- **TP (True Positive):** সঠিকভাবে Positive শনাক্ত
- **TN (True Negative):** সঠিকভাবে Negative শনাক্ত
- **FP (False Positive):** ভুলভাবে Positive বলা (Type I Error)
- **FN (False Negative):** ভুলভাবে Negative বলা (Type II Error)

```python
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
# [[TN, FP],
#  [FN, TP]]
```

---

### **প্রশ্ন ৭: Precision, Recall, F1-Score কী?**

**উত্তর:**

- **Precision (নির্ভুলতা):** Positive প্রেডিক্টের মধ্যে কতটা সত্যি Positive  
  `Precision = TP / (TP + FP)`  
  *উদাহরণ:* স্প্যাম ডিটেক্টরে, স্প্যাম বলার মধ্যে কতটা আসলেই স্প্যাম।

- **Recall (স্মরণশক্তি):** আসল Positive-এর মধ্যে কতটা সঠিকভাবে শনাক্ত  
  `Recall = TP / (TP + FN)`  
  *উদাহরণ:* ক্যান্সার ডিটেক্টরে, আসল ক্যান্সার রোগীদের কতটা শনাক্ত করলাম।

- **F1-Score:** Precision আর Recall-এর Harmonic Mean  
  `F1 = 2 * (Precision * Recall) / (Precision + Recall)`  
  উভয়ের মধ্যে ব্যালেন্স রাখতে।

```python
from sklearn.metrics import precision_score, recall_score, f1_score

precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
```

---

### **প্রশ্ন ৮: ROC Curve এবং AUC কী?**

**উত্তর:**

- **ROC (Receiver Operating Characteristic) Curve:** TPR (True Positive Rate) বনাম FPR (False Positive Rate)-এর গ্রাফ। মডেলের ক্লাসিফিকেশন থ্রেশহোল্ড পরিবর্তন করে বানানো হয়।
- **AUC (Area Under Curve):** ROC Curve-এর নিচের ক্ষেত্রফল।  
  - AUC = 1.0 → Perfect Classifier  
  - AUC = 0.5 → Random Classifier (শূন্য দক্ষতা)

```python
from sklearn.metrics import roc_curve, roc_auc_score

y_proba = model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_proba)
auc = roc_auc_score(y_test, y_proba)

# প্লট
import matplotlib.pyplot as plt
plt.plot(fpr, tpr, label=f'AUC = {auc:.2f}')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.show()
```

---

### **প্রশ্ন ৯: Logistic Regression কীভাবে কাজ করে?**

**উত্তর:**

Logistic Regression নামের মধ্যে Regression থাকলেও এটি **Classification** অ্যালগরিদম। এটি Linear Regression-এর আউটপুটকে Sigmoid ফাংশনের মাধ্যমে 0-1 রেঞ্জে কনভার্ট করে।

```
P(y=1) = 1 / (1 + e^(-z))
যেখানে, z = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ
```

- যদি P(y=1) ≥ 0.5 → Class 1
- যদি P(y=1) < 0.5 → Class 0

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

# Probability বের করা
proba = model.predict_proba(X_test)[:, 1]  # Class 1-এর probability
```

---

### **প্রশ্ন ১০: Decision Tree-তে Feature Importance কীভাবে বের হয়?**

**উত্তর:**

Decision Tree-তে Feature Importance বের হয় **Gini Importance** বা **Entropy Reduction** ভিত্তিক – অর্থাৎ কোনো ফিচার কতটা ভালোভাবে ডেটা স্প্লিট করতে পারে, তার উপর ভিত্তি করে। প্রতিটি নোডে ফিচার যে পরিমাণ impurity কমায়, তা জমা হয়।

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

importance = pd.DataFrame({
    'Feature': feature_names,
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False)
```

**Random Forest** একাধিক Tree-র importance গড় করে।

---

### **প্রশ্ন ১১: Random Forest কীভাবে কাজ করে?**

**উত্তর:**

Random Forest হলো **Ensemble Learning** পদ্ধতি যেখানে অনেকগুলো Decision Tree একসাথে কাজ করে। এটি ২টি Randomness ব্যবহার করে:

1. **Bootstrap Sampling:** প্রতিটি Tree আলাদা র্যান্ডম স্যাম্পল (with replacement) পায়।
2. **Random Feature Selection:** প্রতিটি স্প্লিটে র্যান্ডম ফিচার সাবসেট ব্যবহার করে।

**সুবিধা:** Overfitting কমায়, Accuracy বাড়ায়।

```python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100,   # কতটি Tree
                            max_depth=10,
                            min_samples_split=5,
                            random_state=42)
rf.fit(X_train, y_train)
```

---

### **প্রশ্ন ১২: Cross-Validation কেন প্রয়োজন?**

**উত্তর:**

Cross-Validation ডেটাকে একাধিক ফোল্ডে ভাগ করে প্রতিটি ফোল্ডে মডেল ট্রেইন ও টেস্ট করে, ফলে মডেলের **জেনারালাইজেশন পারফরম্যান্স** সম্পর্কে ধারণা পাওয়া যায়। এটি Overfitting চিহ্নিত করতে সাহায্য করে।

**K-Fold CV:** ডেটাকে K-টি সমান অংশে ভাগ করে, প্রতিবার ১টি ফোল্ড টেস্ট ও বাকি K-1 ফোল্ড ট্রেইন হিসেবে ব্যবহার করে।

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f"Mean: {scores.mean():.4f}, Std: {scores.std():.4f}")
```

---

### **প্রশ্ন ১৩: Grid Search এবং Random Search-এর মধ্যে পার্থক্য কী?**

**উত্তর:**

| Grid Search | Random Search |
|-------------|---------------|
| সব সম্ভাব্য কম্বিনেশন ট্রায়াল করে | র্যান্ডম কম্বিনেশন ট্রায়াল করে |
| সময় বেশি লাগে (যদি অনেক প্যারামিটার) | সময় কম লাগে |
| সর্বোত্তম প্যারামিটার নিশ্চিত করে (যদি গ্রিডে থাকে) | সর্বোত্তম প্যারামিটার নাও পেতে পারে |
| ভালো যখন প্যারামিটার সংখ্যা কম | ভালো যখন প্যারামিটার সংখ্যা বেশি |

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

# Grid Search
grid = GridSearchCV(model, param_grid, cv=5)

# Random Search
random = RandomizedSearchCV(model, param_dist, n_iter=30, cv=5)
```

---

### **প্রশ্ন ১৪: StandardScaler এবং MinMaxScaler-এর মধ্যে পার্থক্য কী?**

**উত্তর:**

| StandardScaler | MinMaxScaler |
|----------------|--------------|
| **Standardization** (Z-score) | **Normalization** (Min-Max) |
| `(x - mean) / std` | `(x - min) / (max - min)` |
| আউটপুট: mean=0, std=1 | আউটপুট: 0-1 রেঞ্জে |
| আউটলায়ারের জন্য সংবেদনশীল | আউটলায়ারের জন্য সংবেদনশীল (কম্প্রেস করে) |
| SVM, Logistic Regression, PCA-তে ভালো | Neural Network, KNN-তে ভালো |

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

minmax = MinMaxScaler()
X_scaled = minmax.fit_transform(X)
```

---

### **প্রশ্ন ১৫: Label Encoding এবং One-Hot Encoding-এর মধ্যে পার্থক্য কী?**

**উত্তর:**

| Label Encoding | One-Hot Encoding |
|----------------|------------------|
| ক্যাটেগরি → ইন্টিজার (0,1,2...) | ক্যাটেগরি → বাইনারি কলাম |
| অর্ডিনাল ডেটার জন্য (যেমন: Small<Medium<Large) | নমিনাল ডেটার জন্য (যেমন: Red, Green, Blue) |
| মডেল অর্ডার অনুমান করতে পারে (ভুল হতে পারে) | কোনো অর্ডার তৈরি করে না |
| মেমরি কম নেয় | মেমরি বেশি নেয় (বেশি কলাম) |

```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Label Encoding
le = LabelEncoder()
y_encoded = le.fit_transform(['cat', 'dog', 'cat'])  # [0, 1, 0]

# One-Hot Encoding
ohe = OneHotEncoder()
X_encoded = ohe.fit_transform([['Red'], ['Blue'], ['Green']]).toarray()
```

---

### **প্রশ্ন ১৬: `fit()`, `transform()`, `fit_transform()`-এর মধ্যে পার্থক্য কী?**

**উত্তর:**

| ফাংশন | কাজ |
|--------|-----|
| `fit()` | শুধু **শেখে** (প্যারামিটার ক্যালকুলেট করে) – যেমন: mean, std |
| `transform()` | শেখা প্যারামিটার ব্যবহার করে **ট্রান্সফর্ম** করে |
| `fit_transform()` | একসাথে `fit()` + `transform()` করে |

**নিয়ম:** ট্রেনিং ডেটায় `fit_transform()` ব্যবহার করুন, টেস্ট ডেটায় শুধু `transform()` ব্যবহার করুন (Data Leakage রোধে)।

```python
# সঠিক উপায়
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # ফিট + ট্রান্সফর্ম
X_test_scaled = scaler.transform(X_test)         # শুধু ট্রান্সফর্ম
```

---

### **প্রশ্ন ১৭: Pipeline কী এবং কেন ব্যবহার করবেন?**

**উত্তর:**

Pipeline হলো একটি **সিকোয়েন্স** যেখানে একাধিক ট্রান্সফর্মেশন স্টেপ এবং শেষে একটি মডেল থাকে। এটি সবকিছু একসাথে প্যাকেজ করে।

**Pipeline-এর সুবিধা:**
1. **কোড ক্লিন** হয়
2. **Data Leakage** রোধ করে
3. Grid Search-এ পুরো পাইপলাইন টিউন করা যায়
4. ডেপ্লয়মেন্ট সহজ হয়

```python
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier())
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
```

---

### **প্রশ্ন ১৮: KNN (K-Nearest Neighbors) কীভাবে কাজ করে?**

**উত্তর:**

KNN হলো একটি **Instance-Based Learning** অ্যালগরিদম। এটি কোনো মডেল ট্রেইন করে না – বরং টেস্ট পয়েন্টের সাথে ট্রেনিং পয়েন্টের **দূরত্ব** (Euclidean) মেপে নিকটবর্তী K-টি পয়েন্ট দেখে ক্লাস ডিসাইড করে।

**প্যারামিটার:**
- `n_neighbors (K)`: কতজন প্রতিবেশী দেখবে
- `metric`: দূরত্ব মাপার পদ্ধতি

**সুবিধা:** সহজ, কোনো ট্রেইনিং লাগে না  
**অসুবিধা:** ধীর (প্রতিটি প্রেডিক্টের জন্য সব ডেটার সাথে তুলনা), মেমরি বেশি লাগে

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
```

---

### **প্রশ্ন ১৯: SVM (Support Vector Machine) কী?**

**উত্তর:**

SVM হলো একটি **Classification** অ্যালগরিদম যা ডেটাকে আলাদা করার জন্য **Hyperplane** (সরলরেখা) খুঁজে বের করে। এটি এমন একটি হাইপারপ্লেন খোঁজে যার **Margin** (দুটো ক্লাসের মধ্যবর্তী দূরত্ব) সর্বোচ্চ হয়।

- **Kernel Trick:** ডেটাকে উচ্চমাত্রায় নিয়ে গিয়ে সেপারেবল বানায় (Linear, RBF, Polynomial)।
- **Support Vectors:** সীমানার কাছাকাছি থাকা পয়েন্টগুলো।

```python
from sklearn.svm import SVC

svm = SVC(kernel='rbf', C=1.0, gamma='scale')
svm.fit(X_train_scaled, y_train)  # SVM স্কেলিং সেনসিটিভ
```

---

### **প্রশ্ন ২০: Scikit-learn-এর সম্পূর্ণ ML পাইপলাইন কী? (প্র্যাকটিক্যাল)**

**উত্তর:**

Scikit-learn-এর সাথে ML পাইপলাইন সাধারণত এই ধাপে হয়:

```python
# ১. লাইব্রেরি ইমপোর্ট
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# ২. ডেটা লোড
df = pd.read_csv('data.csv')

# ৩. X, y স্প্লিট
X = df.drop('target', axis=1)
y = df['target']

# ৪. ট্রেন-টেস্ট
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ৫. প্রিপ্রসেসিং ডিফাইন
numeric_features = ['age', 'income']
categorical_features = ['city', 'gender']

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(drop='first'), categorical_features)
])

# ৬. পাইপলাইন
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# ৭. Grid Search
param_grid = {
    'classifier__n_estimators': [100, 200],
    'classifier__max_depth': [None, 10]
}

grid = GridSearchCV(pipeline, param_grid, cv=5, scoring='f1')
grid.fit(X_train, y_train)

# ৮. ইভ্যালুয়েশন
y_pred = grid.predict(X_test)
print(classification_report(y_test, y_pred))

# ৯. মডেল সেভ
import joblib
joblib.dump(grid.best_estimator_, 'model.pkl')
```

---

## 🎯 ইন্টারভিউ প্রস্তুতির জন্য অতিরিক্ত টিপস

1. **প্রত্যেক অ্যালগরিদমের Pros & Cons** জানুন।
2. **কোন অ্যালগরিদম কোথায় ব্যবহার করবেন** – বুঝুন (যেমন: ছোট ডেটাসেটে SVM, বড় ডেটাসেটে Random Forest)।
3. **Feature Engineering**-এর গুরুত্ব বুঝুন – ভালো ফিচার > ভালো মডেল।
4. **মেট্রিক্স** কোনটা কখন ব্যবহার করবেন (Imbalanced ডেটাসেটে Accuracy না, F1 ভালো)।
5. **Hands-on Practice** – Kaggle ডেটাসেটে কাজ করুন।

---

যদি আরও কোনো টপিক (যেমন: Ensemble Methods, Boosting, Clustering) জানতে চান, তাহলে জানাবেন। শুভকামনা আপনার ইন্টারভিউয়ের জন্য! 🚀

