import chromadb
from chromadb.utils import embedding_functions
import os
from openai import OpenAI
from dotenv import load_dotenv

# Get the API key and organization ID from the environment
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_ORG_ID = os.getenv('OPENAI_ORG_ID')

client = OpenAI()
chroma_client = chromadb.PersistentClient('db')

chroma_client.delete_collection('stories')
collection = chroma_client.get_or_create_collection(
    'stories',
    embedding_function=embedding_functions.OpenAIEmbeddingFunction(
        api_key=OPENAI_API_KEY,
        model_name="text-embedding-ada-002"
    ))

with open('data.txt', 'r') as f:
    sum = f.read()
    chapters = sum.split('\n\n')

    for chapter in chapters:
        splitted = chapter.split('---')
        chapter_title = splitted[0].strip()
        chapter_text = splitted[1].strip()

        collection.add(documents=[chapter_text], ids=[chapter_title])

print('Count collections', chroma_client.count_collections())
print('Number of embeddings:', collection.count())


while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    query_result = collection.query(query_texts=prompt, n_results=1)
    chapter_text = query_result['documents'][0][0]

    print('Found nearest chapter:', chapter_text)

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
