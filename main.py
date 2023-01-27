from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
    text: str

app = FastAPI()
translator = pipeline("translation_en_to_ru", "Helsinki-NLP/opus-mt-en-ru")

@app.get("/")
def root():
    """Default response from root"""
    
    return {"message": "Hello, world!"}

@app.post("/predict/")
def predict(item: Item):
    """Translation of English text to Russian"""
    
    return translator(item.text )[0]