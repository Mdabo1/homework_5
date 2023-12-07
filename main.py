from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()

# Load the question-answering pipeline

distilled_student_sentiment_classifier = pipeline(
    model="lxyuan/distilbert-base-multilingual-cased-sentiments-student"
)


@app.get("/")
def root():
    return {"message": "Hello, Prepod"}


@app.post("/answer/")
def answer(item: Item):
    return distilled_student_sentiment_classifier(item.text)
