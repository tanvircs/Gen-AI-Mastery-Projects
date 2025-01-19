# 🚀 **Source Code Analysis with AI-Powered Chatbot**

Welcome to the **Source Code Analysis** project! This repository is a cutting-edge application built using **Flask**, **LangChain**, and **OpenAI GPT** to create a seamless and interactive AI-powered chatbot for analyzing and understanding source code repositories.

---

## 🌟 **Features**
- **AI-Powered Chatbot**: Communicate with an AI to query and retrieve insights from your codebase.
- **Conversational Retrieval**: Employs state-of-the-art **Conversational Retrieval Chains** with memory for seamless interaction.
- **Persistent Database**: Utilizes **Chroma** for vector storage to ensure efficient data retrieval.
- **Dynamic Repository Ingestion**: Automatically ingests source code repositories for analysis.
- **Scalable Design**: Built with extensibility and modularity for future enhancements.

---

## 🛠️ **Technologies Used**
- **Backend**:
  - [Flask](https://flask.palletsprojects.com/): Python-based web framework for hosting the application.
  - [LangChain](https://www.langchain.com/): Framework for building language model-powered applications.
  - [OpenAI GPT](https://openai.com/): Large language model for natural language understanding.
  - **Chroma**: Vector database for semantic search and retrieval.
- **Frontend**:
  - HTML5, CSS3, JavaScript
- **Deployment**:
  - Docker-ready (future integration planned)

---

## 📂 **Project Structure**
```bash
End-to-End-Projects/
└── Source-Code-Analysis/
    ├── app.py              # Flask application entry point
    ├── src/                # Source code directory
    │   ├── helper.py       # Helper functions for embedding and ingestion
    │   └── __init__.py     # Package initialization
    ├── templates/          # HTML templates for the Flask app
    │   └── index.html      # Home page of the application
    ├── static/             # CSS and JavaScript assets
    ├── .env                # Environment variables
    ├── research/           # Research directory
    │   └── trials.ipynb    # Research notebook for experiments
    └── README.md           # Project documentation
```

### 1. Clone the Repository
   ```bash
   git clone https://github.com/your-username/source-code-analysis.git
   cd source-code-analysis
   ```
### 2. Set Up Virtual Environment:
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
### 3. Install Dependencies:
   ```bash
    pip install -r requirements.txt
   ```
### 4. Set Up Environment Variables:
- Create a .env file in the root directory.
- Add the following:
   ```bash
    OPENAI_API_KEY=your_openai_api_key
   ```
### 5. Run the Application:
   ```bash
   python app.py
   ```

## 🌐 Access the App:
- Open your browser and navigate to http://127.0.0.1:8080.

## 🧠 How It Works
- Repository Ingestion: The app ingests your repository's source code for analysis.
- Embedding: The source code is embedded into vector space using pre-trained models.
- Chat Interaction: You can ask questions about the codebase, and the AI retrieves answers using conversational memory and advanced retrieval techniques.

## ✨ Future Enhancements
- Add Docker Support for containerized deployment.
- Integrate Continuous Deployment with platforms like AWS or Azure.
- Expand support for multiple programming languages.
- Add a visualization tool for code structure insights.

## 💡 Contributing
We welcome contributions! If you’d like to contribute:

- Fork the repository.
- Create a feature branch.
- Submit a pull request with a detailed explanation.

## 🙌 Acknowledgments
Special thanks to:

- The creators of LangChain, Flask, and OpenAI for their amazing tools.
- The open-source community for inspiring innovation.

## 📧 Contact
- Project Maintainer: Tanvir Ahmed
- Email: tanvirahmed.cs.93@gmail.com
- GitHub: tanvircs

## ⭐ Show Your Support
If you find this project useful, please consider giving it a ⭐ on GitHub!
```bash
Let me know if you need help refining or customizing this further!
```

## Created with ❤️ by Tanvir Ahmed.
   ```bash
   This `README.md` provides a comprehensive overview of source code analysis from github using llm model. Replace placeholders like repository URLs and API keys with actual values to complete the setup.
   ```
