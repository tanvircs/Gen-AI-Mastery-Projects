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
```
# Application Setup Guide

## How to Run

This guide walks you through setting up and running the application. Follow the steps below to get everything up and running smoothly.

### Create an environment

1. **Create a Conda environment:** Use the following commands to create a Conda environment named `interview` with Python 3.10. This ensures that all dependencies are managed correctly.

    ```bash
    conda create -n interview python=3.10 -y
    conda activate interview
    ```

### Install requirements

2. **Install required packages:** After setting up and activating the environment, install the necessary packages listed in the `requirements.txt` file. This file contains all the Python libraries that your application needs to run.

    ```bash
    pip install -r requirements.txt
    ```

### Run the application

3. **Start the server:** Once the environment is set up and all packages are installed, you can start the application server using the following command. This command tells Uvicorn, an ASGI server, to run your FastAPI application.

    ```bash
    uvicorn app:app --host 0.0.0.0 --port 8080 --reload
    ```

    - The `--reload` flag enables auto-reloading so the server will restart whenever changes are made to the code.
    - The application will be available at `http://localhost:8080`. Navigate to this URL in your web browser to interact with the application.

## Additional Information

This README provides the basic steps to get your application running. For more detailed information about the project's functionality and its components, refer to the project's documentation or other sections of the README that might include usage examples, development guidelines, and contributions.

Thank you for setting up and using our application!

