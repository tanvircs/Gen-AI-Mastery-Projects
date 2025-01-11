# FastAPI PDF Analysis and Question-Answer Generator

## Project Description
This project leverages FastAPI to create a web application that allows users to upload PDF documents, analyzes the content, and generates question-answer pairs based on the text extracted from the PDFs. It uses the LangChain library for natural language processing, specifically utilizing models like GPT-3.5-turbo to generate and refine questions and answers.

## Features
- **PDF Upload:** Users can upload PDF documents to be analyzed.
- **Content Analysis:** Extracts text from PDFs and processes it to generate questions.
- **Question-Answer Generation:** Uses advanced NLP models to generate and refine questions and answers from the text.
- **CSV Output:** Outputs the questions and their corresponding answers in a CSV file format.

## Tech Stack
- **FastAPI:** Asynchronous framework for building APIs.
- **LangChain:** Utilizes NLP chains for generating and refining content.
- **Jinja2:** Templating engine for serving HTML content.
- **Uvicorn:** ASGI server for hosting the application.
- **aiofiles and Python standard libraries:** For file handling and asynchronous operations.

## Getting Started

### Prerequisites
Before you can run this project, you'll need to install several dependencies:
- Python 3.8 or higher
- FastAPI
- Uvicorn
- aiofiles
- Jinja2
- LangChain

You can install these with pip:
```bash
pip install fastapi uvicorn aiofiles jinja2 langchain
