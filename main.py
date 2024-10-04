from fastapi import FastAPI
import openai
from apikey import APIKEY

openai.api_key = APIKEY

app = FastAPI()

@app.get("/input/{input}")
async def root(input: str):
    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": input}
        ]
    )
    
    result = output.choices[0].message['content']
    return {"message": result}
