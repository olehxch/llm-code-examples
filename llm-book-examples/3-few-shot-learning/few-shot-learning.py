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
            'content': f"""Here is an example: <div> 1+2+3+4=10. </div> The sum is 10."""
        },
        {
            'role': 'user',
            'content': f"""Here is an example: <span> 10+20+30+40=100. </span> The sum is 100."""
        },
        {
            'role': 'user',
            'content': f"""Here is an example: <b> 100+200+300+400=1000. </b> The sum is 1000."""
        },
        {
            'role': 'user',
            'content': f"""Rewrite the following text in the same style as in example. Make text bold and inside a div. Text: 5,6,7,8"""
        }
    ],
    temperature=1.0,
    seed=42
)

print('Chat Completion:', chat_completion)
print('Chat Completion Message:', chat_completion.choices[0].message)
