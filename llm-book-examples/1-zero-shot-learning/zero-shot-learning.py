import os
from openai import OpenAI
from dotenv import load_dotenv

# Get the API key and organization ID from the environment
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_ORG_ID = os.getenv('OPENAI_ORG_ID')

client = OpenAI()

chat_completion = client.chat.completions.create(
    model='gpt-4o-mini-mini',
    messages=[
        {'role': 'system', 'content': 'You are an English to Ukrainian translator.'},
        {'role': 'user', 'content': 'Translate this to Polish: Hi, how are you?'}
    ],
    temperature=0.0,
    seed=42
)

print('Chat Completion:', chat_completion)
print('\n')
print('Chat Completion Message:', chat_completion.choices[0].message)
