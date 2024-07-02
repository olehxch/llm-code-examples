import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Get the API key and organization ID from the environment
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_ORG_ID = os.getenv('OPENAI_ORG_ID')

client = OpenAI()


def get_embedding(text):
    embedding = client.embeddings.create(
        input=[text.replace('\n', ' ')],
        model='text-embedding-ada-002')

    return embedding.data[0].embedding


embeddings = {}

with open('data.txt', 'r') as f:
    sum = f.read()
    chapters = sum.split('\n\n')

    for chapter in chapters:
        splitted = chapter.split('---')
        chapter_title = splitted[0].strip()
        chapter_text = splitted[1].strip()

        print(chapter_title)
        embeddings[chapter_title] = get_embedding(chapter_text)

with open('embeddings.json', 'w+') as f:
    json.dump(embeddings, f)
