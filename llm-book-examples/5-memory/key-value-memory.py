import os
from openai import OpenAI
from dotenv import load_dotenv

# Get the API key and organization ID from the environment
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_ORG_ID = os.getenv('OPENAI_ORG_ID')

client = OpenAI()

# 1. Parse the 'memory.txt' file and store the key-value pairs in a dictionary
with open('./llm-book-examples/5-memory/memory.txt', 'r') as f:
    content = f.read().split('\n\n')

books = {}
for book in content:
    title, description = book.split('\n---\n')
    books[title] = description.strip()

# 2. Create a chat and use the key-value pairs as a memory
chat_messages = []

# In this case a full name of the chapter should be mentioned.
# List of chapters from the 'memory.txt' file:
# Chapter 1: The Call to Adventure
# Chapter 2: The Gathering Storm
# Chapter 3: The Enchanted Bridge

while True:
    memory_message = None
    prompt = input('user: ')

    if prompt == 'exit':
        break

    for book in books:
        if book in prompt:
            print('Title found in the memory:', book)
            memory_message = {
                'role': 'user', 'content': 'Here is a description of ' + book + ': ' + books[book] + '.'}

    messages = []
    if memory_message:
        messages.append(memory_message)
    messages.append({'role': 'user', 'content': prompt})

    chat_completion = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages,
        temperature=0.1,
        seed=42
    )

    message = chat_completion.choices[0].message

    print(f'{message.role}: {message.content}')
