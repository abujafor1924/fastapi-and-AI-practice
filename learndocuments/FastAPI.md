# FastAPI ইন্টারভিউ প্রশ্নসমূহ - বাংলা ব্যাখ্যা

---

## 🟢 Basic Level (1–15)

### 1. What is FastAPI?
**উত্তর:** FastAPI হল Python-এর একটি আধুনিক, দ্রুতগতির (high-performance) ওয়েব ফ্রেমওয়ার্ক যা RESTful APIs তৈরির জন্য ব্যবহৃত হয়। এটি Python 3.6+ এর টাইপ হিন্টিং (type hints) এর উপর ভিত্তি করে তৈরি এবং স্বয়ংক্রিয়ভাবে API ডকুমেন্টেশন তৈরি করে।

**বাংলা ব্যাখ্যা:** FastAPI হলো একটি Python লাইব্রেরি যা দিয়ে আমরা ওয়েব API বানাই। যেমন: একটি মোবাইল অ্যাপ বা ওয়েবসাইটের জন্য backend সার্ভিস তৈরি করা। এটি খুব দ্রুত কাজ করে এবং কোড লেখার সময় আমরা যদি টাইপ উল্লেখ করি (যেমন: `name: str`), তাহলে FastAPI স্বয়ংক্রিয়ভাবে ডেটা ভ্যালিডেশন ও ডকুমেন্টেশন তৈরি করে দেয়।

---

### 2. Why would you choose FastAPI over Django REST Framework?
**উত্তর:**
- **Performance:** FastAPI অনেক দ্রুত (ASGI-based)
- **Lightweight:** ডিজাইনে হালকা
- **Automatic Documentation:** Swagger UI ও ReDoc স্বয়ংক্রিয়
- **Type Hints:** Python type hints ব্যবহার করে
- **Async Support:** `async/await` সম্পূর্ণ সাপোর্ট
- **Less Boilerplate:** কম কোডে বেশি কাজ

**বাংলা ব্যাখ্যা:** Django REST Framework খুব শক্তিশালী কিন্তু ভারী। FastAPI হালকা, দ্রুত, এবং আধুনিক। যদি আপনার প্রোজেক্টে দ্রুত API তৈরি করতে হয়, মাইক্রোসার্ভিস আর্কিটেকচার ব্যবহার করতে হয়, অথবা machine learning মডেল deploy করতে হয় - FastAPI ভালো পছন্দ। Django উপযোগী বড়, মনোলিথিক অ্যাপ্লিকেশনের জন্য।

---

### 3. What are the main features of FastAPI?
**উত্তর:**
1. **High Performance:** NodeJS এবং Go এর সমান দ্রুত
2. **Fast Development:** ডেভেলপমেন্ট স্পিড ২-৩ গুণ বেশি
3. **Automatic Docs:** Swagger UI (`/docs`) এবং ReDoc (`/redoc`)
4. **Data Validation:** Pydantic ব্যবহার করে স্বয়ংক্রিয় ভ্যালিডেশন
5. **Async Support:** `async/await` সাপোর্ট
6. **Dependency Injection:** `Depends()` ব্যবহার করে
7. **Type Safety:** Python type hints সম্পূর্ণ সাপোর্ট
8. **Security:** OAuth2, JWT ইত্যাদি বিল্ট-ইন

**বাংলা ব্যাখ্যা:** FastAPI-এর সবচেয়ে বড় ফিচারগুলো হলো - এটি খুব দ্রুত (Benchmark এ NodeJS-এর সমান), স্বয়ংক্রিয় ডকুমেন্টেশন তৈরি করে, এবং টাইপ হিন্টিং ব্যবহার করে ডেটা ভ্যালিডেশন করে। এছাড়া async সাপোর্ট থাকায় অনেক রিকোয়েস্ট একসাথে হ্যান্ডেল করতে পারে।

---

### 4. FastAPI is built on which libraries?
**উত্তর:**
- **Starlette:** ওয়েব অংশ (রাউটিং, মিডলওয়্যার, রিকোয়েস্ট/রেসপন্স)
- **Pydantic:** ডেটা ভ্যালিডেশন এবং সিরিয়ালাইজেশন
- **Uvicorn:** ASGI সার্ভার (রান করার জন্য)

**বাংলা ব্যাখ্যা:** FastAPI আসলে দুইটি শক্তিশালী লাইব্রেরির সমন্বয়:
- **Starlette** কাজ করে রাউটিং, request/response handle করার মতো ওয়েব অংশে
- **Pydantic** কাজ করে ডেটা ভ্যালিডেশন এবং conversion-এ
- **Uvicorn** হলো সার্ভার যা আমাদের API run করে

---

### 5. What is ASGI?
**উত্তর:** ASGI (Asynchronous Server Gateway Interface) হল Python-এর জন্য একটি স্পেসিফিকেশন যা asynchronous ওয়েব সার্ভার এবং অ্যাপ্লিকেশনের মধ্যে ইন্টারফেস সংজ্ঞায়িত করে। এটি WSGI-এর উত্তরসূরি।

**বাংলা ব্যাখ্যা:** ASGI হলো একটি স্ট্যান্ডার্ড যা asynchronous (একইসাথে একাধিক কাজ) ওয়েব অ্যাপ্লিকেশন তৈরির জন্য। এর মাধ্যমে একটি সার্ভার একইসাথে অনেকগুলো request হ্যান্ডেল করতে পারে। যেমন: একটি রিকোয়েস্ট প্রসেস করার সময় অন্যটি waiting এ থাকে না।

---

### 6. Difference between ASGI and WSGI?
**উত্তর:**

| ASGI | WSGI |
|------|------|
| Asynchronous | Synchronous |
| একসাথে মাল্টিপল রিকোয়েস্ট হ্যান্ডেল করতে পারে | একসাথে একটি রিকোয়েস্ট হ্যান্ডেল করে |
| WebSocket সাপোর্ট করে | WebSocket সাপোর্ট করে না |
| আধুনিক অ্যাপ্লিকেশনের জন্য | লিগ্যাসি অ্যাপ্লিকেশনের জন্য |
| FastAPI, Django 3.0+ | Django, Flask (পুরনো) |

**বাংলা ব্যাখ্যা:** WSGI পুরনো টেকনোলজি যা একটি সময়ে একটি রিকোয়েস্ট প্রসেস করে। ASGI আধুনিক, যা অনেকগুলো রিকোয়েস্ট একসাথে হ্যান্ডেল করতে পারে। যেমন: আপনার অ্যাপে ১০০ জন ইউজার একসাথে request করলে ASGI সবগুলো হ্যান্ডেল করতে পারে, WSGI ধীরে ধীরে করবে।

---

### 7. What is Uvicorn?
**উত্তর:** Uvicorn হল একটি lightning-fast ASGI সার্ভার যা FastAPI অ্যাপ্লিকেশন চালানোর জন্য ব্যবহৃত হয়। এটি `uvloop` এবং `httptools` ব্যবহার করে উচ্চ পারফরম্যান্স প্রদান করে।

**বাংলা ব্যাখ্যা:** Uvicorn হলো সেই সার্ভার যা আমাদের FastAPI কোডকে রান করে এবং ব্রাউজার বা অ্যাপ থেকে আসা request গুলো গ্রহণ করে। যেমন: আপনি যদি `uvicorn main:app --reload` কমান্ড দেন, তাহলে Uvicorn আপনার FastAPI অ্যাপ চালু করে এবং লোকালহোস্টে доступ করে দেয়।

---

### 8. Why do we use Pydantic?
**উত্তর:** Pydantic ব্যবহার করি ডেটা ভ্যালিডেশন, সিরিয়ালাইজেশন এবং ডিসিরিয়ালাইজেশনের জন্য। এটি Python type hints ব্যবহার করে ডেটার টাইপ চেক করে এবং ভুল ডেটা এলে ক্লিয়ার এরর মেসেজ দেয়।

**বাংলা ব্যাখ্যা:** Pydantic হলো ডেটা চেক করার টুল। ধরুন আপনি একটি API বানিয়েছেন যেখানে ইউজারের নাম এবং ইমেইল লাগবে। Pydantic চেক করবে যে নাম স্ট্রিং কিনা, ইমেইল ফরম্যাট সঠিক কিনা। যদি ভুল ডেটা আসে, তাহলে সুন্দর এরর মেসেজ দেখাবে।

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int
```

---

### 9. What is request validation?
**উত্তর:** Request validation হল ক্লায়েন্ট (যেমন: ফ্রন্টএন্ড অ্যাপ) থেকে আসা ডেটা চেক করার প্রক্রিয়া যে ডেটা সঠিক ফরম্যাটে আছে কিনা। FastAPI Pydantic ব্যবহার করে স্বয়ংক্রিয়ভাবে এটি করে।

**বাংলা ব্যাখ্যা:** যখন কেউ আপনার API-তে ডেটা পাঠায় (POST request), তখন সেটা চেক করা হয় যে ডেটা ঠিক আছে কিনা। যেমন: যদি বলা হয় `age: int` পাঠাবে, কিন্তু কেউ `"twenty"` পাঠায় - তাহলে FastAPI এরর দেখাবে। এটাই request validation।

---

### 10. What is response validation?
**উত্তর:** Response validation হল সার্ভার থেকে ক্লায়েন্টে পাঠানো ডেটা চেক করা যে সেটা সঠিক ফরম্যাটে আছে কিনা। এটা নিশ্চিত করে যে API সবসময় প্রত্যাশিত ডেটা টাইপে রেসপন্স দিচ্ছে।

**বাংলা ব্যাখ্যা:** যখন আপনার API ডেটা রিটার্ন করে, তখন সেটাও ভ্যালিডেট করা হয়। যেমন: আপনার API যদি বলে `User` মডেল রিটার্ন করবে, কিন্তু আপনি ভুলবশত ডিফারেন্ট ডেটা রিটার্ন করেন - FastAPI এরর দেখাবে। এটা ভালো প্র্যাকটিস কারণ ক্লায়েন্ট জানে কি ধরনের ডেটা পাবে।

---

### 11. Explain type hints in FastAPI.
**উত্তর:** Type hints হল Python-এ ভেরিয়েবল, ফাংশন প্যারামিটার এবং রিটার্ন ভ্যালুর ডেটা টাইপ নির্ধারণ করার উপায়। FastAPI এগুলি ব্যবহার করে স্বয়ংক্রিয় ভ্যালিডেশন, ডকুমেন্টেশন এবং এডিটর সাপোর্ট প্রদান করে।

**বাংলা ব্যাখ্যা:** Type hints মানে হচ্ছে আপনি কোডে বলে দিচ্ছেন কোন ডেটা কোন টাইপের। যেমন:

```python
def get_user(user_id: int) -> dict:
    return {"id": user_id, "name": "John"}
```

এখানে `user_id: int` বলছে user_id সংখ্যা হবে, আর `-> dict` বলছে ফাংশনটি dictionary রিটার্ন করবে। FastAPI এটা ব্যবহার করে ডেটা চেক করে এবং ডকুমেন্টেশন বানায়।

---

### 12. What is automatic API documentation?
**উত্তর:** Automatic API documentation মানে FastAPI আপনার কোড বিশ্লেষণ করে নিজেই API ডকুমেন্টেশন তৈরি করে দেয়। এটি `/docs` (Swagger UI) এবং `/redoc` (ReDoc) এন্ডপয়েন্টে পাওয়া যায়।

**বাংলা ব্যাখ্যা:** আপনি যখন FastAPI তে API বানান, তখন আপনাকে আলাদা করে ডকুমেন্টেশন লিখতে হয় না। FastAPI আপনার কোড দেখেই সব এন্ডপয়েন্ট, প্যারামিটার, রিকোয়েস্ট বডি, রেসপন্স সবকিছুর ডকুমেন্টেশন তৈরি করে দেয়। ব্রাউজারে `/docs` দিয়ে দেখতে পারেন।

---

### 13. Difference between `/docs` and `/redoc`?
**উত্তর:**

| `/docs` (Swagger UI) | `/redoc` (ReDoc) |
|----------------------|------------------|
| Interactive UI | Static documentation |
| API টেস্ট করা যায় | শুধু পড়ার জন্য |
| JavaScript-based | Clean, minimal design |
| ব্রাউজারে সরাসরি টেস্ট | প্রিন্ট/PDF করতে ভালো |

**বাংলা ব্যাখ্যা:** `/docs` এ আপনি API টেস্ট করতে পারেন - ইনপুট দিয়ে দেখতে পারেন আউটপুট কি আসে। `/redoc` শুধু ডকুমেন্টেশন দেখায়, টেস্ট করা যায় না। ReDoc দেখতে বেশি প্রফেশনাল এবং ডকুমেন্টেশন প্রিন্ট করার জন্য ভালো।

---

### 14. What are path parameters?
**উত্তর:** Path parameters হল URL-এর অংশ যা ডাইনামিক ভ্যালু গ্রহণ করে। যেমন: `/users/{user_id}` - এখানে `user_id` একটি path parameter।

**বাংলা ব্যাখ্যা:** Path parameter মানে URL এর ভেতরে ডাইনামিক ডেটা নেওয়া। যেমন:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

যদি কেউ `/users/5` এ request করে, তাহলে `user_id=5` হবে।

---

### 15. What are query parameters?
**উত্তর:** Query parameters হল URL-এর `?` চিহ্নের পরে থাকা প্যারামিটার। যেমন: `/users?limit=10&page=2` - এখানে `limit` এবং `page` query parameters।

**বাংলা ব্যাখ্যা:** Query parameter ব্যবহার করা হয় ফিল্টার, সার্চ, পেজিনেশন ইত্যাদির জন্য। URL এর শেষে `?` দিয়ে শুরু হয় এবং `&` দিয়ে একাধিক প্যারামিটার যোগ করা যায়।

```python
@app.get("/users")
def get_users(limit: int = 10, page: int = 1):
    return {"limit": limit, "page": page}
```

---

## 🟡 Junior Level (16–30)

### 16. Difference between Path Parameter and Query Parameter?

**উত্তর:**

| Path Parameter | Query Parameter |
|----------------|-----------------|
| URL-এর অংশ (mandatory) | URL-এর শেষে (optional) |
| `/users/{user_id}` | `/users?limit=10` |
| সাধারণত ID বা unique identifier | ফিল্টার, পেজিনেশন, সার্চ |
| অবশ্যই দিতে হবে | অপশনাল, ডিফল্ট ভ্যালু দেওয়া যায় |

**বাংলা ব্যাখ্যা:** Path parameter হলো URL এর অংশ যা ছাড়া রিকোয়েস্ট কাজ করে না (যেমন: ইউজার আইডি)। Query parameter ঐচ্ছিক, যেমন: কতটি রেজাল্ট দেখাবে সেটা। Path parameter দিয়ে রিসোর্স শনাক্ত করা হয়, query parameter দিয়ে রিসোর্স ফিল্টার করা হয়।

---

### 17. How do you create a POST API?

**উত্তর:** POST API তৈরি করতে `@app.post()` ডেকোরেটর ব্যবহার করা হয় এবং Pydantic মডেল দিয়ে request body ডিফাইন করা হয়।

**বাংলা ব্যাখ্যা:** POST API দিয়ে নতুন ডেটা তৈরি করা হয়। যেমন: নতুন ইউজার তৈরি করা।

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str

@app.post("/users/")
def create_user(user: UserCreate):
    return {"message": f"User {user.name} created"}
```

---

### 18. Difference between GET and POST?

**উত্তর:**

| GET | POST |
|-----|------|
| ডেটা পড়ার জন্য (Read) | ডেটা তৈরি/সাবমিট করার জন্য (Create) |
| URL-এ ডেটা দৃশ্যমান | বডিতে ডেটা থাকে (লুকানো) |
| ক্যাশ করা যায় | ক্যাশ করা যায় না |
| সাইজ লিমিটেশন আছে | বড় ডেটা পাঠানো যায় |
| Idempotent (বারবার কল করলেও একই) | Non-idempotent |

**বাংলা ব্যাখ্যা:** GET ব্যবহার করা হয় ডেটা দেখার জন্য (যেমন: ইউজার লিস্ট দেখা), আর POST ব্যবহার করা হয় নতুন ডেটা তৈরি বা সাবমিট করার জন্য (যেমন: ফর্ম সাবমিট করা)। GET-এ ডেটা URL-এ দেখায়, POST-এ বডিতে থাকে।

---

### 19. Difference between PUT and PATCH?

**উত্তর:**

| PUT | PATCH |
|-----|-------|
| সম্পূর্ণ রিসোর্স আপডেট করে | আংশিক আপডেট করে |
| সব ফিল্ড দিতে হবে | শুধু পরিবর্তন করা ফিল্ড দিতে হয় |
| Idempotent | Idempotent নাও হতে পারে |
| `/users/1` | `/users/1` |

**বাংলা ব্যাখ্যা:** PUT ব্যবহার করলে আপনাকে ইউজারের সব ডেটা দিতে হবে (নাম, ইমেইল, এজ সব)। PATCH ব্যবহার করলে শুধু যে ফিল্ড পরিবর্তন করবেন সেটাই দিতে পারেন। যেমন: শুধু নাম পরিবর্তন করতে চাইলে শুধু নাম দিলেই হবে।

---

### 20. Difference between PUT and DELETE?

**উত্তর:**

| PUT | DELETE |
|-----|--------|
| রিসোর্স আপডেট/ক্রিয়েট করে | রিসোর্স ডিলিট করে |
| ডেটা পাঠাতে হয় | ডেটা পাঠাতে হয় না |
| Idempotent | Idempotent |

**বাংলা ব্যাখ্যা:** PUT দিয়ে ডেটা আপডেট করা হয়, DELETE দিয়ে ডেটা মুছে ফেলা হয়। DELETE সাধারণত শুধু রিসোর্সের আইডি পাঠায়, কোনো বডি থাকে না।

---

### 21. What is a Request Body?

**উত্তর:** Request body হল ক্লায়েন্ট থেকে সার্ভারে POST, PUT, PATCH রিকোয়েস্টের সাথে পাঠানো ডেটা। এটি সাধারণত JSON ফরম্যাটে থাকে।

**বাংলা ব্যাখ্যা:** যখন আপনি কোনো ডেটা সার্ভারে পাঠান (যেমন: নতুন ইউজার তৈরি), সেই ডেটাকে request body বলে। এটি রিকোয়েস্টের বডি অংশে যায়, URL-এ নয়।

```python
@app.post("/users")
def create_user(user: User):  # 'user' হলো request body
    return user
```

---

### 22. How do you create a Pydantic model?

**উত্তর:** Pydantic মডেল তৈরি করতে `BaseModel` থেকে ইনহেরিট করে ক্লাস ডিফাইন করতে হয় এবং ফিল্ডগুলোর টাইপ হিন্ট দিতে হয়।

**বাংলা ব্যাখ্যা:** Pydantic মডেল হলো একটি ক্লাস যা ডেটার স্ট্রাকচার ডিফাইন করে। 

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int = 18  # ডিফল্ট ভ্যালু
```

---

### 23. Difference between BaseModel and SQLAlchemy Model?

**উত্তর:**

| BaseModel (Pydantic) | SQLAlchemy Model |
|---------------------|------------------|
| ডেটা ভ্যালিডেশনের জন্য | ডেটাবেস টেবিলের জন্য |
| API request/response এর জন্য | Database ORM এর জন্য |
| JSON conversion করে | SQL conversion করে |
| ডেটাবেসের সাথে সম্পর্কিত নয় | ডেটাবেস টেবিল ম্যাপ করে |

**বাংলা ব্যাখ্যা:** Pydantic BaseModel ব্যবহার করা হয় API তে ডেটা আসা-যাওয়ার সময় ভ্যালিডেট করার জন্য। SQLAlchemy Model ব্যবহার করা হয় ডেটাবেসের টেবিলের সাথে Python কোডের সম্পর্ক স্থাপনের জন্য। একটি ডেটাবেস টেবিলের জন্য, আর একটি API ডেটার জন্য।

---

### 24. How do you return custom status codes?

**উত্তর:** FastAPI তে `status_code` প্যারামিটার দিয়ে কাস্টম স্ট্যাটাস কোড রিটার্ন করা যায়। `fastapi.status` থেকে কোড ব্যবহার করা ভালো।

**বাংলা ব্যাখ্যা:** HTTP স্ট্যাটাস কোড দিয়ে বোঝানো হয় রিকোয়েস্টের অবস্থা। ২০০=OK, ২০১=Created, ৪০৪=Not Found ইত্যাদি।

```python
from fastapi import FastAPI, status

@app.post("/users/", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    return user
```

---

### 25. What is HTTPException?

**উত্তর:** HTTPException হল FastAPI-এর একটি ক্লাস যা HTTP এরর রেসপন্স রিটার্ন করে। এটি ব্যবহার করলে স্ট্যাটাস কোড এবং ডিটেইল মেসেজ সহ এরর রিটার্ন করা যায়।

**বাংলা ব্যাখ্যা:** যখন কোনো এরর হয় (যেমন: ইউজার পাওয়া যায়নি), তখন HTTPException ব্যবহার করে সুন্দর এরর মেসেজ দেখানো যায়।

```python
from fastapi import HTTPException

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id > 100:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id}
```

---

### 26. How do you handle errors?

**উত্তর:** FastAPI তে এরর হ্যান্ডেল করার প্রধান উপায়:
1. `HTTPException` ব্যবহার করা
2. `@app.exception_handler()` ডেকোরেটর দিয়ে কাস্টম exception handler তৈরি করা
3. `try-except` ব্লক ব্যবহার করা

**বাংলা ব্যাখ্যা:** এরর হ্যান্ডেল মানে অপ্রত্যাশিত সমস্যা হলে সেটা সুন্দরভাবে হ্যান্ডেল করা। যেমন: ডেটাবেস কানেকশন ফেল করলে, ইউজার না পাওয়া গেলে ইত্যাদি।

```python
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )
```

---

### 27. What are response models?

**উত্তর:** Response models হল Pydantic মডেল যা API রেসপন্সের স্ট্রাকচার ডিফাইন করে। `response_model` প্যারামিটার দিয়ে সেট করা হয়।

**বাংলা ব্যাখ্যা:** Response model দিয়ে আপনি নিশ্চিত করেন যে আপনার API কেমন ডেটা রিটার্ন করবে। এটি ডেটা ফিল্টার, ভ্যালিডেশন এবং ডকুমেন্টেশনে সাহায্য করে।

```python
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    return {"name": "John", "email": "john@email.com", "password": "secret"}
# password রিটার্ন হবে না কারণ User মডেলে password নেই
```

---

### 28. Why should response models be used?

**উত্তর:**
1. **Data Filtering:** সংবেদনশীল ডেটা (যেমন: পাসওয়ার্ড) বাদ দেওয়া
2. **Validation:** রেসপন্স ডেটা ভ্যালিডেট করা
3. **Documentation:** স্বয়ংক্রিয় ডকুমেন্টেশন তৈরি
4. **Type Safety:** রিটার্ন ডেটার টাইপ নিশ্চিত করা
5. **Consistency:** API রেসপন্স কনসিস্টেন্ট রাখা

**বাংলা ব্যাখ্যা:** Response model ব্যবহার করলে আপনি নিশ্চিত করতে পারেন যে ইউজারের পাসওয়ার্ড বা অন্যান্য সিক্রেট ডেটা রিটার্ন হচ্ছে না। এছাড়া ডকুমেন্টেশনেও সেটা দেখায় এবং ক্লায়েন্ট জানে কি ডেটা পাবে।

---

### 29. What is dependency injection in FastAPI?

**উত্তর:** Dependency Injection (DI) হল একটি ডিজাইন প্যাটার্ন যেখানে কোনো ফাংশনের প্রয়োজনীয় ডিপেন্ডেন্সি (নির্ভরশীলতা) বাইরে থেকে সরবরাহ করা হয়। FastAPI তে `Depends()` ব্যবহার করে এটি করা হয়।

**বাংলা ব্যাখ্যা:** Dependency Injection মানে হলো আপনি যখন কোনো ফাংশন লিখেন, তার জন্য প্রয়োজনীয় জিনিসগুলো (যেমন: ডেটাবেস সেশন, অথেনটিকেশন) ফাংশনের ভেতরে তৈরি না করে বাইরে থেকে দিয়ে দেওয়া। এতে কোড পরিষ্কার এবং টেস্ট করা সহজ হয়।

---

### 30. What is `Depends()`?

**উত্তর:** `Depends()` হল FastAPI-এর একটি ফাংশন যা dependency injection এর জন্য ব্যবহৃত হয়। এটি একটি callable (ফাংশন, ক্লাস ইত্যাদি) নেয় এবং সেটির রিটার্ন ভ্যালু ইনজেক্ট করে।

**বাংলা ব্যাখ্যা:** `Depends()` হলো FastAPI-এর বিশেষ টুল যা কোনো ফাংশনের প্রয়োজনীয় জিনিস সরবরাহ করে। যেমন: ডেটাবেস সেশন, ইউজার অথেনটিকেশন চেক করা ইত্যাদি।

```python
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
```

---

## 🟠 Database Level (31–40)

### 31. How do you connect FastAPI with SQLAlchemy?

**উত্তর:** SQLAlchemy কানেক্ট করতে:
1. ডেটাবেস URL ডিফাইন করতে হবে
2. `create_engine()` দিয়ে engine তৈরি করতে হবে
3. `sessionmaker()` দিয়ে session তৈরি করতে হবে
4. Base ক্লাস তৈরি করতে হবে
5. মডেল ডিফাইন করতে হবে

**বাংলা ব্যাখ্যা:** SQLAlchemy হলো Python-এর ORM টুল যা ডেটাবেসের সাথে কাজ করতে সাহায্য করে। FastAPI তে এটি সংযোগ করার জন্য database.py ফাইল তৈরি করা হয়।

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://user:pass@localhost/db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

---

### 32. What is SessionLocal?

**উত্তর:** SessionLocal হল SQLAlchemy-এর একটি session তৈরি করার ফ্যাক্টরি। এটি ডেটাবেসের সাথে যোগাযোগের জন্য ব্যবহার করা হয়। প্রতিটি রিকোয়েস্টের জন্য নতুন session তৈরি করা হয়।

**বাংলা ব্যাখ্যা:** SessionLocal হলো এমন একটি ফাংশন যা কল করলে ডেটাবেসের সাথে সংযোগ তৈরি হয়। আপনি যখন ডেটাবেসে কিছু করতে চান (query, insert, update), তখন এই session ব্যবহার করেন।

```python
db = SessionLocal()  # নতুন session তৈরি
users = db.query(User).all()  # ডেটাবেস থেকে ডেটা নেওয়া
db.close()  # কাজ শেষে বন্ধ করা
```

---

### 33. Why do we create a database session?

**উত্তর:** ডেটাবেস সেশন তৈরি করা হয়:
1. ডেটাবেস ট্রানজেকশন ম্যানেজ করার জন্য
2. ডেটাবেস অপারেশনগুলো গ্রুপ করার জন্য
3. রিসোর্স ম্যানেজমেন্টের জন্য (সংযোগ বন্ধ করা)
4. প্রতিটি রিকোয়েস্ট আলাদা session পায় (thread-safe)

**বাংলা ব্যাখ্যা:** Session হলো ডেটাবেসের সাথে কাজ করার একটি "কাজের জায়গা"। আপনি যখন ডেটাবেসে কিছু করবেন, সেই কাজগুলো session এর মাধ্যমে হবে। প্রতিটি রিকোয়েস্টের জন্য আলাদা session তৈরি করা ভালো অভ্যাস যাতে একটি রিকোয়েস্ট অন্যটিকে প্রভাবিত না করে।

---

### 34. Difference between Engine and Session?

**উত্তর:**

| Engine | Session |
|--------|---------|
| ডেটাবেসের সাথে কানেকশন পুল ম্যানেজ করে | ডেটাবেস অপারেশন এক্সিকিউট করে |
| পুরো অ্যাপ্লিকেশনে একবার তৈরি হয় | প্রতিটি রিকোয়েস্টে নতুন তৈরি হয় |
| দীর্ঘজীবী (long-lived) | স্বল্পজীবী (short-lived) |
| `create_engine()` দিয়ে তৈরি | `sessionmaker()` দিয়ে তৈরি |

**বাংলা ব্যাখ্যা:** Engine হচ্ছে ডেটাবেসের সাথে সংযোগের "মূল" যা সার্ভার চালু থাকা পর্যন্ত থাকে। Session হলো সেই সংযোগ ব্যবহার করে কাজ করার "টুল" যা প্রতিটি রিকোয়েস্টের জন্য আলাদা করে তৈরি করা হয় এবং কাজ শেষে বন্ধ করে দেওয়া হয়।

---

### 35. What is ORM?

**উত্তর:** ORM (Object-Relational Mapping) হল একটি টেকনিক যা ডেটাবেস টেবিলকে Python ক্লাস এবং রেকর্ডকে অবজেক্ট হিসেবে ম্যাপ করে। SQLAlchemy Python-এর জনপ্রিয় ORM।

**বাংলা ব্যাখ্যা:** ORM মানে হলো আপনি SQL কোয়েরি না লিখে Python ক্লাস এবং অবজেক্ট ব্যবহার করে ডেটাবেস নিয়ে কাজ করতে পারেন। যেমন: `User` নামে একটি Python ক্লাস থাকলে, সেটি ডেটাবেসের `users` টেবিলকে বোঝায়।

```python
# SQL ছাড়াই Python কোডে ডেটাবেস অপারেশন
user = User(name="John", email="john@email.com")
db.add(user)
db.commit()  # SQL automatically তৈরি হয়
```

---

### 36. How do you create a model in SQLAlchemy?

**উত্তর:** SQLAlchemy মডেল তৈরি করতে:
1. `Base` ক্লাস থেকে ইনহেরিট করতে হবে
2. `__tablename__` দিয়ে টেবিলের নাম দিতে হবে
3. `Column` দিয়ে প্রতিটি ফিল্ড ডিফাইন করতে হবে

**বাংলা ব্যাখ্যা:** SQLAlchemy তে মডেল হলো Python ক্লাস যা ডেটাবেস টেবিলের সাথে সম্পর্কিত।

```python
from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(100), unique=True)
```

---

### 37. How do you perform CRUD operations?

**উত্তর:** CRUD অপারেশনগুলো:

**Create (তৈরি):**
```python
db.add(user)
db.commit()
db.refresh(user)
```

**Read (পড়া):**
```python
db.query(User).filter(User.id == 1).first()
db.query(User).all()
```

**Update (আপডেট):**
```python
user = db.query(User).filter(User.id == 1).first()
user.name = "New Name"
db.commit()
```

**Delete (মুছে ফেলা):**
```python
user = db.query(User).filter(User.id == 1).first()
db.delete(user)
db.commit()
```

**বাংলা ব্যাখ্যা:** CRUD মানে Create, Read, Update, Delete - ডেটাবেসের চারটি মৌলিক অপারেশন। SQLAlchemy দিয়ে এই কাজগুলো খুব সহজে Python কোডে করা যায়।

---

### 38. Difference between `add()`, `commit()`, and `refresh()`?

**উত্তর:**

| Method | কাজ |
|--------|-----|
| `add()` | নতুন ডেটা session-এ যোগ করে (কিন্তু ডেটাবেসে এখনো সেভ হয়নি) |
| `commit()` | session-এর সব পরিবর্তন ডেটাবেসে সেভ করে (permanent) |
| `refresh()` | ডেটাবেস থেকে最新 ডেটা অবজেক্টে রিলোড করে |

**বাংলা ব্যাখ্যা:** 
- `add()`: ডেটা তৈরি করার জন্য প্রস্তুত করে
- `commit()`: ডেটাবেসে সত্যিই সেভ করে
- `refresh()`: ডেটাবেস থেকে নতুন ডেটা এনে অবজেক্ট আপডেট করে (যেমন: auto-generated ID পেতে)

```python
user = User(name="John")
db.add(user)      # প্রস্তুত
db.commit()       # ডেটাবেসে সেভ
db.refresh(user)  # ID সহ最新 ডেটা পেতে
print(user.id)    # এখন ID পাওয়া যাবে
```

---

### 39. What happens if you don't call `commit()`?

**উত্তর:** যদি `commit()` না করা হয়:
- ডেটাবেসে কোনো পরিবর্তন সেভ হয় না
- পরিবর্তনগুলো শুধু memory (session) এ থাকে
- `db.close()` বা session শেষ হলে পরিবর্তনগুলো হারিয়ে যায়
- Rollback করা যায় (যেমন: এরর হলে)

**বাংলা ব্যাখ্যা:** `commit()` না করলে আপনার করা সব পরিবর্তন (add, update, delete) ডেটাবেসে যায় না। এগুলো শুধু session-এ থাকে। কাজ শেষে যদি `commit()` করেন, তাহলে ডেটাবেসে সেভ হয়। এরর হলে `rollback()` করতে পারেন।

---

### 40. What is Alembic?

**উত্তর:** Alembic হল SQLAlchemy-এর জন্য একটি ডেটাবেস মাইগ্রেশন টুল। এটি ডেটাবেস স্কিমা পরিবর্তন (টেবিল যোগ, পরিবর্তন, মুছে ফেলা) ট্র্যাক এবং ম্যানেজ করতে সাহায্য করে।

**বাংলা ব্যাখ্যা:** যখন আপনি আপনার অ্যাপ আপডেট করেন এবং ডেটাবেসে নতুন টেবিল বা কলাম যোগ করেন, Alembic সাহায্য করে সেই পরিবর্তনগুলো properly ম্যানেজ করতে। এটি version control এর মতো ডেটাবেসের জন্য।

```bash
alembic init migrations  # মাইগ্রেশন সেটআপ
alembic revision --autogenerate -m "add user table"  # পরিবর্তন ডিটেক্ট
alembic upgrade head  # ডেটাবেস আপডেট
```

---

## 🔵 Authentication & Security (41–45)

### 41. How does JWT authentication work?

**উত্তর:** JWT (JSON Web Token) অথেনটিকেশন কাজ করে:
1. ইউজার লগইন করে (username/password)
2. সার্ভার JWT টোকেন তৈরি করে (সাইন করা)
3. ক্লায়েন্ট টোকেন সংরক্ষণ করে
4. প্রতিটি রিকোয়েস্টে টোকেন পাঠায় (Authorization header)
5. সার্ভার টোকেন ভেরিফাই করে

**বাংলা ব্যাখ্যা:** JWT হলো একটি এনকোডেড টোকেন যাতে ইউজারের তথ্য থাকে। ইউজার লগইন করলে সার্ভার এই টোকেন তৈরি করে দেয়। এরপর ইউজার যখন কোনো API কল করে, এই টোকেন পাঠায়। সার্ভার টোকেন চেক করে বুঝে যে ইউজার অথেনটিকেটেড কিনা।

```python
# JWT টোকেন তৈরি
token = jwt.encode({"user_id": 1, "exp": datetime.utcnow() + timedelta(hours=1)}, SECRET_KEY)
```

---

### 42. Difference between Access Token and Refresh Token?

**উত্তর:**

| Access Token | Refresh Token |
|--------------|---------------|
| স্বল্পমেয়াদী (১৫-৩০ মিনিট) | দীর্ঘমেয়াদী (৭-৩০ দিন) |
| API অ্যাক্সেসের জন্য | নতুন Access Token পাওয়ার জন্য |
| বেশি ব্যবহার হয় | কম ব্যবহার হয় |
| Revoke করা কঠিন | Revoke করা সহজ |

**বাংলা ব্যাখ্যা:** Access Token হলো মূল টোকেন যা দিয়ে আপনি API তে ডেটা নেন। এটি অল্প সময়ের জন্য বৈধ। Refresh Token ব্যবহার করে মেয়াদ শেষ হয়ে গেলে নতুন Access Token নেওয়া যায়, যাতে ইউজারকে বারবার লগইন করতে না হয়।

---

### 43. How do you secure FastAPI endpoints?

**উত্তর:** FastAPI এন্ডপয়েন্ট সিকিউর করার উপায়:
1. **Dependency Injection:** `Depends()` দিয়ে অথেনটিকেশন চেক
2. **JWT:** টোকেন-বেসড অথেনটিকেশন
3. **OAuth2:** OAuth2PasswordBearer ব্যবহার
4. **Role-based Access:** ইউজার রোল চেক করে অ্যাক্সেস কন্ট্রোল
5. **HTTPS:** প্রোডাকশনে HTTPS ব্যবহার
6. **CORS:** সঠিক CORS সেটআপ

**বাংলা ব্যাখ্যা:** আপনার API কে শুধু অথেনটিকেটেড ইউজাররাই ব্যবহার করতে পারে সেটা নিশ্চিত করতে বিভিন্ন পদ্ধতি আছে। সবচেয়ে কমন হলো JWT টোকেন - ইউজার লগইন করলে টোকেন পায়, আর প্রতিটি রিকোয়েস্টে সেই টোকেন পাঠায়। 

---

### 44. What is OAuth2PasswordBearer?

**উত্তর:** OAuth2PasswordBearer হল FastAPI-এর একটি ক্লাস যা OAuth2 password flow ইমপ্লিমেন্ট করে। এটি request থেকে টোকেন এক্সট্র্যাক্ট করে এবং ভ্যালিডেশন করে।

**বাংলা ব্যাখ্যা:** এটি হলো FastAPI-এর বিল্ট-ইন টুল যা ইউজারনেম/পাসওয়ার্ড বেসড অথেনটিকেশন করে। এটি request এর Authorization header থেকে টোকেন নিয়ে চেক করে।

```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"token": token}
```

---

### 45. Why should passwords be hashed?

**উত্তর:** পাসওয়ার্ড হ্যাশ করার কারণ:
1. **Security:** ডেটাবেস চুরি গেলেও পাসওয়ার্ড পড়া যাবে না
2. **One-way:** হ্যাশ থেকে পাসওয়ার্ড বের করা অসম্ভব (প্রায়)
3. **Salting:** একই পাসওয়ার্ডের আলাদা হ্যাশ হয়
4. **Compliance:** GDPR, PCI-DSS কমপ্লায়েন্স

**বাংলা ব্যাখ্যা:** পাসওয়ার্ড কখনো প্লেইন টেক্সটে ডেটাবেসে সেভ করা উচিত নয়। যদি কেউ ডেটাবেস হ্যাক করে, তাহলে সব পাসওয়ার্ড চলে যাবে। তাই পাসওয়ার্ডকে হ্যাশ (গাণিতিকভাবে এনক্রিপ্ট) করে রাখা হয়। `bcrypt` বা `passlib` ব্যবহার করা হয়।

```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
```

---

## 🔴 Mid-Level (46–50)

### 46. How do you structure a FastAPI project?

**উত্তর:** একটি ভালো FastAPI প্রজেক্ট স্ট্রাকচার:

```
app/
├── main.py                 # এন্ট্রি পয়েন্ট
├── core/
│   ├── config.py          # কনফিগারেশন (.env)
│   └── security.py        # অথেনটিকেশন
├── database/
│   ├── connection.py      # ডেটাবেস কানেকশন
│   └── models.py          # SQLAlchemy মডেল
├── schemas/
│   └── user.py            # Pydantic মডেল
├── crud/
│   └── user.py            # ডেটাবেস অপারেশন
├── routers/
│   └── user.py            # API রাউটার
├── services/
│   └── user.py            # বিজনেস লজিক
└── utils/
    └── helpers.py         # হেল্পার ফাংশন
```

**বাংলা ব্যাখ্যা:** প্রজেক্ট স্ট্রাকচার মানে কোডগুলো কীভাবে সাজানো হবে। ভালো স্ট্রাকচার কোড পড়তে, মেইনটেইন করতে এবং টেস্ট করতে সহজ করে। বিভিন্ন ফোল্ডারে বিভিন্ন ধরনের কোড আলাদা করা হয়।

---

### 47. What is the difference between `models.py` and `schemas.py`?

**উত্তর:**

| models.py (SQLAlchemy) | schemas.py (Pydantic) |
|------------------------|----------------------|
| ডেটাবেস টেবিল ডিফাইন করে | API request/response ডেটা ডিফাইন করে |
| ডেটাবেস-নির্ভর | ডেটাবেস-স্বাধীন |
| ORM অপারেশনের জন্য | ভ্যালিডেশনের জন্য |
| `Base` থেকে ইনহেরিট করে | `BaseModel` থেকে ইনহেরিট করে |
| Column, Integer, String ব্যবহার | Python type hints ব্যবহার |

**বাংলা ব্যাখ্যা:** `models.py` তে SQLAlchemy মডেল থাকে যা ডেটাবেস টেবিলের সাথে সম্পর্কিত। `schemas.py` তে Pydantic মডেল থাকে যা API তে ডেটা আসা-যাওয়ার সময় ব্যবহৃত হয়। এদের আলাদা রাখা ভালো কারণ ডেটাবেসের ডেটা এবং API ডেটা আলাদা হতে পারে (যেমন: পাসওয়ার্ড শুধু API তে আসবে, ডেটাবেসে হ্যাশ হয়ে থাকে)।

---

### 48. Explain FastAPI request lifecycle.

**উত্তর:** FastAPI রিকোয়েস্ট লাইফসাইকেল:

```
Client (Browser/App)
    ↓
1. Uvicorn (ASGI Server) → রিকোয়েস্ট গ্রহণ
    ↓
2. FastAPI App → রিকোয়েস্ট প্রসেসিং শুরু
    ↓
3. Middleware → যদি থাকে, রিকোয়েস্ট প্রসেস করে
    ↓
4. Route Matching → কোন এন্ডপয়েন্টে যাবে
    ↓
5. Dependencies → `Depends()` গুলো রেজলভ করে
    ↓
6. Request Validation → Pydantic দিয়ে ডেটা ভ্যালিডেট
    ↓
7. Route Function → আপনার কোড এক্সিকিউট হয়
    ↓
8. Database → (যদি প্রয়োজন হয়) ডেটাবেস অপারেশন
    ↓
9. Response Validation → Pydantic দিয়ে রেসপন্স ভ্যালিডেট
    ↓
10. Response → ক্লায়েন্টে রেসপন্স পাঠানো
```

**বাংলা ব্যাখ্যা:** যখন কেউ আপনার API কল করে, তখন ডেটা কীভাবে প্রসেস হয় তার সম্পূর্ণ প্রক্রিয়া। প্রথমে Uvicorn রিকোয়েস্ট নেয়, তারপর FastAPI তে যায়, সেখানে ভ্যালিডেশন হয়, আপনার কোড রান করে, ডেটাবেস অপারেশন হয় (যদি থাকে), তারপর রেসপন্স ক্লায়েন্টে যায়।

---

### 49. How do you implement pagination?

**উত্তর:** Pagination ইমপ্লিমেন্ট করার উপায়:

```python
from sqlalchemy import func

@app.get("/users")
def get_users(
    skip: int = 0,      # কতটি স্কিপ করবে
    limit: int = 10,    # কতটি দেখাবে
    db: Session = Depends(get_db)
):
    total = db.query(func.count(User.id)).scalar()  # মোট কাউন্ট
    users = db.query(User).offset(skip).limit(limit).all()
    return {
        "total": total,
        "page": skip // limit + 1,
        "pages": (total + limit - 1) // limit,
        "data": users
    }
```

**বাংলা ব্যাখ্যা:** Pagination মানে অনেক ডেটা থাকলে তা পেজ আকারে দেখানো। যেমন: ১০০০ ইউজার থাকলে ১০ জন করে ১০০ পেজে দেখানো। `skip` দিয়ে কতটি বাদ দেবে, `limit` দিয়ে কতটি দেখাবে।

---

### 50. If you are building a production FastAPI application, what best practices would you follow?

**উত্তর:** প্রোডাকশন অ্যাপ্লিকেশনের জন্য বেস্ট প্র্যাকটিস:

1. **Environment Variables:** `.env` ব্যবহার করা (পাসওয়ার্ড, সিক্রেট কী)
2. **Project Structure:** পরিষ্কার স্ট্রাকচার
3. **Error Handling:** সব জায়গায় এরর হ্যান্ডেল
4. **Logging:** লগ রাখা
5. **Testing:** `pytest` দিয়ে টেস্ট
6. **Docker:** ডকারাইজ করা
7. **Database Connection Pool:** কানেকশন পুল ব্যবহার
8. **CORS:** সঠিক CORS সেটআপ
9. **Rate Limiting:** রেট লিমিট
10. **Security Headers:** নিরাপত্তা হেডার
11. **Async/await:** যেখানে সম্ভব async ব্যবহার
12. **Dependencies:** সব ডিপেন্ডেন্সি আপডেটেড রাখা

**বাংলা ব্যাখ্যা:** প্রোডাকশনে অ্যাপ চালানোর মানে রিয়েল ইউজার ব্যবহার করবে। তাই নিরাপত্তা, পারফরম্যান্স, রিলায়েবিলিটি সবকিছু নিশ্চিত করতে হবে। 

```python
# .env ব্যবহার
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str
    DATABASE_URL: str
    
    class Config:
        env_file = ".env"

settings = Settings()
```

---

## ⭐ Bonus: Scenario-Based Questions

### 1. How would you upload an image in FastAPI?

**উত্তর:** FastAPI তে ফাইল আপলোড করতে `File` এবং `UploadFile` ব্যবহার করা হয়:

```python
from fastapi import File, UploadFile

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    # ফাইল সেভ করা
    with open(f"uploads/{file.filename}", "wb") as f:
        f.write(contents)
    return {"filename": file.filename}
```

**বাংলা ব্যাখ্যা:** `UploadFile` ব্যবহার করে ইমেজ বা যেকোনো ফাইল আপলোড করা যায়। এটি async সাপোর্ট করে এবং বড় ফাইল efficient ভাবে হ্যান্ডেল করে।

---

### 2. How would you implement file download?

**উত্তর:** ফাইল ডাউনলোড করতে `FileResponse` ব্যবহার করা হয়:

```python
from fastapi.responses import FileResponse

@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = f"uploads/{filename}"
    return FileResponse(
        path=file_path,
        filename=filename,
        media_type="application/octet-stream"
    )
```

**বাংলা ব্যাখ্যা:** `FileResponse` দিয়ে সার্ভার থেকে ক্লায়েন্টে ফাইল পাঠানো যায়। media_type দিয়ে ফাইলের টাইপ নির্ধারণ করা হয়।

---

### 3. How would you send an email from FastAPI?

**উত্তর:** ইমেইল পাঠাতে `fastapi-mail` বা `smtplib` ব্যবহার করা হয়:

```python
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

@app.post("/send-email/")
async def send_email():
    message = MessageSchema(
        subject="Test Email",
        recipients=["user@email.com"],
        body="Hello World",
        subtype="html"
    )
    fm = FastMail(conf)
    await fm.send_message(message)
    return {"message": "Email sent"}
```

**বাংলা ব্যাখ্যা:** ইমেইল পাঠানোর জন্য SMTP সার্ভার ব্যবহার করা হয়। ব্যাকগ্রাউন্ড টাস্ক হিসেবে পাঠানো ভালো যাতে ইউজার অপেক্ষা না করে।

---

### 4. How would you integrate Redis with FastAPI?

**উত্তর:** Redis ইন্টিগ্রেট করতে `redis` প্যাকেজ ব্যবহার করা হয়:

```python
import redis
from fastapi import FastAPI

app = FastAPI()
redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.get("/cache/{key}")
async def get_cache(key: str):
    value = redis_client.get(key)
    if value:
        return {"cached": value}
    # ডেটাবেস থেকে ডেটা নেওয়া
    return {"data": "from db"}
```

**বাংলা ব্যাখ্যা:** Redis ক্যাশ হিসেবে ব্যবহার করা হয় ডেটা দ্রুত পাওয়ার জন্য। যেমন: ইউজারের প্রোফাইল ডেটা Redis এ ক্যাশ করে রাখলে বারবার ডেটাবেস কল করতে হয় না।

---

### 5. How would you implement background tasks?

**উত্তর:** Background tasks করতে `BackgroundTasks` ব্যবহার করা হয়:

```python
from fastapi import BackgroundTasks

def send_email(email: str, message: str):
    # ইমেইল পাঠানোর কোড
    pass

@app.post("/register/")
async def register_user(background_tasks: BackgroundTasks):
    # ইউজার রেজিস্টার করা
    background_tasks.add_task(send_email, "user@email.com", "Welcome!")
    return {"message": "User registered"}
```

**বাংলা ব্যাখ্যা:** Background tasks মানে এমন কাজ যা ইউজারকে অপেক্ষা করানো ছাড়াই পিছনে চালানো যায়। যেমন: ইমেইল পাঠানো, লগ সংরক্ষণ করা ইত্যাদি। ইউজার সঙ্গে সঙ্গে রেসপন্স পায়, কাজটা পিছনে চলে।

---

### 6. How would you build authentication with JWT?

**উত্তর:** JWT অথেনটিকেশন বিল্ড করতে:

```python
# 1. লগইন এন্ডপয়েন্ট - টোকেন তৈরি
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# 2. টোকেন ভেরিফাই
async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload

# 3. প্রোটেক্টেড এন্ডপয়েন্ট
@app.get("/users/me")
async def read_users_me(current_user = Depends(get_current_user)):
    return current_user
```

**বাংলা ব্যাখ্যা:** JWT অথেনটিকেশনে ইউজার লগইন করলে টোকেন পায়। প্রতিটি রিকোয়েস্টে টোকেন দিয়ে প্রমাণ করে যে সে অথেনটিকেটেড ইউজার।

---

### 7. How would you connect PostgreSQL?

**উত্তর:** PostgreSQL সংযোগ করতে:

```python
# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# main.py - dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

**বাংলা ব্যাখ্যা:** PostgreSQL সংযোগ করতে URL-এ ডেটাবেসের লোকেশন, ইউজারনেম, পাসওয়ার্ড দিতে হবে। SQLAlchemy এই URL ব্যবহার করে কানেকশন তৈরি করে।

---

### 8. How would you deploy FastAPI on a VPS?

**উত্তর:** VPS তে ডিপ্লয় করার ধাপ:

1. **Server Setup:** VPS এ Python ইনস্টল
2. **Code Transfer:** Git দিয়ে কোড ক্লোন
3. **Virtual Environment:** `python -m venv venv`
4. **Dependencies:** `pip install -r requirements.txt`
5. **Gunicorn + Uvicorn:** `gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app`
6. **Nginx:** রিভার্স প্রক্সি সেটআপ
7. **Systemd:** সার্ভিস হিসেবে চালানো
8. **SSL:** Let's Encrypt দিয়ে HTTPS

**বাংলা ব্যাখ্যা:** VPS তে ডিপ্লয় মানে আপনার অ্যাপ্লিকেশনকে ইন্টারনেটে লাইভ করা। Nginx রিভার্স প্রক্সি হিসেবে কাজ করে এবং SSL দিয়ে সিকিউর করা হয়।

---

### 9. How would you Dockerize a FastAPI application?

**উত্তর:** ডকারাইজ করতে Dockerfile তৈরি করা হয়:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/app
  db:
    image: postgres:15
    environment:
      - POSTGRES_PASSWORD=password
```

**বাংলা ব্যাখ্যা:** Docker ব্যবহার করলে অ্যাপ্লিকেশন যে কোনো জায়গায় একইভাবে চালানো যায়। Dockerfile বলে দেয় কীভাবে অ্যাপ বানাতে হবে। docker-compose দিয়ে একসাথে একাধিক সার্ভিস (অ্যাপ + ডেটাবেস) চালানো যায়।

---

### 10. How would you improve FastAPI performance?

**উত্তর:** পারফরম্যান্স উন্নত করার উপায়:

1. **Async/Await:** I/O অপারেশনে async ব্যবহার
2. **Connection Pooling:** ডেটাবেস কানেকশন পুল
3. **Caching:** Redis বা অন্য ক্যাশ
4. **Gunicorn Workers:** মাল্টিপল ওয়ার্কার
5. **Database Indexing:** সঠিক ইনডেক্স
6. **Query Optimization:** জটিল কোয়েরি অপটিমাইজ
7. **CDN:** স্ট্যাটিক ফাইলের জন্য
8. **Load Balancer:** একাধিক সার্ভার
9. **Profiling:** কোড প্রোফাইল করে বটলনেক খুঁজে বের করা
10. **Pydantic v2:** নতুন ভার্সন দ্রুততর

**বাংলা ব্যাখ্যা:** পারফরম্যান্স মানে অ্যাপ কত দ্রুত কাজ করে। async ব্যবহার করলে অনেক রিকোয়েস্ট একসাথে হ্যান্ডেল করা যায়। ক্যাশ ব্যবহার করলে বারবার ডেটাবেস কল করতে হয় না। মাল্টিপল ওয়ার্কার দিয়ে CPU ভালোভাবে ব্যবহার করা যায়।

---

## 💼 Final Tips for Interview

১. **হাতে কলমে কোড লেখার অভ্যাস করুন** - ইন্টারভিউতে কোড লিখতে হতে পারে
২. **প্রতিটি টপিকের প্র্যাকটিক্যাল উদাহরণ জানুন**
৩. **প্রজেক্টে কীভাবে ব্যবহার করেছেন সেটা বলতে পারবেন**
৪. **Common issues এবং তাদের সমাধান জানুন**
৫. **FastAPI vs অন্যান্য ফ্রেমওয়ার্কের তুলনা করতে পারবেন**
৬. **Async/await সম্পর্কে ক্লিয়ার কনসেপ্ট থাকতে হবে**
৭. **ডেটাবেস অপারেশন সম্পর্কে ভালো ধারণা থাকতে হবে**
৮. **Authentication/Authorization সম্পর্কে জানতে হবে**

শুভকামনা! 🚀

