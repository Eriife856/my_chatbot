
from google import genai
from pydantic import BaseModel, Field
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from google.genai import types
import os
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
config = types.GenerateContentConfig(
    system_instruction='''You are a Child Development Assistant.
Your goal is to help with questions related to child development, child psychology,
early childhood education, parenting, and family studies.

Explain concepts clearly, in simple language, and use examples when possible.

If the user asks about something NOT related to child development, early childhood,
parenting, child psychology, or family studies, politely refuse and say:
"I can only help with child development related topics."
'''
)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)
class ChatRequest(BaseModel):
    message: str = Field(..., example="What is child development?")
@app.post("/chat")
def chat(input: ChatRequest):
    try:
        response = client.models.generate_content_stream(
            model="gemini-2.5-flash",
            contents=input.message,
            config=config,
        )
        result = ""
        for chunks in response:
            print("chatbot completed!", chunks.text, end="", flush=True)
            result += chunks.text
        return {"response": result}
    except Exception as e:
        return {"error": "Check Your internet Connection"}