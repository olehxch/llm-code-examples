import requests
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(
    base_url='https://integrate.api.nvidia.com/v1',
)

completion = client.chat.completions.create(
    model="mistralai/mistral-large",
    messages=[{"role": "user",
               "content": """Implement a function that takes a list of integers and returns the sum of the list in JavaScript language. 
               Provide only the function body without any additional descriptions, comments or tests."""}],
    temperature=0.2,
    top_p=0.7,
    max_tokens=1024,
    stream=False
)

print(completion.choices[0].message.content)
