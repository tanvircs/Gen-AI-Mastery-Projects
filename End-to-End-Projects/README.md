# 🌟 End-to-End AI Projects Repository

## Overview
This repository houses two comprehensive AI projects that demonstrate end-to-end implementations of real-world applications using cutting-edge technologies such as **Flask**, **LangChain**, **OpenAI GPT**, and more. The projects include:

1. **Medical Chatbot with Generative AI and Pinecone Integration**
2. **Source Code Analysis with AI-Powered Chatbot**

---

## 🚀 Projects Overview

### 1️⃣ Medical Chatbot with Generative AI and Pinecone Integration

#### Description
This project builds a Medical Chatbot that allows users to input medical-related queries. The chatbot retrieves relevant context from preprocessed documents and generates accurate, concise responses.

#### Features
- Document Preprocessing and Splitting
- Vector Storage using Pinecone
- Intelligent Document Retrieval
- Generative AI Integration via OpenAI GPT
- User-Friendly Web Interface built with Flask

#### Project Structure
```plaintext
Medical-Chatbot/
├── app.py                # Main Flask application
├── src/
│   ├── __init__.py       # Package initialization
│   ├── helper.py         # Helper functions for embeddings and document processing
│   ├── prompt.py         # Prompt templates for the LLM
├── setup.py              # Setup file for project dependencies
├── requirements.txt      # Python package dependencies
├── store_index.py        # Index creation and data addition to Pinecone
├── template.py           # File structure initialization script
├── research/
│   ├── trials.ipynb      # Jupyter notebook for experimentation
├── test.py               # Test script
```

#### Setup Instructions
1. Clone the Repository:
   ```bash
   git clone https://github.com/your-username/medical-chatbot.git
   cd medical-chatbot
   ```
2. Create a Virtual Environment:
   ```bash
   conda create -n medical-chatbot python=3.8 -y
   conda activate medical-chatbot
   ```
3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set Environment Variables:
   ```plaintext
   PINECONE_API_KEY=your_pinecone_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```
5. Preprocess Data and Create Index:
   ```bash
   python store_index.py
   ```
6. Run the Application:
   ```bash
   python app.py
   ```

---

### 2️⃣ Source Code Analysis with AI-Powered Chatbot

#### Description
This project enables interactive analysis and understanding of source code repositories through an AI-powered chatbot. It uses LangChain, OpenAI GPT, and Chroma for efficient retrieval and analysis.

#### Features
- AI-Powered Chatbot for Source Code Queries
- Conversational Retrieval with Memory
- Persistent Vector Database with Chroma
- Dynamic Repository Ingestion
- Scalable Design for Extensibility

#### Project Structure
```plaintext
Source-Code-Analysis/
├── app.py                # Flask application entry point
├── src/
│   ├── helper.py         # Helper functions for embedding and ingestion
│   └── __init__.py       # Package initialization
├── templates/            # HTML templates for the Flask app
│   └── index.html        # Home page of the application
├── static/               # CSS and JavaScript assets
├── .env                  # Environment variables
├── research/             # Research directory
│   └── trials.ipynb      # Research notebook for experiments
├── README.md             # Project documentation
```

#### Setup Instructions
1. Clone the Repository:
   ```bash
   git clone https://github.com/your-username/source-code-analysis.git
   cd source-code-analysis
   ```
2. Set Up Virtual Environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set Environment Variables:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   ```
5. Run the Application:
   ```bash
   python app.py
   ```
6. Access the App:
   Open your browser and navigate to http://127.0.0.1:8080.

---

## 🛠️ Technologies Used
### Shared Across Projects
- **Backend**:
  - Flask
  - LangChain
  - OpenAI GPT
- **Frontend**:
  - HTML5, CSS3, JavaScript
- **Database**:
  - Pinecone (Medical Chatbot)
  - Chroma (Source Code Analysis)
- **Deployment**:
  - Docker-ready (future integration planned)

---

## ✨ Future Enhancements
- Dockerize both projects for containerized deployment.
- Add Continuous Deployment pipelines using GitHub Actions.
- Extend support for multilingual queries and analysis.
- Integrate visualization tools for better user experience.

---

## 💡 Contributing
We welcome contributions! To contribute:
1. Fork this repository.
2. Create a feature branch.
3. Submit a pull request with detailed explanations of changes.

---

## 🙌 Acknowledgments
Special thanks to:
- The creators of LangChain, Flask, OpenAI, and Chroma for their excellent tools.
- The open-source community for fostering innovation and collaboration.

---

## 📧 Contact
- **Project Maintainer**: Tanvir Ahmed
- **Email**: tanvirahmed.cs.93@gmail.com
- **GitHub**: [tanvircs](https://github.com/tanvircs)

---

## ⭐ Show Your Support
If you find this repository useful, please consider giving it a ⭐ on GitHub!
