import streamlit as st
import requests

# Define the FastAPI server URL
API_URL = "http://127.0.0.1:8000"  # Adjust if your server runs on a different port

# Streamlit application title
st.title("Mental Health Chatbot")

# RAG Section
st.header("Retrieval-Augmented Generation (RAG)")

# User input for RAG
rag_prompt = st.text_area("Describe your mental health issues:")
if st.button("Get Articles"):
    if rag_prompt:
        response = requests.post(f"{API_URL}/rag", json={"prompt": rag_prompt})
        if response.status_code == 200:
            articles = response.json().get("response", "")
            st.subheader("Relevant Articles:")
            st.write(articles)
        else:
            st.error("Error fetching articles from the server.")

# Classification Section
st.header("Classification")

# User input for Classification
classification_input = st.text_area("Enter stories to classify (one per line):")
if st.button("Classify"):
    if classification_input:
        stories = classification_input.splitlines()
        response = requests.post(f"{API_URL}/classification", json={"data": stories})
        if response.status_code == 200:
            classifications = response.json()
            st.subheader("Classification Results:")
            for item in classifications:
                st.write(f"**Title:** {item['title']}")
                st.write(f"**URL:** {item['url']}")
                st.write(f"**Category:** {item['category']}")
                st.write("---")
        else:
            st.error("Error classifying stories from the server.")