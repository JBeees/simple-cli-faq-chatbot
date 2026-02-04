# Semantic-Similarity FAQ Chatbot (CLI)

A simple FAQ chatbot that runs in the terminal (CLI) and answers user questions **only based on a predefined FAQ file**.  
The chatbot uses **semantic similarity** with sentence embeddings from Hugging Face to handle variations in natural language questions.

---

## 📌 Project Description

This project implements a **context-based FAQ chatbot** using a transformer-based NLP model.  
Instead of matching questions using exact string comparison (if–else), the chatbot measures **semantic similarity** between user input and FAQ questions.

If the user's question is not semantically similar to any FAQ entry, the chatbot will respond with a fallback message.

---
