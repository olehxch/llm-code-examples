import os
from pprint import pprint
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_ORG_ID = os.getenv('OPENAI_ORG_ID')

client = OpenAI()

chat_completion = client.chat.completions.create(
    model='gpt-4o-mini-mini',
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': 'Hello!'}
    ],
    temperature=0.0,
    top_p=1.0,
    max_tokens=4096,
    stop=['\n'],
    n=1,
    seed=42
)

response = chat_completion.choices[0].message

print('Chat Completion:', chat_completion.to_dict())
print('\n')
print('Chat Completion Message:', response.to_dict())
