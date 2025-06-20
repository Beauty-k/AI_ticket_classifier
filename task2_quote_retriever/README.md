# Task 2: Quote Retriever – AI Internship Assignment

Hello!
This is my solution to **Task 2** of the AI Dev Internship assignment.  
It's a simple but powerful system that retrieves **motivational quotes** based on what the user is feeling or searching for.

---

## Objective

Build a system that:
- Accepts **natural language queries** like _"motivation for exams"_
- Returns the **most semantically similar quotes**
- Uses modern **sentence embedding models** (e.g., MiniLM)
- Follows **clean, modular OOP principles**

---

## How It Works

1. **Quotes are loaded** from a local list (or can be extended to load from Hugging Face).
2. Quotes are embedded using **Sentence Transformers** (`all-MiniLM-L6-v2`).
3. At runtime, a user query is embedded and **compared with all quote vectors** using **cosine similarity**.
4. The top-k most relevant quotes are returned.

---


