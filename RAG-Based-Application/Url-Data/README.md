# RAG Application for ARi Website Bot

This repository contains a **Retrieval-Augmented Generation (RAG) Application** designed to serve as a question-answering bot for the ARi website. The bot uses cutting-edge technologies, including **Streamlit**, **LangChain**, and **Google Generative AI (Gemini 1.5 Pro)**, to retrieve and generate insightful responses based on content retrieved from specified URLs.

## Features

- **URL-Based Content Loading**: Fetches unstructured data from websites.
- **Recursive Text Splitting**: Prepares the data for indexing and retrieval by dividing it into manageable chunks.
- **FAISS Vectorstore Integration**: Efficiently indexes and retrieves similar content using embeddings from Google Generative AI.
- **Google Generative AI**: Generates detailed and context-aware answers based on retrieved information.
- **Streamlit Interface**: Provides an interactive UI for users to ask questions and receive responses.

## Technologies Used

- [Streamlit](https://streamlit.io/) for creating a user-friendly web interface.
- [LangChain](https://langchain.readthedocs.io/) for building retrieval and document-processing chains.
- [FAISS](https://faiss.ai/) for vector-based similarity search.
- [Google Generative AI](https://cloud.google.com/generative-ai) for embedding and answering queries.
- [NLTK](https://www.nltk.org/) for natural language processing utilities.

## Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/rag-ari-bot.git
   cd rag-ari-bot
   ```
2. **Set up a Python virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Create a .env file and add your required environment variables (e.g., API keys for Google Generative AI).**
5. **Run the application:**
   ```bash
   streamlit run app.py
   ```
