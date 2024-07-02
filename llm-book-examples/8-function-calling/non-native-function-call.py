from ast import arguments
import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Get the API key and organization ID from the environment
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_ORG_ID = os.getenv('OPENAI_ORG_ID')

client = OpenAI()


def get_weather(city):
    # A real API call would go here
    print('Getting weather for:', city)

    return 'Sunny and 19 degrees, with 10% chance of rain in Tokyo.'


functions = {
    'get_weather': get_weather
}

chat_completion = client.chat.completions.create(
    model='gpt-4o',
    messages=[
        # system message with a function description
        {"role": "system", "content": "You are an AI personal assistant. You can call external functions to accomplish tasks or get more information. To call an external function, your respond is only JSON. The return value of the function will be made available to you. Only call the functions described next:"},
        {"role": "system", "content": "Function: get_weather - Gets the weather given a city name. Call this if you need to know the weather for a selected city. Arguments: city - city name as a string; returns a string with the weather description for the provided city."},

        # few-shot examples
        {"role": "user", "content": "What is the weather like today in Copenhagen?"},
        {"role": "assistant",
            "content": "{ \"name\": \"get_weather\", \"args\": { \"city\": \"Copenhagen\"} }"},
        {"role": "user", "name": "get_weather",
            "content": "Cloudy and 15 degrees, with no chance of rain in Copenhagen."},

        {"role": "user", "content": "What is the weather like today in Lviv?"},
        {"role": "assistant",
            "content": "{ \"name\": \"get_weather\", \"args\": { \"city\": \"Lviv\"} }"},
        {"role": "user", "name": "get_weather",
            "content": "Sunny and 20 degrees, with small change chance of rain in Lviv."},

        # actual user prompt
        {'role': 'user', 'content': 'What is the weather like today in Tokyo?'}
    ],
    temperature=0.0,
    seed=42
)

print('Chat Completion Message 2:', chat_completion.choices[0].message.content)

# get function name from the response

if 'get_weather' in chat_completion.choices[0].message.content:
    print('Function Call:', chat_completion.choices[0].message.content)

    json = json.loads(chat_completion.choices[0].message.content)

    print(json)

    # # Execute the function
    function_name = json['name']
    function_arguments = json['args']
    city = function_arguments['city']

    print('Function Name:', function_name)
    print('Function Arguments:', function_arguments)
    print('Function City:', city)

    # # Call the function
    fn_result = functions[function_name](city)

    print('Function Result:', fn_result)
