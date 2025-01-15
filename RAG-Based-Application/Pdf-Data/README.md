# RAG Application using Gemini Pro

This project is a **Retrieval-Augmented Generation (RAG) Application** built using Streamlit, LangChain, and Google Gemini Pro. The application allows users to interactively ask questions based on PDF documents and receive detailed, context-aware answers.

---

## 🚀 Features

- **PDF Document Loading**: Upload and process PDFs for question-answering tasks.
- **Document Splitting**: Utilizes `RecursiveCharacterTextSplitter` to split large documents into manageable chunks.
- **Vector Search**: Embeds document data using Google Generative AI embeddings and stores it in a FAISS vector database for efficient retrieval.
- **Question-Answering**: Leverages Google Gemini Pro for generating detailed and context-rich answers to user queries.
- **Streamlit Interface**: Interactive and user-friendly interface for real-time Q&A.

---

## 🛠️ Tech Stack

- **[Streamlit](https://streamlit.io/)**: For creating the user interface.
- **[LangChain](https://www.langchain.com/)**: Framework for integrating retrieval-augmented generation workflows.
- **[FAISS](https://github.com/facebookresearch/faiss)**: Vector database for fast similarity search.
- **[Google Generative AI](https://ai.google/tools/)**: Embeddings and language model (`Gemini Pro`) for Q&A generation.
- **Python**: Programming language used for development.

---

## 📂 File Structure

- **`Acceptance-testing.pdf`**: Sample PDF file loaded into the application.
- **`app.py`**: Main application script with Streamlit, LangChain, and model integrations.
- **`.env`**: Environment variables for API keys and sensitive information.

---

## 📝 Usage

1. **Install Dependencies**:
   ```bash
   pip install streamlit langchain faiss-cpu langchain-google-genai python-dotenv
   ```
2. **Set Up Environment: Create a .env file and add your API keys**:
   ```bash
   GOOGLE_GENAI_API_KEY=<your_google_genai_api_key>
   ```
3. **Run the Application: Start the Streamlit app**:
   ```bash
   streamlit run app.py
   ```
4. **Interact with the App**:
- Upload a PDF file (e.g., Acceptance-testing.pdf).
- Enter your question in the chat input.
- View detailed answers generated using Google Gemini Pro.