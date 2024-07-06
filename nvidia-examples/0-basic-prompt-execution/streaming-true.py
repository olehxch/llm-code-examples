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
    model="meta/llama3-70b-instruct",
    messages=[{"role": "user",
               "content": "Write a limerick about the wonders of GPU computing."}],
    temperature=0.2,
    top_p=0.7,
    max_tokens=1024,
    stream=True
)

for chunk in completion:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")

