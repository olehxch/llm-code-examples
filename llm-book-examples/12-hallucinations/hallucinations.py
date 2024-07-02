import os
from openai import OpenAI
from dotenv import load_dotenv

# Get the API key and organization ID from the environment
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_ORG_ID = os.getenv('OPENAI_ORG_ID')

client = OpenAI()


def imaginary_fact():
    # Provide an imaginary fact and check the hallucinated response

    chat_completion = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {'role': 'user', 'content': 'Tell me more about razor sword fish inside the ocean.'},
        ],
        max_tokens=500,
        temperature=0.1,
        seed=42
    )

    print('Hallucinated response:', chat_completion.choices[0].message.content)


def limit_fake_facts():
    # Limit the LLM to not generate fake facts

    guide = f'''
    You are a large language model trained on vast amounts of data.
    You respond to questions based on the data you were trained on.
    When you do not have enough information to provide an accurate answer, you will say so.
    Do not use fake facts or make up fake information.
    '''

    chat_completion = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {'role': 'user', 'content': guide +
                'Tell me more about razor sword fish inside the ocean.'},
        ],
        max_tokens=500,
        temperature=0.1,
        seed=42
    )

    print('---')
    print('Actual response:', chat_completion.choices[0].message.content)


def incorrect_math():
    # Example with incorrect math calculation

    chat_completion = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {'role': 'user', 'content': 'What are the last five Fibonacci numbers starting from 1000000000000 Fibonacci number?'},
        ],
        max_tokens=500,
        temperature=0.1,
        seed=42
    )

    print('---')
    print('Incorrect response:', chat_completion.choices[0].message.content)


def incorrect_calculation():
    # Example with incorrect math calculation

    chat_completion = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {'role': 'user', 'content': 'How many times does the letter "e" show up in the days of the week?'},
        ],
        max_tokens=500,
        temperature=0.1,
        seed=42
    )

    print('---')
    print('Incorrect response:', chat_completion.choices[0].message.content)


def python_code_for_calculation():
    # Example with Python code generation from LLM

    chat_completion = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {'role': 'user', 'content': 'Provide a python code for the task: How many times does the letter "e" show up in the days of the week?.'},
        ],
        max_tokens=500,
        temperature=0.1,
        seed=42
    )

    print('---')
    print('Incorrect response:', chat_completion.choices[0].message.content)


def incorrect_python_code_execution():
    # Example with fake Python code execution on LLM

    code = '''
    # List of days of the week
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Initialize a counter for the letter 'e'
    e_count = 0

    # Loop through each day and count the occurrences of 'e'
    for day in days_of_week:
        e_count += day.lower().count('e')

    # Print the result
    print(f"The letter 'e' appears {e_count} times in the days of the week.")
    '''
    chat_completion = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {'role': 'user', 'content': 'Execute provided Python code and show the result: ' + code},
        ],
        max_tokens=500,
        temperature=0.1,
        seed=42
    )

    print('---')
    print('Incorrect response:', chat_completion.choices[0].message.content)


imaginary_fact()
limit_fake_facts()
incorrect_math()
incorrect_calculation()
python_code_for_calculation()
incorrect_python_code_execution()
