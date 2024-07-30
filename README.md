# Mental Health Chatbot

This repository contains a FastAPI server and a Streamlit application for a mental health chatbot. The chatbot utilizes a Retrieval-Augmented Generation (RAG) mechanism and a classification model to assist users with their mental health inquiries.

## Table of Contents

- [Installation](#installation)
- [FastAPI Server](#fastapi-server)
  - [Endpoints](#endpoints)
- [Streamlit Application](#streamlit-application)
- [Bonus Points](#bonus-points)
- [Running the Application](#running-the-application)
- [Documentation](#documentation)

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## FastAPI Server

The FastAPI server is developed with two main endpoints:

### Endpoints

#### `/rag`

- **Objective**: Build a Retrieval-Augmented Generation (RAG) application for a mental health chatbot. This endpoint accepts a user prompt describing their mental health issues and returns relevant articles or blog posts.
- **Implementation**: Utilizes an open-source large language model (LLM) to generate responses.

#### `/classification`

- **Objective**: Create a classification model that classifies input data into appropriate categories based on a provided dataset.
- **Implementation**: Uses Scikit-learn to train a model on the dataset and return the classification results along with the title and URL of each classified story.

## Streamlit Application

The Streamlit application provides a user-friendly interface to interact with the FastAPI server. Users can input their mental health prompts and stories for classification, and view the generated articles and classification results.

## Bonus Points

### Hugging Face Space

- Created a Hugging Face Space to test and demonstrate the models developed in this project.

### Optimization

- Optimized the response time of the FastAPI application to ensure efficient performance.

### Productionisation

- Created a `Dockerfile` and `requirements.txt` to containerize and productionize the FastAPI server.

## Running the Application

1. **Start the FastAPI server**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

3. Open your browser and navigate to `http://localhost:8501` to access the Streamlit interface.

## Documentation

Ensure that your code is well-documented with comments explaining key parts of the implementation. The repository includes a README file with clear instructions for setup and execution.

---

Make sure to replace `yourusername` and `your-repo-name` with your actual GitHub username and repository name. This README provides a comprehensive overview of your project, making it easier for others to understand and use your work.

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/17170031/e0f38de8-8dc7-4da2-9b8a-b20f5db811e1/Assignment-For-AI-Intern-.pdf
