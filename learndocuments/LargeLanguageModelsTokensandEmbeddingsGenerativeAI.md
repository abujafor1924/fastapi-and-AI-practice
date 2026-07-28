চমৎকার! এখন আমরা আসছি **Generative AI** এবং **Large Language Models (LLMs)**-এর মৌলিক ধারণাগুলোতে – বিশেষ করে **Tokens** এবং **Embeddings**। এগুলোই হলো আধুনিক AI-এর (ChatGPT, Gemini, Claude ইত্যাদি) ভিত্তি।

আমি এখন **LLM বেসিক, Token, Embedding** – সবকিছু বিস্তারিত বাংলায় ব্যাখ্যা করব, তারপর **২০টি ইন্টারভিউ প্রশ্ন ও উত্তর** দেব।

---

## 🧠 Large Language Model (LLM) কী?

**Large Language Model (LLM)** হলো একটি **Neural Network**-ভিত্তিক মডেল যা বিপুল পরিমাণ টেক্সট ডেটার উপর ট্রেইন করা হয়। এটি **টেক্সট জেনারেট**, **সারসংক্ষেপ**, **অনুবাদ**, **কোড লেখা** – এমনকি **রিজনিং** পর্যন্ত করতে পারে।

**LLM-এর প্রধান বৈশিষ্ট্য:**
- **বিপুল সংখ্যক প্যারামিটার** (বিলিয়ন বা ট্রিলিয়ন)
- **Transformer Architecture** ব্যবহার করে
- **Self-Supervised Learning** (পূর্ববর্তী শব্দ থেকে পরবর্তী শব্দ প্রেডিক্ট করে শেখে)
- **Context Window** (একবারে কতটুকু টেক্সট "দেখতে" পারে)

**প্রচলিত LLM:**
- **GPT (OpenAI):** GPT-3, GPT-4, ChatGPT
- **Gemini (Google):** Gemini Pro, Ultra
- **Claude (Anthropic):** Claude 3
- **LLaMA (Meta):** LLaMA 2, LLaMA 3
- **Mistral, Falcon, BERT** ইত্যাদি

---

## 🔤 Token কী?

**Token** হলো LLM-এর ভাষার **সবচেয়ে ছোট একক**। টেক্সটকে টোকেনে ভাগ করাকে বলে **Tokenization**।

### টোকেন কেমন হয়?

| টেক্সট | টোকেন |
|--------|--------|
| "Hello" | ["Hello"] (১টি টোকেন) |
| "Hello World" | ["Hello", "World"] (২টি টোকেন) |
| "I love AI" | ["I", "love", "AI"] (৩টি টোকেন) |
| "Unbelievable" | ["Un", "belie", "vable"] (৩টি সাব-ওয়ার্ড টোকেন) |
| "আমি বাংলায় কথা বলি" | ["আমি", "বাংলায়", "কথা", "বলি"] (৪টি টোকেন) |

### Tokenization-এর প্রকারভেদ

1. **Word Tokenization:** শব্দ অনুযায়ী ভাগ (যেমন: space দিয়ে)  
   - সমস্যা: অজানা শব্দ (OOV – Out of Vocabulary) হ্যান্ডেল করতে পারে না

2. **Character Tokenization:** প্রতিটি অক্ষর আলাদা টোকেন  
   - সমস্যা: খুব লম্বা সিকোয়েন্স, কম্পিউটেশনালি ব্যয়বহুল

3. **Subword Tokenization (সেরা):** সাধারণ শব্দ পুরো রাখে, বিরল শব্দ ছোট অংশে ভাগ করে  
   - **BPE (Byte-Pair Encoding):** GPT-তে ব্যবহৃত হয়  
   - **WordPiece:** BERT-তে ব্যবহৃত হয়  
   - **SentencePiece:** LLaMA, Gemini-তে ব্যবহৃত হয়

```python
# Hugging Face Transformers দিয়ে Tokenization
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")
tokens = tokenizer.tokenize("I love artificial intelligence!")
print(tokens)
# ['I', 'Ġlove', 'Ġartificial', 'Ġintelligence', '!']

# টোকেন আইডি
token_ids = tokenizer.encode("I love AI")
print(token_ids)  # [40, 716, 1234]
```

### কেন Token গুরুত্বপূর্ণ?

- LLM **টোকেনের সিকোয়েন্স** হিসেবে ইনপুট নেয়
- **Context Window** টোকেন সংখ্যা দিয়ে মাপা হয় (যেমন: GPT-4 Turbo → 128K টোকেন)
- **API খরচ** টোকেন ভিত্তিক (ইনপুট + আউটপুট টোকেন)
- টোকেনাইজেশন ভাষাভেদে ভিন্ন হয় (ইংরেজিতে ১ টোকেন ≈ ৪ অক্ষর, বাংলায় ১ টোকেন ≈ ২-৩ অক্ষর)

---

## 🧬 Embedding কী?

**Embedding** হলো টেক্সট, শব্দ বা সত্তাকে **সংখ্যার ভেক্টরে** (vector) রূপান্তর করার প্রক্রিয়া। এই ভেক্টরগুলি এমনভাবে তৈরি হয় যে **একই অর্থের শব্দগুলির ভেক্টর কাছাকাছি** থাকে।

### Embedding-এর বৈশিষ্ট্য

```python
# ধরা যাক, 3D embedding space
king = [0.8, 0.2, 0.9]
queen = [0.7, 0.3, 0.8]   # king-এর কাছে
man = [0.6, -0.1, 0.4]
woman = [0.5, 0.0, 0.5]   # man-এর কাছে

# king - man + woman ≈ queen (প্রসিদ্ধ উদাহরণ!)
```

### Embedding-এর প্রকারভেদ

| ধরণ | বিবরণ | উদাহরণ |
|------|--------|---------|
| **Word Embedding** | প্রতিটি শব্দের ভেক্টর | Word2Vec, GloVe, FastText |
| **Sentence Embedding** | পুরো বাক্যের ভেক্টর | Sentence-BERT, Universal Sentence Encoder |
| **Contextual Embedding** | প্রসঙ্গ অনুযায়ী ভিন্ন ভেক্টর | BERT, GPT-এর এম্বেডিং (প্রতিটি লেয়ার) |

### Embedding Dimension (ডাইমেনশন)

- **Word2Vec:** সাধারণত 100-300 ডাইমেনশন
- **BERT-base:** 768 ডাইমেনশন
- **BERT-large:** 1024 ডাইমেনশন
- **GPT-3:** 12288 ডাইমেনশন
- **OpenAI Embeddings:** 1536 ডাইমেনশন (`text-embedding-ada-002`)

### Embedding কীভাবে কাজ করে?

1. প্রতিটি টোকেনকে **র্যান্ডম ভেক্টর** দিয়ে শুরু করা হয়
2. মডেল ট্রেইনিং-এর সময় ভেক্টরগুলো **আপডেট** হয়
3. একই অর্থের শব্দগুলোর ভেক্টর **কাছাকাছি** আসে (cosine similarity বেশি)
4. ভিন্ন অর্থের শব্দগুলো **দূরে** সরে যায়

```python
# OpenAI Embeddings উদাহরণ
import openai

response = openai.Embedding.create(
    model="text-embedding-ada-002",
    input="I love artificial intelligence"
)
embedding_vector = response['data'][0]['embedding']  # 1536 ডাইমেনশনের ভেক্টর
print(len(embedding_vector))  # 1536
```

### Embedding-এর ব্যবহার

1. **Semantic Search** – অর্থ অনুযায়ী সার্চ
2. **RAG (Retrieval-Augmented Generation)** – ডকুমেন্ট রিট্রিভাল
3. **Recommendation Systems** – কন্টেন্ট রেকমেন্ডেশন
4. **Clustering** – একই ধরনের টেক্সট একত্রিত করা
5. **Classification** – টেক্সট ক্যাটেগরাইজেশন
6. **Anomaly Detection** – অস্বাভাবিক টেক্সট খোঁজা

---

## 🏗️ LLM-এর Architecture (Transformer)

### Transformer-এর মূল উপাদান

1. **Tokenization** – টেক্সট → টোকেন
2. **Embedding Layer** – টোকেন → ভেক্টর (Embedding)
3. **Positional Encoding** – শব্দের ক্রম বুঝতে
4. **Multi-Head Self-Attention** – কোন শব্দ কোন শব্দের সাথে সম্পর্কিত
5. **Feed-Forward Neural Network** – নন-লিনিয়ার ট্রান্সফর্মেশন
6. **Layer Normalization + Residual Connections** – স্টেবিলিটি
7. **Softmax Output** – পরবর্তী টোকেন প্রেডিক্ট

### Self-Attention Mechanism (সহজ ভাষায়)

"**The cat sat on the mat**" – এই বাক্যে "sat" শব্দটি "cat"-এর সাথে বেশি সম্পর্কিত, "mat"-এর সাথে কম। Self-Attention প্রতিটি শব্দের জন্য **অন্য সব শব্দের সাথে সম্পর্কের গুরুত্ব** (attention weight) বের করে।

```
Query (Q): আমি কী খুঁজছি?
Key (K):   আমার কাছে কী আছে?
Value (V): আসল তথ্য কী?

Attention = softmax(Q × Kᵀ) × V
```

---

## 🔄 LLM-এর Training Process

### 1. Pre-training (প্রাক-প্রশিক্ষণ)

- **বিপুল ডেটা** (ইন্টারনেট, বই, উইকিপিডিয়া) – টেরাবাইটস
- **Self-Supervised Learning** – পরবর্তী শব্দ প্রেডিক্ট করা (Next Token Prediction)
- **Cost:** মিলিয়ন ডলার (GPT-3-এর ট্রেইনিং খরচ ~$4.6M)

### 2. Fine-tuning (সূক্ষ্ম-প্রশিক্ষণ)

- নির্দিষ্ট কাজের জন্য ডেটাতে আরও ট্রেইন করা
- **Instruction Tuning:** "এভাবে উত্তর দাও" – ChatGPT-এর মতো

### 3. RLHF (Reinforcement Learning from Human Feedback)

- মানুষ ভালো/খারাপ উত্তর রেট করে
- মডেল শেখে কীভাবে ভালো উত্তর দিতে হয়
- ChatGPT-এর সাফল্যের মূল চাবিকাঠি

---

## 📊 LLM-এর Evaluation Metrics

1. **Perplexity** – মডেল কতটা "অবাক" হয় (কম = ভালো)
2. **BLEU** – মেশিন ট্রান্সলেশন মান
3. **ROUGE** – সারসংক্ষেপের মান
4. **Human Evaluation** – মানুষ রেট করে
5. **MMLU, GSM8K, HumanEval** – বেঞ্চমার্ক টেস্ট

---

## 🛠️ LLM ব্যবহারের Practical Way (Python)

### 1. Hugging Face Transformers

```python
from transformers import pipeline

# Text Generation
generator = pipeline('text-generation', model='gpt2')
result = generator("Once upon a time", max_length=50)
print(result[0]['generated_text'])

# Sentiment Analysis
classifier = pipeline('sentiment-analysis')
result = classifier("I love this product!")
print(result)  # [{'label': 'POSITIVE', 'score': 0.999}]

# Zero-shot Classification
classifier = pipeline('zero-shot-classification')
result = classifier("I want to cancel my order", 
                   candidate_labels=['refund', 'delivery', 'support'])
```

### 2. OpenAI API

```python
import openai

openai.api_key = "your-api-key"

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain quantum physics in simple terms."}
    ],
    max_tokens=200,
    temperature=0.7
)

print(response['choices'][0]['message']['content'])
```

### 3. Embedding Creation

```python
# OpenAI Embedding
response = openai.Embedding.create(
    model="text-embedding-ada-002",
    input="Your text here"
)
embedding = response['data'][0]['embedding']

# Sentence Transformers (Open Source)
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(["Hello world", "How are you?"])
print(embeddings.shape)  # (2, 384)
```

---

## 🔍 Semantic Search using Embeddings

```python
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# ধরা যাক, ডকুমেন্টগুলোর এম্বেডিং আছে
documents = [
    "I love machine learning",
    "Python is a programming language",
    "AI is transforming the world"
]
doc_embeddings = model.encode(documents)  # (3, 384)

# Query
query = "Tell me about AI"
query_embedding = model.encode([query])   # (1, 384)

# Cosine Similarity
similarities = cosine_similarity(query_embedding, doc_embeddings)
best_match_idx = np.argmax(similarities)
print(f"Best match: {documents[best_match_idx]}")
```

---

## 🧠 RAG (Retrieval-Augmented Generation)

RAG হলো একটি কৌশল যেখানে LLM-কে **বাইরের ডকুমেন্ট থেকে তথ্য এনে** উত্তর দিতে বলা হয়।

```
User Query → Embedding → Vector Database Search → Relevant Documents → LLM → Answer
```

```python
# RAG-এর সরল উদাহরণ
query = "What is the capital of Bangladesh?"
relevant_docs = vector_db.search(query)  # "Dhaka is the capital..."

prompt = f"""
Context: {relevant_docs}
Question: {query}
Answer based on the context only:
"""

response = llm.generate(prompt)
# Output: "The capital of Bangladesh is Dhaka"
```

---

# 📋 LLM, Token, Embedding – ২০টি ইন্টারভিউ প্রশ্ন ও উত্তর

---

### **প্রশ্ন ১: Large Language Model (LLM) কী? এটি কীভাবে কাজ করে?**

**উত্তর:**

**LLM** হলো একটি বড় নিউরাল নেটওয়ার্ক যা বিপুল পরিমাণ টেক্সট ডেটাতে ট্রেইন করা হয়। এটি **Transformer Architecture** ব্যবহার করে এবং **পরবর্তী টোকেন প্রেডিক্ট** করে টেক্সট জেনারেট করে।

**কাজ করার ধাপ:**
1. টেক্সট → **Tokenization** (টোকেনে ভাগ)
2. প্রতিটি টোকেন → **Embedding** (সংখ্যার ভেক্টর)
3. Embeddings → **Transformer Layer** (Self-Attention + FFN)
4. আউটপুট → **Softmax** → পরবর্তী টোকেনের Probability
5. সবচেয়ে সম্ভাব্য টোকেন সিলেক্ট করে আউটপুটে যোগ করে
6. স্টেপ ৩-৫ রিপিট করে সম্পূর্ণ টেক্সট জেনারেট করে

---

### **প্রশ্ন ২: Token কী? Tokenization কেন প্রয়োজন?**

**উত্তর:**

**Token** হলো LLM-এর ভাষার মৌলিক একক – টেক্সটের একটি অংশ (শব্দ, সাব-ওয়ার্ড, অক্ষর) যা মডেল ইনপুট হিসেবে নেয়।

**Tokenization প্রয়োজন কারণ:**
- LLM টেক্সট সরাসরি বুঝতে পারে না – এটি শুধু সংখ্যা প্রসেস করতে পারে
- টোকেন → সংখ্যায় (Token ID) কনভার্ট করে
- সাব-ওয়ার্ড টোকেনাইজেশন অজানা শব্দ (OOV) হ্যান্ডেল করতে পারে
- টোকেন সংখ্যা Context Window এবং API খরচ নির্ধারণ করে

```python
# উদাহরণ: GPT-2 Tokenization
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")
tokens = tokenizer.tokenize("I love AI")
print(tokens)  # ['I', 'Ġlove', 'ĠAI']
```

---

### **প্রশ্ন ৩: BPE, WordPiece, SentencePiece – এগুলোর মধ্যে পার্থক্য কী?**

**উত্তর:**

এগুলো সবই **Subword Tokenization** পদ্ধতি।

| পদ্ধতি | বিবরণ | ব্যবহার |
|--------|--------|----------|
| **BPE (Byte-Pair Encoding)** | সবচেয়ে কমন পেয়ার মージ করে | GPT, LLaMA, RoBERTa |
| **WordPiece** | BPE-এর মতো কিন্তু মরফোলজি সংরক্ষণ করে | BERT, DistilBERT |
| **SentencePiece** | ভাষা-স্বাধীন (স্পেসও টোকেন হিসেবে), নিয়মিত এক্সপ্রেশন দরকার নেই | LLaMA, Gemini, T5 |

```python
# BPE Example (GPT-2)
"unbelievable" → ["un", "believ", "able"]

# WordPiece (BERT)
"unbelievable" → ["un", "##believ", "##able"]

# SentencePiece (LLaMA)
"unbelievable" → ["▁un", "belie", "vable"]
```

---

### **প্রশ্ন ৪: Embedding কী? এটি কীভাবে কাজ করে?**

**উত্তর:**

**Embedding** হলো টেক্সট, শব্দ বা সত্তাকে **ঘন (dense) সংখ্যার ভেক্টর**-এ রূপান্তর করার প্রক্রিয়া। এই ভেক্টরগুলো ডেটা থেকে শেখা হয় এবং একই অর্থের শব্দের ভেক্টর কাছাকাছি থাকে।

**কীভাবে কাজ করে:**
1. প্রতিটি টোকেনের জন্য **র্যান্ডম ভেক্টর** দিয়ে শুরু
2. ট্রেইনিং-এর সময় নিউরাল নেটওয়ার্ক ভেক্টরগুলো **আপডেট** করে
3. একই কনটেক্সটে আসা শব্দগুলোর ভেক্টর **কাছাকাছি** আসে (cosine similarity বেশি)
4. ভিন্ন অর্থের শব্দ **দূরে** সরে যায়

```python
# Example: Word2Vec
king = [0.8, 0.2, 0.9]
queen = [0.7, 0.3, 0.8]   # king-এর কাছে
```

---

### **প্রশ্ন ৫: Word2Vec, GloVe, এবং Contextual Embedding (BERT/GPT)-এর মধ্যে পার্থক্য কী?**

**উত্তর:**

| টাইপ | বিবরণ | উদাহরণ | বৈশিষ্ট্য |
|------|--------|---------|-----------|
| **Static Word Embedding** | প্রতিটি শব্দের জন্য **একটি** ভেক্টর (প্রসঙ্গ নিরপেক্ষ) | Word2Vec, GloVe, FastText | "bank" এর জন্য সব জায়গায় একই ভেক্টর |
| **Contextual Embedding** | প্রসঙ্গ অনুযায়ী **ভিন্ন** ভেক্টর | BERT, GPT, ELMo | "bank" (নদীর তীর) vs "bank" (ব্যাংক) – আলাদা |

```python
# Contextual Embedding (BERT)
sentence1 = "I went to the bank to deposit money."
sentence2 = "I sat on the river bank."
# BERT "bank"-এর জন্য ভিন্ন ভিন্ন ভেক্টর দিবে!
```

---

### **প্রশ্ন ৬: Transformer Architecture-এর মূল উপাদানগুলো কী কী?**

**উত্তর:**

Transformer-এর মূল উপাদান:

1. **Input Embedding** – টোকেন → ভেক্টর
2. **Positional Encoding** – শব্দের ক্রম (order) বুঝতে
3. **Multi-Head Self-Attention** – প্রতিটি শব্দের সাথে অন্য শব্দের সম্পর্ক
4. **Feed-Forward Neural Network** – নন-লিনিয়ার ট্রান্সফর্মেশন
5. **Layer Normalization** – ট্রেইনিং স্টেবিলিটি
6. **Residual Connections** – গ্রেডিয়েন্ট সমস্যা সমাধান
7. **Softmax Output** – পরবর্তী টোকেন প্রেডিক্ট

```
Input → Embedding → Positional Encoding → Multi-Head Attention 
→ Add & Norm → FFN → Add & Norm → (repeat N times) → Output
```

---

### **প্রশ্ন ৭: Self-Attention কী? Query, Key, Value কী?**

**উত্তর:**

**Self-Attention** হলো Transformer-এর সবচেয়ে গুরুত্বপূর্ণ অংশ যা প্রতিটি শব্দের জন্য অন্য সব শব্দের সাথে **সম্পর্কের গুরুত্ব** (attention weight) বের করে।

**Query, Key, Value:**
- **Query (Q):** "আমি কী খুঁজছি?" (বর্তমান শব্দের প্রশ্ন)
- **Key (K):** "আমার কাছে কী আছে?" (অন্য শব্দগুলোর তথ্য)
- **Value (V):** "আসল তথ্য কী?" (শব্দটির অর্থ)

```
Attention(Q, K, V) = softmax(Q × Kᵀ / √d) × V
```

**সহজ ভাষায়:** প্রতিটি শব্দ অন্য সব শব্দকে "জিজ্ঞেস" করে – "তুমি আমার জন্য কতটুকু গুরুত্বপূর্ণ?" – এবং সেই গুরুত্ব অনুযায়ী তথ্য সংগ্রহ করে।

---

### **প্রশ্ন ৮: Multi-Head Attention কী?**

**উত্তর:**

**Multi-Head Attention** হলো একাধিক Self-Attention (Head) সমান্তরালভাবে চালানো। প্রতিটি Head ভিন্ন ভিন্ন সম্পর্ক শেখে।

**কেন Multi-Head?**
- একটি Head শিখতে পারে **সিনট্যাকটিক** সম্পর্ক (যেমন: subject-verb)
- অন্যটি শিখতে পারে **সিমেন্টিক** সম্পর্ক (যেমন: synonym)
- আরেকটি শিখতে পারে **দূরবর্তী** সম্পর্ক (যেমন: অ্যানাফোরা)

```python
# GPT-3: 96 Layers, প্রতিটি Layer-এ 96 Heads
# Total = 96 × 96 = 9216 Attention Heads!
```

---

### **প্রশ্ন ৯: Positional Encoding কী? কেন দরকার?**

**উত্তর:**

Transformer-তে **কোনো RNN বা CNN নেই** – তাই এটি শব্দের **অর্ডার** (ক্রম) বুঝতে পারে না। Positional Encoding শব্দের অবস্থান (পজিশন) সম্পর্কে তথ্য যোগ করে।

**Positional Encoding-এর প্রকার:**
1. **Sinusoidal (সাইন-কোসাইন):** ফিক্সড ফরমুলা (Original Transformer)
2. **Learned Positional Embedding:** মডেল নিজেই শেখে (GPT, BERT)
3. **Relative Positional Encoding:** শব্দের মধ্যে দূরত্ব (RoPE, ALiBi)

```python
# Sinusoidal Encoding Example
PE(pos, 2i) = sin(pos / 10000^(2i/d))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d))
```

---

### **প্রশ্ন ১০: Pre-training এবং Fine-tuning-এর মধ্যে পার্থক্য কী?**

**উত্তর:**

| Pre-training | Fine-tuning |
|--------------|-------------|
| **বিপুল ডেটা** (ইন্টারনেট, বই) | **ছোট ডেটা** (নির্দিষ্ট কাজের জন্য) |
| **Self-supervised** (Next Token Prediction) | **Supervised** (লেবেলযুক্ত ডেটা) |
| **সাধারণ জ্ঞান** শেখে | **নির্দিষ্ট কাজ** শেখে (যেমন: Sentiment Analysis) |
| **ব্যয়বহুল** ($M+) | **সস্তা** ($) |
| একবার করে ফেললে বারবার ব্যবহার | প্রতিটি কাজের জন্য আলাদা |

```python
# Pre-trained model (BERT)
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

# Fine-tuning
model.fit(train_data, labels)
```

---

### **প্রশ্ন ১১: RLHF (Reinforcement Learning from Human Feedback) কী?**

**উত্তর:**

RLHF হলো একটি ট্রেইনিং পদ্ধতি যেখানে:
1. মডেল বিভিন্ন উত্তর জেনারেট করে
2. মানুষ উত্তরগুলোর **র্যাঙ্কিং** দেয় (কোনটা ভালো, কোনটা খারাপ)
3. র্যাঙ্কিং থেকে একটি **Reward Model** ট্রেইন করা হয়
4. Reward Model ব্যবহার করে মডেলকে **Reinforcement Learning** দিয়ে টিউন করা হয়

**RLHF-এর কারণে ChatGPT-এর উত্তর:** 
- বেশি হেল্পফুল
- কম হ্যালুসিনেট করে
- ইনস্ট্রাকশন ভালো ফলো করে
- কম টক্সিক

```
RLHF Pipeline:
LLM → Generate Responses → Human Ranking → Reward Model → PPO Training → Better LLM
```

---

### **প্রশ্ন ১২: Context Window কী? কেন গুরুত্বপূর্ণ?**

**উত্তর:**

**Context Window** হলো LLM একটি ইনপুটে কতগুলো টোকেন "দেখতে" পারে (প্রসেস করতে পারে) – তার সীমা।

**গুরুত্ব:**
- বড় Context Window → **বড় ডকুমেন্ট** বা **দীর্ঘ কথোপকথন** প্রসেস করতে পারে
- ছোট Context Window → তথ্য হারিয়ে যায় (কথার শুরু ভুলে যায়)

**উদাহরণ:**
- GPT-3.5: 4,096 টোকেন (~3,000 শব্দ)
- GPT-4 Turbo: 128,000 টোকেন (~100,000 শব্দ)
- Claude 3: 200,000 টোকেন (~150,000 শব্দ)
- Gemini 1.5 Pro: 2,000,000 টোকেন (~পুরো Harry Potter সিরিজ!)

---

### **প্রশ্ন ১৩: Hallucination কী? কীভাবে কমানো যায়?**

**উত্তর:**

**Hallucination** হলো যখন LLM এমন তথ্য জেনারেট করে যা **সঠিক নয়** কিন্তু যুক্তিযুক্ত/বিশ্বাসযোগ্য মনে হয় – এটাকে "মিথ্যা বলা" বা "বানোয়াট" বলতে পারেন।

**Hallucination কমানোর উপায়:**
1. **RAG (Retrieval-Augmented Generation)** – বাইরের ডকুমেন্ট থেকে তথ্য এনে উত্তর
2. **Fine-tuning** – নির্ভুল ডেটাতে টিউন করা
3. **Temperature কমানো** – কম ক্রিয়েটিভ, বেশি ডিটারমিনিস্টিক
4. **Prompt Engineering** – "শুধু ফ্যাক্ট বলো" বা "উৎস উল্লেখ করো"
5. **Human-in-the-loop** – ক্রিটিক্যাল কাজে মানুষ চেক করে
6. **Self-Consistency** – একই প্রশ্ন একাধিকবার করে মিল চেক

---

### **প্রশ্ন ১৪: RAG (Retrieval-Augmented Generation) কী?**

**উত্তর:**

**RAG** হলো একটি কৌশল যেখানে LLM-কে **বাইরের ডকুমেন্ট ডেটাবেস** থেকে প্রাসঙ্গিক তথ্য এনে উত্তর দিতে বলা হয়।

**RAG এর ধাপ:**
1. User Query → **Embedding** → Vector Database
2. Database থেকে **সবচেয়ে প্রাসঙ্গিক ডকুমেন্ট** খোঁজা (Semantic Search)
3. Query + Relevant Documents → **Prompt** তৈরি
4. Prompt → **LLM** → উত্তর

**RAG-এর সুবিধা:**
- Hallucination কমায়
- বর্তমান (up-to-date) তথ্য দিতে পারে
- কোম্পানির নিজস্ব ডেটা ব্যবহার করতে পারে
- নতুন ডেটা দিয়ে মডেল পুনরায় ট্রেইন করতে হয় না

```python
# RAG Pipeline (সরল)
query = "What is RAG?"
docs = vector_db.search(query)  # ["RAG stands for Retrieval-Augmented Generation..."]
prompt = f"Context: {docs}\nQuestion: {query}"
response = llm.generate(prompt)
```

---

### **প্রশ্ন ১৫: Temperature এবং Top-p (Nucleus Sampling) কী?**

**উত্তর:**

এগুলো LLM-এর **Output Randomness** নিয়ন্ত্রণ করে।

| Parameter | কাজ | কম মান | বেশি মান |
|-----------|-----|---------|----------|
| **Temperature** | Probability Distribution-এর "sharpness" | 0.0 → ডিটারমিনিস্টিক (সবসময় একই) | 1.0 → বেশি র্যান্ডম/ক্রিয়েটিভ |
| **Top-p (Nucleus)** | মোট probability p-এর মধ্যে সীমাবদ্ধ রাখে | 0.1 → শুধু টপ কয়েকটি টোকেন | 1.0 → সব টোকেন বিবেচনা করে |

```python
# OpenAI API-তে ব্যবহার
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[...],
    temperature=0.7,    # মিডিয়াম ক্রিয়েটিভিটি
    top_p=0.9           # ৯০% probability কভার করে
)

# Creative writing → temperature 0.9
# Factual Q&A → temperature 0.1
```

---

### **প্রশ্ন ১৬: LLM-এর Evaluation Metrics কী কী?**

**উত্তর:**

| Metric | কী মাপে | ব্যবহার |
|--------|---------|----------|
| **Perplexity** | মডেল কতটা "অবাক" হয় (কম = ভালো) | Language Modeling |
| **BLEU** | Machine Translation-এর মান | Translation, Summarization |
| **ROUGE** | Reference-এর সাথে overlap | Summarization |
| **METEOR** | Precision + Recall + Alignment | Translation |
| **MMLU** | ৫৭টি বিষয়ে MCQ | General Knowledge |
| **GSM8K** | Math Word Problem | Reasoning |
| **HumanEval** | Code Generation | Programming |
| **Chatbot Arena** | Human ELO Rating | Conversation Quality |

---

### **প্রশ্ন ১৭: Zero-shot, Few-shot, Chain-of-Thought (CoT) কী?**

**উত্তর:**

| পদ্ধতি | বিবরণ | উদাহরণ Prompt |
|--------|--------|----------------|
| **Zero-shot** | কোনো উদাহরণ ছাড়াই কাজ করে | "Translate to Bangla: Hello" |
| **Few-shot** | ২-৩টি উদাহরণ দিয়ে কাজ শেখায় | "Eng: Hello → Ban: হ্যালো\nEng: Good → Ban: ভালো\nEng: Book → Ban: ?" |
| **Chain-of-Thought (CoT)** | স্টেপ বাই স্টেপ রিজনিং দেখায় | "Let's think step by step: 1. ... 2. ... 3. ..." |

```python
# Zero-shot
prompt = "Classify sentiment: I love this product."

# Few-shot
prompt = """
Review: Great product! → Positive
Review: Terrible service → Negative
Review: Average quality → ?
"""

# Chain-of-Thought
prompt = """
Q: If a train travels 60 miles in 2 hours, what's its speed?
Let's solve step by step:
1. Speed = Distance / Time
2. Distance = 60 miles
3. Time = 2 hours
4. Speed = 60/2 = 30 mph
Answer: 30 mph
"""
```

---

### **প্রশ্ন ১৮: Embedding-এ Cosine Similarity কেন ব্যবহার করা হয়?**

**উত্তর:**

**Cosine Similarity** দুইটি ভেক্টরের মধ্যে **কোণের কোসাইন** মাপে – যার মান -1 থেকে 1 এর মধ্যে।

```
Cosine Similarity = (A · B) / (||A|| × ||B||)
```

**কেন Cosine?**
- **ভেক্টরের দৈর্ঘ্য (magnitude) নিয়ে কাজ করে না** – শুধু দিক (direction) দেখে
- Embedding-এ গুরুত্বপূর্ণ হলো **দিক** (অর্থের দিক) – দৈর্ঘ্য না
- মান -1 (বিপরীত) থেকে 1 (একই) – 1 হলে অর্থ একই
- Euclidean Distance-এর চেয়ে ভালো কারণ স্কেলিং-এর প্রতি কম সংবেদনশীল

```python
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

vec1 = np.array([0.8, 0.2, 0.9])
vec2 = np.array([0.7, 0.3, 0.8])
sim = cosine_similarity([vec1], [vec2])
print(sim)  # 0.99 (খুব কাছাকাছি)
```

---

### **প্রশ্ন ১৯: Vector Database কী? কেন LLM-এর জন্য গুরুত্বপূর্ণ?**

**উত্তর:**

**Vector Database** হলো এমন একটি ডেটাবেস যা **Embedding ভেক্টর** সংরক্ষণ করে এবং **Semantic Search** (অর্থ ভিত্তিক সার্চ) করতে পারে।

**জনপ্রিয় Vector Databases:**
- Pinecone, Weaviate, Chroma, Milvus, Qdrant, FAISS (Facebook)

**কেন গুরুত্বপূর্ণ?**
1. **RAG-এর জন্য অপরিহার্য** – দ্রুত প্রাসঙ্গিক ডকুমেন্ট খোঁজে
2. **Semantic Search** – কীওয়ার্ড না, অর্থ দিয়ে সার্চ
3. **Scalability** – মিলিয়ন ডকুমেন্টের মধ্যে দ্রুত সার্চ (Approximate Nearest Neighbor)

```python
# ChromaDB উদাহরণ
import chromadb
client = chromadb.Client()
collection = client.create_collection("my_docs")

# Add documents
collection.add(
    documents=["I love AI", "Python is great"],
    ids=["doc1", "doc2"]
)

# Search
results = collection.query(query_texts=["machine learning"], n_results=1)
```

---

### **প্রশ্ন ২০: Prompt Engineering কী? ভালো Prompt-এর নিয়ম কী?**

**উত্তর:**

**Prompt Engineering** হলো LLM থেকে **সর্বোত্তম উত্তর** পাওয়ার জন্য Input (Prompt) ডিজাইন করার শিল্প ও বিজ্ঞান।

**ভালো Prompt-এর নিয়ম:**

1. **স্পষ্ট এবং নির্দিষ্ট হোন**
   - ❌ "Tell me about AI"
   - ✅ "Explain artificial intelligence in 3 paragraphs for a 10-year-old"

2. **রোল দিন (Role-Playing)**
   - "Act as a expert data scientist. Explain SVM in simple terms."

3. **কনটেক্সট দিন**
   - "Context: This is a customer support chat. Answer professionally."

4. **ফরম্যাট উল্লেখ করুন**
   - "Output as JSON: {'name': ..., 'age': ...}"

5. **Few-shot উদাহরণ দিন**
   - "Here are 2 examples: ... Now do this: ..."

6. **Chain-of-Thought ব্যবহার করুন**
   - "Let's think step by step"

7. **সীমাবদ্ধতা দিন**
   - "Keep response under 100 words. Do not mention politics."

8. **ইটারেট করুন** – প্রথম উত্তরে ভালো না হলে Prompt পরিবর্তন করুন

```python
# Poor Prompt
"Tell me about machine learning"

# Good Prompt
"""
You are a senior ML engineer with 10 years of experience. 
Explain what is machine learning to a beginner who knows basic Python.
Use simple analogies.
Keep it under 150 words.
Format: 2 paragraphs.
"""
```

---

## 🎯 LLM ইন্টারভিউ প্রস্তুতির জন্য অতিরিক্ত টিপস

1. **Hands-on Practice:** Hugging Face, OpenAI API, LangChain নিয়ে কাজ করুন
2. **Tokenization খেলুন:** বিভিন্ন টোকেনাইজার চেষ্টা করুন (GPT, BERT, LLaMA)
3. **Embedding Visualize করুন:** t-SNE বা PCA দিয়ে এম্বেডিং প্লট করুন
4. **RAG প্রজেক্ট করুন:** নিজের PDF ডকুমেন্ট নিয়ে RAG তৈরি করুন
5. **Latest Research পড়ুন:** Attention Is All You Need, GPT-3 Paper, BERT Paper
6. **Fine-tuning চেষ্টা করুন:** ছোট ডেটাসেটে BERT/GPT-2 ফাইন-টিউন করুন

---

## 🔚 শেষ কথা

**LLM, Token, এবং Embedding** – এই তিনটি কনসেপ্ট হলো আধুনিক Generative AI-এর ভিত্তি। Tokenization ছাড়া মডেল টেক্সট বুঝতে পারে না, Embedding ছাড়া অর্থ বুঝতে পারে না, আর LLM ছাড়া জেনারেট করতে পারে না।

**আপনার পরবর্তী স্টেপ:**
1. Hugging Face Transformers দিয়ে খেলুন
2. OpenAI API ব্যবহার করে অ্যাপ বানান
3. RAG প্রজেক্ট তৈরি করুন
4. LangChain শিখুন

যদি আরও গভীরে যেতে চান (যেমন: Fine-tuning, Quantization, LoRA, RLHF), তাহলে জানাবেন। শুভকামনা আপনার ইন্টারভিউয়ের জন্য! 🚀

