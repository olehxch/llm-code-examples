import os
import json
from openai import OpenAI, embeddings
from dotenv import load_dotenv
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions


# Get the API key and organization ID from the environment
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_ORG_ID = os.getenv('OPENAI_ORG_ID')

client = OpenAI()

embeddings = json.load(open('embeddings.json', 'r'))


def get_embedding(text):
    embedding = client.embeddings.create(
        input=[text.replace('\n', ' ')],
        model='text-embedding-ada-002')

    return embedding.data[0].embedding


def cosine_distance(a, b):
    return 1 - sum([a_i * b_i for a_i, b_i in zip(a, b)]) / (
        sum([a_i ** 2 for a_i in a]) ** 0.5 * sum([b_i ** 2 for b_i in b]) ** 0.5)


def nearest_embedding(embedding):
    nearest, nearest_distance = None, 1

    for chapter_key, chapter_embedding in embeddings.items():
        distance = cosine_distance(embedding, chapter_embedding)
        if distance < nearest_distance:
            nearest, nearest_distance = chapter_key, distance

    return nearest


def find_chapter_by_key(key):
    local_embeddings = {}

    with open('data.txt', 'r') as f:
        sum = f.read()
        chapters = sum.split('\n\n')

        for chapter in chapters:
            splitted = chapter.split('---')
            chapter_title = splitted[0].strip()
            chapter_text = splitted[1].strip()

            local_embeddings[chapter_title] = chapter_text

    return local_embeddings[key]


while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    prompt_embedding = get_embedding(prompt)
    nearest_embedding_key = nearest_embedding(prompt_embedding)
    chapter_text = find_chapter_by_key(nearest_embedding_key)

    print('Found nearest chapter:', nearest_embedding_key)

    chat_completion = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {'role': 'system', 'content': 'You are a Q&A AI.'},
            {'role': 'system', 'content': 'Here are some facts that can help you answer the following question: ' + chapter_text},
            {'role': 'user', 'content': prompt}
        ],
        temperature=0.1,
        seed=42
    )

    print('Chat Completion Message:',
          chat_completion.choices[0].message.content)
