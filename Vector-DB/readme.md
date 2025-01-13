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

## Pinecone Workflow
### Steps:
1. Initialize Pinecone:

```bash
from pinecone import Pinecone, ServerlessSpec
pc = Pinecone(api_key="your-pinecone-api-key")
index_name = "example-index"
pc.create_index(
    name=index_name,
    dimension=1536,
    metric='cosine',
    spec=ServerlessSpec(cloud='aws', region='us-east-1')
)
index = pc.Index(index_name)
```

2. Upload Embeddings: Embed document chunks and upload vectors to Pinecone.

```bash
embedded_texts = [OpenAIEmbeddings().embed_query(chunk.page_content) for chunk in text_chunks]
index.upsert(vectors=[(str(i), vec) for i, vec in enumerate(embedded_texts)])
```

3. Query the Index: Retrieve similar documents from Pinecone.

```bash
query_vector = OpenAIEmbeddings().embed_query("YOLOv7 outperforms which models?")
response = index.query(vector=query_vector, top_k=5)
```

## Weaviate Workflow
### Steps:
1. Initialize Weaviate:

```bash
from weaviate.client import Client
from weaviate.auth import AuthApiKey

auth_config = AuthApiKey(api_key="your-weaviate-api-key")

client = Client(
    url="https://your-weaviate-instance",
    auth_client_secret=auth_config,
    additional_headers={"X-OpenAI-Api-Key": "your-openai-api-key"}
)
```

2. Define Schema: Set up the schema for storing document vectors.

```bash
schema = {
    "classes": [
        {
            "class": "Document",
            "description": "Documents for retrieval",
            "properties": [{"dataType": ["text"], "name": "content"}]
        }
    ]
}
client.schema.create(schema)
```

3. Upload Text Chunks: Add document embeddings to Weaviate.

```bash
from langchain.vectorstores import Weaviate
vectorstore = Weaviate(client, "Document", "content")
vectorstore.add_texts([chunk.page_content for chunk in text_chunks])
```

4. Perform Similarity Search: Retrieve documents based on query similarity.

```bash
query = "What is YOLO?"
results = vectorstore.similarity_search(query, top_k=5)
```

## Requirements
- [Python 3.7 or higher]
- [API keys for OpenAI, Pinecone, and Weaviate.]


## Usage
Replace placeholders like your-openai-api-key, your-pinecone-api-key, and your-weaviate-api-key with valid keys.

Run the provided code cells step by step for each vector database to see the respective functionality.

## Acknowledgements
Special thanks to:
- [LangChain for providing robust tools for embeddings and vector databases.]
- [ChromaDB, Pinecone, and Weaviate for seamless vector database integrations.]
- [OpenAI for the powerful GPT models.]