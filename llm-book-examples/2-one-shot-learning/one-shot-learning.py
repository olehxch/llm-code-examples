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
        {'role': 'system', 'content': 'You are helpful math assistant.'},
        {
            'role': 'user',
            'content': f"""Here is some sample text: One equals 1, two equals 2, three equals 3, and four equals 4. The sum is 10.
        Rewrite the following text in the same style as the sample: 5,6,7,8"""
        }
    ],
    temperature=0.0,
    seed=42
)

print('Chat Completion:', chat_completion)
print('Chat Completion Message:', chat_completion.choices[0].message)
