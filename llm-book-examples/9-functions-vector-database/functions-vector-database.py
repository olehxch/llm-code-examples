import os
import json
from openai import OpenAI
from dotenv import load_dotenv
import chromadb
from chromadb.utils import embedding_functions

# Get the API key and organization ID from the environment
load_dotenv(override=True)
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_ORG_ID = os.getenv('OPENAI_ORG_ID')

client = OpenAI()


def get_embedding(text):
    embedding = client.embeddings.create(
        input=[text.replace('\n', ' ')],
        model='text-embedding-ada-002')

    return embedding.data[0].embedding


def get_weather(city):
    # A real API call would go here
    print('Getting weather for:', city)

    return 'Sunny and 75 degrees, with 10% chance of rain in ' + city


functions = {
    'get_weather': get_weather
}

# Initialize the database
chroma_client = chromadb.PersistentClient('db')

list_collections = chroma_client.list_collections()
print('List collections', list_collections)

if 'functions' in list_collections:
    print('Deleting functions collection')
    chroma_client.delete_collection('functions')

collection = chroma_client.get_or_create_collection(
    'functions',
    embedding_function=embedding_functions.OpenAIEmbeddingFunction(
        api_key=OPENAI_API_KEY,
        model_name="text-embedding-ada-002"
    ))

# Create embedding for the function description
with open('./llm-book-examples/9-functions-vector-database/get_weather.json', 'r') as f:
    function = json.load(f)
    function_str = json.dumps(function)

    function_name = function['name']
    function_description = function['description']

    # Get the embedding for the function description
    embedding = get_embedding(function_description)

    print('Function:', function)
    collection.add(documents=[function_str],
                   ids=[function_name],
                   embeddings=[embedding])

print('Count collections', chroma_client.count_collections())
print('Number of embeddings:', collection.count())


while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    # query top 3 nearest functions for the prompt
    query_result = collection.query(query_texts=prompt, n_results=3)
    query_documents = query_result['documents']
    fns = [json.loads(doc) for doc in query_documents[0]]

    print('Found function:', fns)

    chat_completion = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'user', 'content': prompt}
        ],
        functions=fns,
        temperature=0.1,
        seed=42
    )

    # Get finish reason
    print('Finish Reason:', chat_completion.choices[0].finish_reason)

    if (chat_completion.choices[0].finish_reason == 'function_call'):
        print('Function Call:',
              chat_completion.choices[0].message.function_call)
    else:
        print('Chat Completion:', chat_completion)
        print('Chat Completion Message:', chat_completion.choices[0].message)

    # Execute the function
    function_name = chat_completion.choices[0].message.function_call.name
    function_arguments = json.loads(
        chat_completion.choices[0].message.function_call.arguments)
    city = function_arguments['city']

    print('Function Name:', function_name)
    print('Function Arguments:', function_arguments)
    print('Function City:', city)

    # Call the function
    fn_result = functions[function_name](city)

    # Pass back the results of the function call
    chat_completion2 = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'user', 'content': prompt},
            {'role': 'function', 'name': function_name, 'content': fn_result},
        ],
        functions=[{
            "name": "get_weather",
            "description": "Gets the weather given a city name",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string"}}
            }
        }],
        temperature=0.0,
        seed=42
    )

    # print('Finish Reason 2:', chat_completion2)
    print('Chat Completion Message 2:',
          chat_completion2.choices[0].message.content)
