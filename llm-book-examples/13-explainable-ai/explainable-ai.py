import os
from openai import OpenAI
from dotenv import load_dotenv

# Get the API key and organization ID from the environment
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_ORG_ID = os.getenv('OPENAI_ORG_ID')

client = OpenAI()


def asking_for_reference():
    chat_completion = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {'role': 'user', 'content': 'Tell me more about razor sword fish inside the ocean. Provide all references.'},
        ],
        max_tokens=1500,
        temperature=0.1,
        seed=42
    )

    print('Response:', chat_completion.choices[0].message.content)


def calculate_letters():
    # Example with incorrect math calculation

    chat_completion = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {'role': 'user', 'content': 'How many times does the letter "e" show up in the days of the week? Think step by step.'},
        ],
        max_tokens=500,
        temperature=0.1,
        seed=42
    )

    print('Response:', chat_completion.choices[0].message.content)


asking_for_reference()
calculate_letters()
