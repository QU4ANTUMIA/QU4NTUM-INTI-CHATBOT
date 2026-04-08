from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Message(BaseModel):
    message: str

@app.get("/")
def home():
    return {"mensaje": "Chatbot activo 🚀"}

@app.post("/chat")
def chat(msg: Message):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": msg.message}]
    )
    
    return {"respuesta": response.choices[0].message.content}
