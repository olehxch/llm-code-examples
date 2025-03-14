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

    return 'Sunny and 75 degrees, with 10% chance of rain in Tokyo.'


functions = {
    'get_weather': get_weather
}

chat_completion = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {'role': 'user', 'content': 'What is the weather like today in Tokyo?'}
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

# Get finish reason
print('Finish Reason:', chat_completion.choices[0].finish_reason)

if (chat_completion.choices[0].finish_reason == 'function_call'):
    print('Function Call:', chat_completion.choices[0].message.function_call)
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
        {'role': 'user', 'content': 'What is the weather like today in Tokyo?'},
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
