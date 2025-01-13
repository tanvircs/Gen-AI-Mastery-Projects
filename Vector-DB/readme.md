# Vector Database Demo: ChromaDB, Pinecone, and Weaviate

This repository contains examples and workflows to demonstrate the use of vector databases (**ChromaDB**, **Pinecone**, and **Weaviate**) for document retrieval and integration with OpenAI's language models.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [ChromaDB Workflow](#chromadb-workflow)
- [Pinecone Workflow](#pinecone-workflow)
- [Weaviate Workflow](#weaviate-workflow)
- [Requirements](#requirements)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)

---

## Overview

This project demonstrates:
1. Document ingestion and text chunking.
2. Vector embeddings generation using OpenAI.
3. Vector database integration for similarity search and retrieval using:
   - [ChromaDB](https://www.trychroma.com/)
   - [Pinecone](https://www.pinecone.io/)
   - [Weaviate](https://weaviate.io/)
4. Integration with OpenAI's GPT models for query-based document retrieval and answering.

---

## Installation

Install the required packages:

```bash
pip install openai langchain tiktoken chromadb==0.4.15
pip install pinecone-client weaviate-client>=3.26.7,<4.0.0
pip install unstructured "unstructured[pdf]"
pip install langchain_community
```

## ChromaDB Workflow
### Steps:
1. Load Documents: Download and unzip a collection of text files to process.

```bash
from langchain.document_loaders import DirectoryLoader
loader = DirectoryLoader("/path/to/text/files", glob="./*.txt")
documents = loader.load()
```

2. Split Documents: Split the documents into smaller chunks for efficient embedding.
```bash
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
text_chunks = text_splitter.split_documents(documents)
```

3. Create a Vector Database: Use ChromaDB to create and persist a database of embeddings.
```bash
from langchain.vectorstores import Chroma
vectordb = Chroma.from_documents(
    embedding=OpenAIEmbeddings(),
    documents=text_chunks,
    persist_directory="db"
)
```

4. Query and Retrieve Results: Retrieve documents using natural language queries.
```bash
retriever = vectordb.as_retriever()
docs = retriever.get_relevant_documents("What is Google AI?")
```

