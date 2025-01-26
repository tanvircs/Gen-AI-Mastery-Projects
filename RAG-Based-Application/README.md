# RAG-Based Applications with Streamlit and Gemini Pro

This repository contains two Retrieval-Augmented Generation (RAG) applications built using Streamlit, LangChain, and Google Gemini Pro. These applications demonstrate the power of combining document retrieval with generative AI to provide detailed, context-driven responses to user queries.

## Applications

### 1. **RAG Application for Sentiment Analysis Research**

#### Overview
This application processes a research paper, *"Sentiment Analysis of COVID-19"*, and provides detailed answers to user queries by retrieving relevant content from the document.

#### Features
- Loads a PDF document using `PyPDFLoader`.
- Splits the document into manageable chunks for efficient retrieval.
- Uses **FAISS** for vectorized search based on semantic similarity.
- Employs Google Gemini Pro for generating context-aware answers.
- Interactive chat interface built with Streamlit.

#### How It Works
1. The PDF file is loaded and split into chunks of 1000 characters.
2. The chunks are vectorized and stored in a FAISS index.
3. User queries are matched against the FAISS index to retrieve relevant context.
4. The context is passed to a fine-tuned language model (Gemini Pro) to generate an elaborate answer.

#### Example
- **Input**: "What is the main methodology used in the research paper?"
- **Output**: A comprehensive explanation based on retrieved content.

---

### 2. **RAG Application for any Website Bot**

#### Overview
This application creates a chatbot for answering questions related to the content of specific websites. It is designed for ARi and other personal/professional sites.

#### Features
- Loads content from multiple URLs using `UnstructuredURLLoader`.
- Processes and splits website data into chunks for better retrieval.
- Utilizes FAISS for similarity-based document retrieval.
- Generates detailed responses with Google Gemini Pro.
- Allows for user interaction via a Streamlit interface.

#### How It Works
1. Website content is scraped and parsed into text documents.
2. The text is split into smaller chunks and indexed with FAISS.
3. User queries are matched with the most relevant content from the FAISS index.
4. The language model generates detailed answers using the retrieved context.

#### Example
- **Input**: "What services does ARi provide?"
- **Output**: A detailed explanation derived from the retrieved website content.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/rag-applications.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd rag-applications
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up environment variables by creating a .env file:**
   ```bash
   GOOGLE_API_KEY=<your_google_api_key>
   ```
5. **Run the Streamlit applications:**
   ```bash
   streamlit run app1.py  # For Sentiment Analysis RAG App
   streamlit run app2.py  # For ARi Website Bot
   ```

## Dependencies
- Python 3.8 or higher
- Streamlit
- LangChain
- Google Generative AI
- FAISS
- NLTK

## Acknowledgments
- LangChain for the framework.
- Google Gemini Pro for the powerful generative AI capabilities.
- Streamlit for the seamless UI development.
