from fastapi import FastAPI
import openai
from apikey import APIKEY
openai.api_key = APIKEY

app = FastAPI()

@app.get("/input/{input}")
async def root(input):
    output = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": 
            input}]
    )

    # Print out the whole output dictionary
    # print(output)

    # Get the output text only
    result = output['choices'][0]['message']['content']
    return {"message": result}

