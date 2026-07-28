চমৎকার! আমরা এখন আসছি **RAG (Retrieval-Augmented Generation)** এবং **ChromaDB (Vector Database)**-এর জগতে – যা বর্তমান Generative AI-এর **সবচেয়ে গুরুত্বপূর্ণ এবং প্র্যাকটিক্যাল** টপিকগুলোর মধ্যে অন্যতম। 

আমি এখন **দিন ২৮ (RAG)** এবং **দিন ২৯ (ChromaDB)** – দুটোই বিস্তারিত বাংলায় ব্যাখ্যা করব, তারপর **২০টি ইন্টারভিউ প্রশ্ন ও উত্তর** দেব।

---

# Day 28: RAG (Retrieval-Augmented Generation)

---

## 🤔 RAG কী এবং কেন দরকার?

**RAG (Retrieval-Augmented Generation)** হলো একটি কৌশল যেখানে LLM-কে **বাইরের ডেটাসোর্স** (ডকুমেন্ট, ডেটাবেস, ওয়েব) থেকে **প্রাসঙ্গিক তথ্য খুঁজে এনে** তারপর সেই তথ্যের ভিত্তিতে উত্তর জেনারেট করতে বলা হয়।

### কেন RAG দরকার?

| LLM-এর সমস্যা | RAG-এর সমাধান |
|---------------|----------------|
| **Hallucination** (মিথ্যা তথ্য) | ডকুমেন্ট থেকে তথ্য এনে উত্তর দেয় → নির্ভুলতা বাড়ে |
| **Knowledge Cutoff** (পুরনো জ্ঞান) | বর্তমান ডেটা দিয়ে উত্তর দিতে পারে |
| **Private Data** (কোম্পানির ডেটা) | কোম্পানির ডকুমেন্ট অ্যাক্সেস করতে পারে |
| **Fine-tuning ছাড়া** | নতুন ডেটাতে মডেল পুনরায় ট্রেইন করতে হয় না |
| **Costly** | Fine-tuning-এর চেয়ে সস্তা |
| **Transparency** | কোন ডকুমেন্ট থেকে উত্তর এলো, তা দেখানো যায় |

---

## 🏗️ RAG-এর Architecture

RAG-এর মূল আর্কিটেকচার দুটি প্রধান অংশে বিভক্ত:

### 1. Indexing Phase (ইনডেক্সিং ফেজ) – অফলাইন

```
Raw Documents → Load → Split (Chunk) → Embed → Store (Vector DB)
```

### 2. Retrieval & Generation Phase (রিট্রিভাল ও জেনারেশন ফেজ) – অনলাইন

```
User Query → Embed → Vector Search → Relevant Chunks → Prompt → LLM → Answer
```

```
User Query
    ↓
[1. Retrieve] → Vector Database → Relevant Documents
    ↓
[2. Augment] → Prompt = Context + Query
    ↓
[3. Generate] → LLM → Final Answer
```

---

## 📝 RAG-এর Complete Pipeline (LangChain সহ)

### Step 1: Document Loading (ডকুমেন্ট লোড করা)

```python
from langchain_community.document_loaders import PyPDFLoader, TextLoader, WebBaseLoader

# PDF থেকে
pdf_loader = PyPDFLoader("knowledge_base.pdf")
docs = pdf_loader.load()

# Text file থেকে
txt_loader = TextLoader("data.txt")
docs = txt_loader.load()

# Website থেকে
web_loader = WebBaseLoader("https://example.com")
docs = web_loader.load()
```

### Step 2: Splitting/Chunking (টুকরো টুকরো করা)

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,        # প্রতি চাঙ্কে ৫০০ অক্ষর
    chunk_overlap=50,      # ওভারল্যাপ (প্রসঙ্গ ধরে রাখতে)
    separators=["\n\n", "\n", " ", ""],
    length_function=len
)

chunks = text_splitter.split_documents(docs)
print(f"Total chunks: {len(chunks)}")
```

**Chunk Size কেন গুরুত্বপূর্ণ?**
- খুব বড় চাঙ্ক → অনেক তথ্য, কিন্তু প্রাসঙ্গিক অংশ খুঁজে পাওয়া কঠিন
- খুব ছোট চাঙ্ক → প্রসঙ্গ হারিয়ে যায়
- **Best Practice:** 500-1000 টোকেন

### Step 3: Embedding Creation (এম্বেডিং তৈরি)

```python
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

# OpenAI (Paid)
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

# Open Source (Free)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# প্রতিটি চাঙ্কের এম্বেডিং
# (ভেক্টর ডেটাবেসে স্টোর করার সময় auto-matically হয়)
```

### Step 4: Vector Store (ChromaDB)

```python
from langchain_community.vectorstores import Chroma

# ChromaDB তৈরি
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"  # ডিস্কে সেভ
)

# persist (সেভ)
vectorstore.persist()
```

### Step 5: Retrieval (খুঁজে বের করা)

```python
# Retriever তৈরি
retriever = vectorstore.as_retriever(
    search_type="similarity",  # বা "mmr" (Maximal Marginal Relevance)
    search_kwargs={"k": 4}     # টপ ৪টি ডকুমেন্ট
)

# Query করা
query = "What is machine learning?"
relevant_docs = retriever.get_relevant_documents(query)

for doc in relevant_docs:
    print(f"Source: {doc.metadata.get('source', 'Unknown')}")
    print(f"Content: {doc.page_content[:200]}...\n")
```

### Step 6: Generation (উত্তর তৈরি)

```python
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough

# Prompt Template
template = """
You are a helpful assistant. Answer the question based ONLY on the following context:

Context:
{context}

Question: {question}

Answer (be concise and accurate):
"""

prompt = ChatPromptTemplate.from_template(template)

# LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# RAG Chain (LCEL)
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
)

# Query
query = "What is machine learning?"
response = rag_chain.invoke(query)
print(response.content)
```

---

## 🧠 RAG-এর বিভিন্ন Strategy

### 1. Stuff (সব একসাথে)

```python
from langchain.chains.combine_documents import create_stuff_documents_chain

# সব ডকুমেন্টকে এক প্রম্পটে "stuff" করে
stuff_chain = create_stuff_documents_chain(llm, prompt)
```

**সুবিধা:** দ্রুত  
**অসুবিধা:** কনটেক্সট উইন্ডো লিমিট

---

### 2. Map-Reduce (প্রতিটি আলাদা + মিলিয়ে)

```python
from langchain.chains import MapReduceDocumentsChain

# Map: প্রতিটি ডকুমেন্ট আলাদাভাবে প্রসেস
# Reduce: সব রেজাল্ট একত্রিত করে
```

**সুবিধা:** লম্বা ডকুমেন্টের জন্য  
**অসুবিধা:** অনেক API কল, ধীর

---

### 3. Refine (ধীরে ধীরে আপডেট)

```python
from langchain.chains import RefineDocumentsChain

# প্রথম ডকুমেন্ট দিয়ে শুরু → পরের ডকুমেন্ট দিয়ে রিফাইন
```

**সুবিধা:** সবচেয়ে ভালো মানের আউটপুট  
**অসুবিধা:** সবচেয়ে ধীর

---

### 4. HyDE (Hypothetical Document Embedding)

```python
# প্রশ্ন থেকে "হাইপোথেটিক্যাল" উত্তর তৈরি করে
# তারপর সেই উত্তর দিয়ে সার্চ
```

**সুবিধা:** প্রশ্ন এবং ডকুমেন্টের মধ্যে সিমিলারিটি গ্যাপ কমায়

---

## 🛠️ Advanced RAG Techniques

### 1. Multi-Query Retrieval

```python
from langchain.retrievers.multi_query import MultiQueryRetriever

# একই প্রশ্নের একাধিক ভার্সন তৈরি করে সার্চ
retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(),
    llm=llm
)
```

### 2. Self-Query Retrieval (মেটাডেটা ফিল্টার)

```python
from langchain.retrievers.self_query.base import SelfQueryRetriever

# প্রশ্ন থেকে মেটাডেটা ফিল্টার বের করে
# যেমন: "2023 সালের ডকুমেন্ট থেকে..." 
```

### 3. Parent Document Retriever

```python
from langchain.retrievers import ParentDocumentRetriever

# ছোট চাঙ্কে সার্চ, বড় চাঙ্ক রিটার্ন
# ছোট = স্পেসিফিক সার্চ, বড় = সম্পূর্ণ কনটেক্সট
```

### 4. Ensemble Retriever

```python
from langchain.retrievers import EnsembleRetriever

# একাধিক রিট্রিভারের রেজাল্ট একত্রিত করে
ensemble = EnsembleRetriever(
    retrievers=[retriever1, retriever2],
    weights=[0.5, 0.5]
)
```

---

## 🧪 Complete RAG Example (End-to-End)

```python
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

# 1. Load Documents
loader = PyPDFLoader("machine_learning_book.pdf")
docs = loader.load()

# 2. Split
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# 3. Embed & Store
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory="./chroma_db")
vectorstore.persist()

# 4. Retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# 5. Prompt
template = """
Context: {context}

Question: {question}

Instructions:
- Answer based ONLY on the context.
- If the answer is not in the context, say "I don't know."
- Be concise and accurate.

Answer:
"""
prompt = ChatPromptTemplate.from_template(template)

# 6. LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 7. RAG Chain
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 8. Query
while True:
    query = input("\n🔍 Ask a question (or 'quit'): ")
    if query.lower() == 'quit':
        break
    
    response = rag_chain.invoke(query)
    print(f"🤖 Answer: {response}")
```

---

# Day 29: ChromaDB (Vector Database)

---

## 🗄️ ChromaDB কী?

**ChromaDB** হলো একটি **ওপেন-সোর্স ভেক্টর ডেটাবেস** যা এম্বেডিং (embedding) সংরক্ষণ করে এবং **সিমিলারিটি সার্চ** (অর্থ অনুসারে খোঁজ) করতে পারে। এটি RAG অ্যাপ্লিকেশনের জন্য বিশেষভাবে ডিজাইন করা হয়েছে।

**ChromaDB-এর বৈশিষ্ট্য:**
- **Lightweight & Easy** – ব্যবহার করা খুব সহজ
- **In-memory বা Persistent** – RAM বা ডিস্কে সেভ করা যায়
- **Metadata Filtering** – ডকুমেন্টের মেটাডেটা দিয়ে ফিল্টার
- **LangChain Integration** – LangChain-এর সাথে সহজেই কাজ করে
- **Open Source** – ফ্রি, সেলফ-হোস্টেড

---

## 📦 ChromaDB ইনস্টলেশন

```bash
pip install chromadb
```

```python
import chromadb
from chromadb.config import Settings

# 1. In-Memory (RAM-এ, ডিস্কে সেভ হবে না)
client = chromadb.Client()

# 2. Persistent (ডিস্কে সেভ)
client = chromadb.PersistentClient(path="./chroma_db")
```

---

## 🏗️ ChromaDB-এর Basic Operations

### 1. Collection তৈরি করা

```python
# Collection = SQL-এর TABLE-এর মতো
collection = client.create_collection(
    name="my_docs",
    metadata={"hnsw:space": "cosine"}  # সিমিলারিটি মেট্রিক
)

# Collection তালিকা
collections = client.list_collections()

# Collection ডিলিট
client.delete_collection("my_docs")
```

### 2. Documents যোগ করা (Add)

```python
# Directly
collection.add(
    documents=[
        "Machine learning is a subset of AI.",
        "Python is a programming language.",
        "Deep learning uses neural networks."
    ],
    metadatas=[
        {"source": "wiki", "topic": "AI"},
        {"source": "wiki", "topic": "programming"},
        {"source": "book", "topic": "AI"}
    ],
    ids=["doc1", "doc2", "doc3"]
)

# LangChain Document থেকে
from langchain_community.vectorstores import Chroma

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="my_docs",
    persist_directory="./chroma_db"
)
```

### 3. Query (সার্চ করা)

```python
# Basic Query
results = collection.query(
    query_texts=["What is machine learning?"],
    n_results=2  # টপ ২টি ফলাফল
)

print(results['documents'])  # ডকুমেন্টগুলো
print(results['distances'])  # দূরত্ব (0 = সবচেয়ে কাছাকাছি)
print(results['metadatas'])  # মেটাডেটা
print(results['ids'])        # আইডি

# Metadata Filter সহ Query
results = collection.query(
    query_texts=["What is AI?"],
    n_results=3,
    where={"source": "wiki"},  # শুধু "wiki" সোর্সের ডকুমেন্ট
    where_document={"$contains": "learning"}  # ডকুমেন্টে "learning" থাকতে হবে
)
```

### 4. Update & Delete

```python
# Update
collection.update(
    ids=["doc1"],
    documents=["Machine learning is a field of AI."],
    metadatas=[{"source": "updated"}]
)

# Delete
collection.delete(ids=["doc1"])

# Get all documents
all_docs = collection.get()

# Count
count = collection.count()
```

---

## 📊 ChromaDB-এর Advanced Features

### 1. Filter Operators

```python
# Metadata Filter
results = collection.query(
    query_texts=["AI"],
    where={
        "$and": [
            {"source": {"$in": ["wiki", "book"]}},
            {"year": {"$gt": 2020}}
        ]
    }
)

# Available Operators
# $eq, $ne, $gt, $gte, $lt, $lte, $in, $nin
```

### 2. Embedding Function Customization

```python
from chromadb.utils import embedding_functions

# OpenAI
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key="sk-...",
    model_name="text-embedding-ada-002"
)

# Sentence Transformers (Open Source)
sentence_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Collection with custom embedding
collection = client.create_collection(
    name="my_docs",
    embedding_function=sentence_ef
)
```

### 3. Batch Processing

```python
# Batch Add (বড় ডেটার জন্য)
batch_size = 100
for i in range(0, len(documents), batch_size):
    batch = documents[i:i+batch_size]
    collection.add(
        documents=batch,
        ids=[f"doc_{j}" for j in range(i, i+len(batch))]
    )
```

---

## 🧠 ChromaDB with LangChain (Complete RAG Setup)

```python
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# 1. Load & Split
loader = PyPDFLoader("document.pdf")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# 2. Create Vector Store
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db",
    collection_name="my_knowledge_base"
)

# 3. Persist
vectorstore.persist()

# 4. Load Existing Vector Store
loaded_vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings,
    collection_name="my_knowledge_base"
)

# 5. Retriever
retriever = loaded_vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}
)

# 6. Query
results = retriever.get_relevant_documents("What is AI?")
for doc in results:
    print(doc.page_content)
```

---

## 📊 ChromaDB vs Other Vector Databases

| Feature | ChromaDB | Pinecone | Weaviate | Qdrant | FAISS |
|---------|----------|----------|----------|--------|-------|
| **Open Source** | ✅ | ❌ | ✅ | ✅ | ✅ |
| **Self-hosted** | ✅ | ❌ | ✅ | ✅ | ✅ |
| **Cloud Option** | ❌ | ✅ | ✅ | ✅ | ❌ |
| **Metadata Filter** | ✅ | ✅ | ✅ | ✅ | ❌ |
| **LangChain Support** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Ease of Use** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Production Ready** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| **Use Case** | Prototype, Small | Enterprise | Enterprise | Enterprise | Research |

---

## 🚀 ChromaDB-র Best Practices

### 1. Chunking Strategy

```python
# Overlap গুরুত্বপূর্ণ
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,  # 10-20% overlap
    separators=["\n\n", "\n", ". ", " ", ""]
)
```

### 2. Metadata Management

```python
metadatas = [
    {
        "source": "document.pdf",
        "page": 10,
        "section": "Chapter 3",
        "date": "2024-01-01"
    }
]

# Metadata Filtering দিয়ে প্রাসঙ্গিক ডকুমেন্ট খুঁজুন
results = collection.query(
    query_texts=["AI"],
    where={"source": "document.pdf", "page": {"$gt": 5}}
)
```

### 3. Distance Metrics

```python
# Chroma-তে ৩টি distance metric সাপোর্ট করে
# 1. cosine (ডিফল্ট)
# 2. l2 (Euclidean)
# 3. ip (Inner Product)

collection = client.create_collection(
    name="my_docs",
    metadata={"hnsw:space": "cosine"}  # বা "l2", "ip"
)
```

### 4. Index Optimization

```python
# HNSW (Hierarchical Navigable Small World) index
# HNSW-র parameters:
collection = client.create_collection(
    name="my_docs",
    metadata={
        "hnsw:space": "cosine",
        "hnsw:construction_ef": 200,  # ইনডেক্স বিল্ড কোয়ালিটি (100-500)
        "hnsw:M": 32                  # ম্যাক্স ডিগ্রি (16-64)
    }
)
```

---

## 📝 Complete RAG + ChromaDB Project

```python
import os
from dotenv import load_dotenv
load_dotenv()

import chromadb
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

class RAGSystem:
    def __init__(self, persist_dir="./chroma_db"):
        self.persist_dir = persist_dir
        self.embeddings = OpenAIEmbeddings()
        self.llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        self.vectorstore = None
        self.retriever = None
        
    def load_documents(self, file_paths):
        """Load documents from various sources"""
        all_docs = []
        for path in file_paths:
            if path.endswith('.pdf'):
                loader = PyPDFLoader(path)
            else:
                loader = TextLoader(path)
            all_docs.extend(loader.load())
        return all_docs
    
    def create_vectorstore(self, documents, collection_name="knowledge_base"):
        """Create vector store from documents"""
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        chunks = splitter.split_documents(documents)
        
        self.vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=self.persist_dir,
            collection_name=collection_name
        )
        self.vectorstore.persist()
        self.retriever = self.vectorstore.as_retriever(
            search_kwargs={"k": 4}
        )
        print(f"✅ Created vector store with {len(chunks)} chunks")
    
    def load_vectorstore(self, collection_name="knowledge_base"):
        """Load existing vector store"""
        self.vectorstore = Chroma(
            persist_directory=self.persist_dir,
            embedding_function=self.embeddings,
            collection_name=collection_name
        )
        self.retriever = self.vectorstore.as_retriever(
            search_kwargs={"k": 4}
        )
        print(f"✅ Loaded vector store with {self.vectorstore._collection.count()} documents")
    
    def query(self, question):
        """Query the RAG system"""
        if not self.retriever:
            return "⚠️ Please load or create a vector store first."
        
        template = """
        You are a helpful assistant. Answer the question based ONLY on the following context:
        
        Context:
        {context}
        
        Question: {question}
        
        Instructions:
        - If the context doesn't contain the answer, say "I don't have enough information."
        - Be concise and accurate.
        - Use bullet points if helpful.
        
        Answer:
        """
        
        prompt = ChatPromptTemplate.from_template(template)
        
        rag_chain = (
            {"context": self.retriever, "question": RunnablePassthrough()}
            | prompt
            | self.llm
            | StrOutputParser()
        )
        
        return rag_chain.invoke(question)
    
    def add_documents(self, documents):
        """Add new documents to existing vector store"""
        if not self.vectorstore:
            return "⚠️ No vector store exists. Create one first."
        
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(documents)
        self.vectorstore.add_documents(chunks)
        self.vectorstore.persist()
        print(f"✅ Added {len(chunks)} new chunks")

# Usage
rag = RAGSystem()

# Load documents
docs = rag.load_documents(["data.pdf", "knowledge.txt"])

# Create vector store
rag.create_vectorstore(docs)

# Query
response = rag.query("What is machine learning?")
print(response)
```

---

# 📋 RAG & ChromaDB – ২০টি ইন্টারভিউ প্রশ্ন ও উত্তর

---

### **প্রশ্ন ১: RAG (Retrieval-Augmented Generation) কী? কেন প্রয়োজন?**

**উত্তর:**

**RAG** হলো একটি কৌশল যেখানে LLM-কে **বাইরের ডেটাসোর্স** থেকে প্রাসঙ্গিক ডকুমেন্ট খুঁজে এনে তার ভিত্তিতে উত্তর তৈরি করতে বলা হয়।

**কেন প্রয়োজন:**
1. **Hallucination কমানো** – মডেলকে রেফারেন্স দিয়ে উত্তর দিতে বাধ্য করা
2. **Private/Enterprise Data** – কোম্পানির নিজস্ব ডেটা অ্যাক্সেস
3. **Up-to-date Information** – মডেলের Knowledge Cutoff পার হওয়া
4. **No Fine-tuning Required** – নতুন ডেটাতে মডেল পুনরায় ট্রেইন করতে হয় না
5. **Cost-effective** – Fine-tuning-এর চেয়ে সস্তা

---

### **প্রশ্ন ২: RAG-এর দুটি প্রধান ফেজ কী কী?**

**উত্তর:**

RAG-এর দুটি প্রধান ফেজ:

| ফেজ | কাজ | অফলাইন/অনলাইন |
|-----|-----|---------------|
| **Indexing (ইনডেক্সিং)** | ডকুমেন্ট → লোড → স্প্লিট → এম্বেড → ভেক্টর ডেটাবেসে স্টোর | **অফলাইন** (একবার করে ফেলতে হয়) |
| **Retrieval & Generation (রিট্রিভাল ও জেনারেশন)** | প্রশ্ন → এম্বেড → ভেক্টর সার্চ → প্রাসঙ্গিক ডকুমেন্ট → প্রম্পট → LLM → উত্তর | **অনলাইন** (প্রতি প্রশ্নে) |

```
Indexing Phase:
Raw Data → Load → Split → Embed → Store (Vector DB)

Retrieval & Generation Phase:
Query → Embed → Search → Retrieve → Prompt → LLM → Answer
```

---

### **প্রশ্ন ৩: RAG এবং Fine-tuning-এর মধ্যে পার্থক্য কী?**

**উত্তর:**

| Feature | RAG | Fine-tuning |
|---------|-----|-------------|
| **Data Integration** | ডাইনামিক (যেকোনো সময় ডেটা যোগ করা যায়) | স্ট্যাটিক (ডেটা যোগ করতে পুনরায় ট্রেইন করতে হবে) |
| **Cost** | সস্তা (vector search + LLM call) | ব্যয়বহুল (GPU, time) |
| **Up-to-date** | বর্তমান ডেটা দিয়ে কাজ করতে পারে | Knowledge Cutoff থাকে |
| **Hallucination** | কম (ডকুমেন্ট রেফারেন্স দিয়ে) | বেশি (মডেল নিজে থেকে তৈরি করে) |
| **Transparency** | কোন ডকুমেন্ট থেকে এলো, দেখানো যায় | ব্ল্যাকবক্স |
| **Latency** | ধীর (search + generate) | দ্রুত (শুধু generate) |
| **Use Case** | Private data, FAQs, Customer support | Specific tone/style, Domain expertise |

---

### **প্রশ্ন ৪: RAG-এ Chunking (টুকরো করা) কেন গুরুত্বপূর্ণ?**

**উত্তর:**

**Chunking** হলো বড় ডকুমেন্টকে ছোট ছোট টুকরোতে ভাগ করা। এটি গুরুত্বপূর্ণ কারণ:
1. **Context Window Limit** – মডেল একবারে সীমিত টোকেন নিতে পারে
2. **Relevance** – ছোট চাঙ্কে সার্চ করলে বেশি প্রাসঙ্গিক ফলাফল পাওয়া যায়
3. **Semantic Coherence** – প্রতিটি চাঙ্ক একটি সম্পূর্ণ ধারণা ধারণ করে

**Best Practices:**
- **Chunk Size:** 500-1000 টোকেন (আপনার ইউজ কেস অনুযায়ী)
- **Overlap:** 10-20% (প্রসঙ্গ ধরে রাখতে)
- **Separators:** Paragraph (`\n\n`), Sentence (`.`), Word (` `)

```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", ". ", " ", ""]
)
```

---

### **প্রশ্ন ৫: RAG-এ Embedding কী ভূমিকা পালন করে?**

**উত্তর:**

**Embedding** হলো টেক্সটকে **সংখ্যার ভেক্টরে** রূপান্তর করা – যা কম্পিউটার বুঝতে পারে এবং তুলনা করতে পারে।

**RAG-এ Embedding-এর ভূমিকা:**
1. **Indexing Phase:** ডকুমেন্টের চাঙ্কগুলোর এম্বেডিং তৈরি করে ভেক্টর ডেটাবেসে স্টোর করা
2. **Retrieval Phase:** প্রশ্নের এম্বেডিং তৈরি করে এবং ডেটাবেসের সাথে তুলনা করে সবচেয়ে কাছাকাছি চাঙ্ক খোঁজা
3. **Similarity Search:** Cosine Similarity দিয়ে অর্থ অনুসারে ডকুমেন্ট খোঁজা

```python
# Query Embedding → Vector Search
query_embedding = embeddings.embed_query("What is AI?")
results = vectorstore.similarity_search_by_vector(query_embedding)
```

---

### **প্রশ্ন ৬: RAG-এর Main Components কী কী?**

**উত্তর:**

RAG-এর ৫টি Main Component:

| কম্পোনেন্ট | কাজ |
|------------|-----|
| **Document Loader** | বিভিন্ন সোর্স (PDF, CSV, Web) থেকে ডকুমেন্ট লোড করা |
| **Text Splitter** | ডকুমেন্টকে ছোট ছোট চাঙ্কে ভাগ করা |
| **Embeddings** | টেক্সটকে ভেক্টরে রূপান্তর করা |
| **Vector Store** | এম্বেডিং সংরক্ষণ এবং সিমিলারিটি সার্চ করা |
| **LLM** | প্রাসঙ্গিক চাঙ্ক + প্রশ্ন → উত্তর জেনারেট করা |

```python
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import ChatOpenAI
```

---

### **প্রশ্ন ৭: Vector Database কী? ChromaDB এর সাথে অন্য Vector DB-এর পার্থক্য কী?**

**উত্তর:**

**Vector Database** হলো একটি ডেটাবেস যা **এম্বেডিং ভেক্টর** সংরক্ষণ করে এবং **সিমিলারিটি সার্চ** (অর্থ অনুসারে খোঁজ) করতে পারে।

**ChromaDB বনাম অন্যান্য:**

| Feature | ChromaDB | Pinecone | Weaviate | Qdrant | FAISS |
|---------|----------|----------|----------|--------|-------|
| **Open Source** | ✅ | ❌ | ✅ | ✅ | ✅ |
| **Self-hosted** | ✅ | ❌ | ✅ | ✅ | ✅ |
| **Metadata Filter** | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Ease of Use** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Production Ready** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| **Best For** | Prototype, Small | Enterprise | Enterprise | Enterprise | Research |

---

### **প্রশ্ন ৮: ChromaDB-তে Collection কী?**

**উত্তর:**

**Collection** হলো ChromaDB-তে SQL-এর **Table**-এর মতো। এটি এম্বেডিং ডকুমেন্টগুলোর একটি গ্রুপ যা একসাথে সংরক্ষিত থাকে।

```python
# Collection তৈরি
collection = client.create_collection(
    name="my_docs",
    metadata={"hnsw:space": "cosine"}
)

# Collection তালিকা
collections = client.list_collections()

# Collection ডিলিট
client.delete_collection("my_docs")
```

প্রতিটি Collection-এর নিজস্ব:
- **Embedding Function** (যেমন: OpenAI, Sentence Transformers)
- **Distance Metric** (cosine, l2, ip)
- **Metadata Schema**

---

### **প্রশ্ন ৯: ChromaDB-তে Metadata Filtering কীভাবে কাজ করে?**

**উত্তর:**

**Metadata Filtering** দিয়ে আপনি ডকুমেন্টের মেটাডেটা (যেমন: source, date, author) এর ভিত্তিতে সার্চ ফলাফল ফিল্টার করতে পারেন।

```python
# Metadata Filtering
results = collection.query(
    query_texts=["AI"],
    where={
        "source": "document.pdf",           # exact match
        "year": {"$gt": 2020},              # greater than
        "author": {"$in": ["John", "Jane"]} # in list
    }
)

# Available Operators
# $eq, $ne, $gt, $gte, $lt, $lte, $in, $nin
```

**Use Case:** "2023 সালের পরে লেখা ডকুমেন্ট থেকে AI সম্পর্কে জানো"

---

### **প্রশ্ন ১০: ChromaDB-তে Persistent এবং In-Memory মোডের মধ্যে পার্থক্য কী?**

**উত্তর:**

| মোড | বর্ণনা | ব্যবহার |
|------|--------|----------|
| **In-Memory** | RAM-এ ডেটা থাকে, অ্যাপ বন্ধ হলে ডেটা হারিয়ে যায় | Prototype, Testing |
| **Persistent** | ডিস্কে ডেটা সেভ থাকে, অ্যাপ বন্ধ করলেও থাকে | Production |

```python
# In-Memory (সব RAM-এ)
client = chromadb.Client()

# Persistent (ডিস্কে সেভ)
client = chromadb.PersistentClient(path="./chroma_db")

# Persistent-এর সুবিধা:
# 1. ডেটা পুনরায় এম্বেড করতে হয় না
# 2. অ্যাপ রিস্টার্ট করলেও ডেটা থাকে
# 3. বড় ডেটাসেটের জন্য ভালো
```

---

### **প্রশ্ন ১১: ChromaDB-তে Distance Metrics কী কী?**

**উত্তর:**

ChromaDB ৩টি Distance Metric সাপোর্ট করে:

| Metric | সূত্র | ভালো ব্যবহার |
|--------|-------|--------------|
| **Cosine** | `cosine = 1 - (A·B)/(||A||·||B||)` | টেক্সট সিমিলারিটি (ডিফল্ট) |
| **L2 (Euclidean)** | `distance = √(Σ(Ai - Bi)²)` | যখন ভেক্টর দৈর্ঘ্য গুরুত্বপূর্ণ |
| **IP (Inner Product)** | `ip = -A·B` | যখন ম্যাগনিটিউড গুরুত্বপূর্ণ |

```python
# Cosine (ডিফল্ট, টেক্সটের জন্য সেরা)
collection = client.create_collection(
    name="my_docs",
    metadata={"hnsw:space": "cosine"}
)

# L2
collection = client.create_collection(
    name="my_docs",
    metadata={"hnsw:space": "l2"}
)
```

---

### **প্রশ্ন ১২: HyDE (Hypothetical Document Embedding) কী?**

**উত্তর:**

**HyDE** হলো একটি RAG কৌশল যেখানে:
1. প্রশ্ন থেকে একটি **হাইপোথেটিক্যাল (কল্পিত) উত্তর** তৈরি করা হয়
2. এই উত্তরটির এম্বেডিং তৈরি করা হয়
3. এই এম্বেডিং দিয়ে ভেক্টর ডেটাবেসে সার্চ করা হয়

**কেন HyDE?**
- প্রশ্ন এবং ডকুমেন্টের মধ্যে **Semantic Gap** কমায়
- প্রশ্ন ছোট হলে ভালো ফলাফল দেয়
- বিশেষ করে "How", "Why" টাইপ প্রশ্নের জন্য

```python
# HyDE Implementation
hypothetical_answer = llm.generate(f"Answer this briefly: {query}")
query_embedding = embeddings.embed_query(hypothetical_answer)
results = vectorstore.similarity_search_by_vector(query_embedding)
```

---

### **প্রশ্ন ১৩: Multi-Query Retrieval কী?**

**উত্তর:**

**Multi-Query Retrieval** হলো একই প্রশ্নের **একাধিক ভিন্ন ভিন্ন ভার্সন** তৈরি করে (প্রম্পট পরিবর্তন করে) এবং সবগুলো দিয়ে সার্চ করে রেজাল্ট একত্রিত করা।

```python
from langchain.retrievers.multi_query import MultiQueryRetriever

retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(),
    llm=llm
)

# MultiQueryRetriever ৫টি ভিন্নভাবে প্রশ্ন তৈরি করে
# যেমন: 
# 1. "What is machine learning?"
# 2. "Define machine learning"
# 3. "Explain ML"
# 4. "What does machine learning mean?"
# 5. "Tell me about machine learning"
```

**সুবিধা:** বিভিন্নভাবে প্রশ্ন করলে বেশি প্রাসঙ্গিক ডকুমেন্ট পাওয়া যায়  
**অসুবিধা:** বেশি API কল, ধীর

---

### **প্রশ্ন ১৪: Parent Document Retriever কী?**

**উত্তর:**

**Parent Document Retriever** হলো এমন একটি কৌশল যেখানে:
1. **ছোট চাঙ্কে** সার্চ করা হয় (স্পেসিফিক)
2. কিন্তু **বড় প্যারেন্ট ডকুমেন্ট** রিটার্ন করা হয় (সম্পূর্ণ কনটেক্সট)

```python
from langchain.retrievers import ParentDocumentRetriever
from langchain.storage import InMemoryStore

# ছোট চাঙ্ক (সার্চের জন্য)
child_splitter = RecursiveCharacterTextSplitter(chunk_size=200)
# বড় চাঙ্ক (কনটেক্সটের জন্য)
parent_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)

retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=InMemoryStore(),
    child_splitter=child_splitter,
    parent_splitter=parent_splitter
)
```

**সুবিধা:** স্পেসিফিক সার্চ + সম্পূর্ণ কনটেক্সট, দুটোই পাওয়া যায়

---

### **প্রশ্ন ১৫: RAG-এ Similarity Search এবং MMR-এর মধ্যে পার্থক্য কী?**

**উত্তর:**

| Feature | Similarity Search | MMR (Maximal Marginal Relevance) |
|---------|-------------------|----------------------------------|
| **Goal** | সবচেয়ে কাছাকাছি ডকুমেন্ট খোঁজা | কাছাকাছি + ভিন্নতা (diversity) |
| **Result** | টপ Kটি ডকুমেন্ট (সব একই রকম হতে পারে) | ভিন্ন ভিন্ন ডকুমেন্ট |
| **Use Case** | প্রশ্নের সরাসরি উত্তর খোঁজা | একাধিক পerspective বা সোর্স চাইলে |

```python
# Similarity
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}
)

# MMR (সবচেয়ে কাছাকাছি + ভিন্নতা)
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 4, "fetch_k": 20}  # 20 টা থেকে 4 টা সিলেক্ট
)
```

---

### **প্রশ্ন ১৬: RAG-এ Context Window Limit কীভাবে হ্যান্ডেল করবেন?**

**উত্তর:**

Context Window Limit ম্যানেজ করার উপায়:

1. **Smaller Chunks** – চাঙ্ক সাইজ কমান (300-500 টোকেন)
2. **Less Retrieved Documents** – `k` কমান (3-4 ডকুমেন্ট)
3. **Summarization** – ডকুমেন্টগুলোর সারাংশ তৈরি করা
4. **Map-Reduce** – প্রতিটি ডকুমেন্ট আলাদা প্রসেস করা
5. **Refine** – ধীরে ধীরে কনটেক্সট তৈরি করা

```python
# Strategy 1: কম ডকুমেন্ট
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# Strategy 2: Summarization
from langchain.chains.summarize import load_summarize_chain
summary_chain = load_summarize_chain(llm, chain_type="stuff")
summary = summary_chain.run(docs)
```

---

### **প্রশ্ন ১৭: RAG-এ Hallucination কীভাবে কমানো যায়?**

**উত্তর:**

RAG-এ Hallucination কমানোর উপায়:

1. **Strong Prompt Engineering** – "শুধু কনটেক্সট থেকে উত্তর দাও"
2. **Re-ranking** – প্রাসঙ্গিক ডকুমেন্ট রি-র্যাঙ্ক করা
3. **Threshold Filtering** – খুব কম স্কোরের ডকুমেন্ট বাদ দেওয়া
4. **Citation** – উত্তরসহ ডকুমেন্ট সোর্স দেখানো
5. **Self-consistency** – একই প্রশ্ন একাধিকবার করে মিল চেক

```python
template = """
Answer the question BASED ONLY on the following context.
If the answer is not in the context, say "I don't have enough information."

Context: {context}
Question: {question}

Answer:
"""
```

---

### **প্রশ্ন ১৮: ChromaDB-তে HNSW Index কী?**

**উত্তর:**

**HNSW (Hierarchical Navigable Small World)** হলো ChromaDB-তে ব্যবহৃত একটি **Approximate Nearest Neighbor (ANN)** অ্যালগরিদম যা দ্রুত সিমিলারিটি সার্চ করতে সাহায্য করে।

**HNSW Parameters:**

| Parameter | কাজ | Recommendation |
|-----------|-----|----------------|
| `M` | প্রতিটি নোডের ম্যাক্স কানেকশন | 16-64 (ডিফল্ট 32) |
| `construction_ef` | ইনডেক্স বিল্ড কোয়ালিটি | 100-500 (ডিফল্ট 200) |
| `space` | Distance Metric | cosine, l2, ip |

```python
collection = client.create_collection(
    name="my_docs",
    metadata={
        "hnsw:space": "cosine",
        "hnsw:construction_ef": 200,
        "hnsw:M": 32
    }
)
```

**Trade-off:** বড় M এবং EF → ভালো সার্চ কোয়ালিটি → বেশি মেমোরি + ধীর ইনডেক্সিং

---

### **প্রশ্ন ১৯: RAG অ্যাপ্লিকেশনের Evaluation কীভাবে করবেন?**

**উত্তর:**

RAG Evaluation-এর জন্য কিছু মেট্রিক্স:

| Metric | কী মাপে |
|--------|---------|
| **Context Relevance** | রিট্রিভ করা ডকুমেন্ট কতটা প্রাসঙ্গিক |
| **Answer Faithfulness** | উত্তর কি কনটেক্সটের সাথে সামঞ্জস্যপূর্ণ |
| **Answer Relevance** | উত্তর কি প্রশ্নের সাথে প্রাসঙ্গিক |
| **Latency** | কত দ্রুত উত্তর আসে |
| **Ground Truth** | সঠিক উত্তর কতবার পাচ্ছে |

```python
# RAGAS Library ব্যবহার (RAG Evaluation)
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_relevancy

result = evaluate(
    dataset=dataset,
    metrics=[faithfulness, answer_relevancy, context_relevancy]
)
```

---

### **প্রশ্ন ২০: RAG + ChromaDB Production-এ ডেপ্লয় করার Best Practices কী?**

**উত্তর:**

Production RAG System-এর Best Practices:

1. **Persistent Storage** – ডিস্কে ভেক্টর ডেটাবেস সেভ করুন
2. **Batch Processing** – বড় ডেটা ব্যাচে প্রসেস করুন
3. **Caching** – একই প্রশ্ন বারবার না পাঠান
4. **Monitoring** – Latency, Accuracy, Cost Track করুন
5. **Fallback Mechanism** – কোনো ডকুমেন্ট না পেলে Generic উত্তর দিন
6. **Security** – API Key Secure রাখুন, User Data Privacy বজায় রাখুন

```python
# Production Setup
import logging
from functools import lru_cache

logging.basicConfig(level=logging.INFO)

class ProductionRAG:
    def __init__(self):
        self.vectorstore = Chroma(
            persist_directory="./prod_chroma_db",
            embedding_function=OpenAIEmbeddings()
        )
        self.cache = {}
    
    @lru_cache(maxsize=1000)
    def query(self, question):
        try:
            logging.info(f"Query: {question[:50]}...")
            response = self.rag_chain.invoke(question)
            logging.info(f"Response length: {len(response)}")
            return response
        except Exception as e:
            logging.error(f"Error: {e}")
            return "I'm having trouble answering right now."
```

---

## 🎯 ইন্টারভিউ প্রস্তুতির জন্য টিপস

1. **RAG Pipeline এর প্রতিটি স্টেপ হ্যান্ডস-অন করুন** – লোড, স্প্লিট, এম্বেড, স্টোর, রিট্রিভ, জেনারেট
2. **Chunking Strategy নিয়ে Experiment করুন** – সাইজ, ওভারল্যাপ, সেপারেটর
3. **Vector Database তুলনা করুন** – ChromaDB, Pinecone, Weaviate
4. **Advanced RAG Techniques জানুন** – HyDE, Multi-Query, Self-Query
5. **Evaluation জানুন** – RAGAS, Faithfulness, Context Relevancy

---

## 🔚 শেষ কথা

**RAG** এবং **ChromaDB** হলো Generative AI-র **সবচেয়ে প্র্যাকটিক্যাল** টপিক। আপনি যদি এই দুটি ভালোভাবে বুঝতে পারেন এবং নিজের প্রজেক্টে ইমপ্লিমেন্ট করতে পারেন, তাহলে যেকোনো AI ইন্টারভিউতে আপনি কনফিডেন্ট থাকবেন।

**আপনার পরবর্তী স্টেপ:**
1. LangChain + ChromaDB দিয়ে নিজের RAG প্রজেক্ট বানান
2. PDF ডকুমেন্ট বা ওয়েবসাইটের উপর RAG ইমপ্লিমেন্ট করুন
3. Advanced RAG Techniques (HyDE, Multi-Query) চেষ্টা করুন
4. RAGAS দিয়ে আপনার RAG System ইভ্যালুয়েট করুন

**শুভকামনা আপনার ইন্টারভিউয়ের জন্য! 🚀**

