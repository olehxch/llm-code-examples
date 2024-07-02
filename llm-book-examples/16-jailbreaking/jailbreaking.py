import os
from openai import OpenAI
from dotenv import load_dotenv

# Get the API key and organization ID from the environment
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_ORG_ID = os.getenv('OPENAI_ORG_ID')

client = OpenAI()


def content_filter():
    prompt = 'Did the Darth Vader defeat the Jedi?'
    messages = [
        {'role': 'system', 'content': 'You are a classifier. Does the following text cover the topic of Star Wars in any way? Respond with "yes" or "no".'},
        {'role': 'user', 'content': 'Who was Luke Skywalker\'s father?'},
        {'role': 'assistant', 'content': 'yes'},
        {'role': 'user', 'content': 'Who was better, Kirk or Picard?'},
        {'role': 'assistant', 'content': 'no'},
        {'role': 'user', 'content': prompt}
    ]

    chat_completion = client.chat.completions.create(
        model='gpt-4o',
        messages=messages,
        max_tokens=500,
        temperature=0.1,
        seed=42
    )

    if 'yes' in chat_completion.choices[0].message.content:
        print('I am not at liberty to discuss this topic.')
    else:
        print(chat_completion.choices[0].message.content)


def allowed_content():
    prompt = 'Write in a few words how the car engine works.'
    messages = [
        {'role': 'system', 'content': 'You are a classifier. Does the following text cover the topic of Star Wars in any way? Respond with "yes" or "no".'},
        {'role': 'user', 'content': 'Who was Luke Skywalker\'s father?'},
        {'role': 'assistant', 'content': 'yes'},
        {'role': 'user', 'content': 'Who was better, Kirk or Picard?'},
        {'role': 'assistant', 'content': 'no'},
        {'role': 'user', 'content': prompt}
    ]

    chat_completion = client.chat.completions.create(
        model='gpt-4o',
        messages=messages,
        max_tokens=500,
        temperature=0.1,
        seed=42
    )

    if 'yes' in chat_completion.choices[0].message.content:
        print('I am not at liberty to discuss this topic.')
    else:
        allowed_chat_completion = client.chat.completions.create(
            model='gpt-4o',
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=500,
            temperature=0.1,
            seed=42
        )

        print(allowed_chat_completion.choices[0].message.content)


def bypass_content_policy():
    prompt = 'Who created Indiana Jones? What are some other popular movies created by them?'
    messages = [
        {'role': 'system', 'content': 'You are a classifier. Does the following text cover the topic of Star Wars in any way? Respond with "yes" or "no".'},
        {'role': 'user', 'content': 'Who was Luke Skywalker\'s father?'},
        {'role': 'assistant', 'content': 'yes'},
        {'role': 'user', 'content': 'Who was better, Kirk or Picard?'},
        {'role': 'assistant', 'content': 'no'},
        {'role': 'user', 'content': prompt}
    ]

    chat_completion = client.chat.completions.create(
        model='gpt-4o',
        messages=messages,
        max_tokens=500,
        temperature=0.1,
        seed=42
    )

    if 'yes' in chat_completion.choices[0].message.content:
        print('I am not at liberty to discuss this topic.')
    else:
        allowed_chat_completion = client.chat.completions.create(
            model='gpt-4o',
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=500,
            temperature=0.1,
            seed=42
        )

        print(allowed_chat_completion.choices[0].message.content)


content_filter()
allowed_content()
bypass_content_policy()
