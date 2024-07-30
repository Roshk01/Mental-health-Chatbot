import pandas as pd
from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from typing import List


app = FastAPI()

# Load the dataset
data = pd.read_csv('dataset.csv')

# Load a pre-trained LLM for text generation
generator = pipeline('text-generation', model='gpt2')

# Prepare the data
X = data['TITLE']  # Features (text data)
y = data['CATEGORY']  # Labels (categories)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline for vectorization and model training
model = make_pipeline(CountVectorizer(), LogisticRegression())
model.fit(X_train, y_train)

class MentalHealthPrompt(BaseModel):
    prompt: str

@app.post("/rag")
async def rag_endpoint(prompt: MentalHealthPrompt):
    # Generate relevant articles based on the user's prompt
    articles = generator(prompt.prompt, max_length=100, num_return_sequences=3)
    response = "\n".join([article['generated_text'] for article in articles])
    return {"response": response}

class ClassificationInput(BaseModel):
    data: List[str]

class ClassificationResponse(BaseModel):
    title: str
    url: str
    category: str

@app.post("/classification", response_model=List[ClassificationResponse])
async def classification_endpoint(input_data: ClassificationInput):
    # Predict categories for the input data
    predictions = model.predict(input_data.data)
    
    # Prepare the response with titles and URLs
    response = []
    for i, prediction in enumerate(predictions):
        response.append({
            "title": data.iloc[i]['TITLE'],  # Get title from the original dataset
            "url": data.iloc[i]['URL'],      # Get URL from the original dataset
            "category": prediction.tolist()   # Predicted category
        })
    
    return response

