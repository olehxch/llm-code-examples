import os
from openai import OpenAI
from dotenv import load_dotenv

# Get the API key and organization ID from the environment
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_ORG_ID = os.getenv('OPENAI_ORG_ID')

client = OpenAI()

chat_completion = client.chat.completions.create(
    model='gpt-4o',
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

print('Chat Completion:', chat_completion)
print('Chat Completion Message:', chat_completion.choices[0].message)
