import os
from openai import OpenAI
from dotenv import load_dotenv

# Get the API key and organization ID from the environment
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_ORG_ID = os.getenv('OPENAI_ORG_ID')

client = OpenAI()

# 5. Get the last fine-tuned model
ft_models = client.models.list()
ft_models_reverse = list(ft_models)[::-1]
last_fine_tuned_model_id = None

for ft_model in ft_models_reverse:
    if (ft_model.id.startswith('ft:')):
        last_fine_tuned_model_id = ft_model.id
        break

print('Last Fine-tuned Model:', last_fine_tuned_model_id)

# 6. Prompt the latest fine-tuned model
chat_completion = client.chat.completions.create(
    model=last_fine_tuned_model_id,
    messages=[
        {'role': 'user', 'content': 'What is my favorite music genre?'},
    ],
    temperature=1.0,
    seed=42
)

print('Chat Completion Message:', chat_completion.choices[0].message)

chat_completion = client.chat.completions.create(
    model=last_fine_tuned_model_id,
    messages=[
        {'role': 'user', 'content': 'Do you know my favorite hobby and a sport?'},
    ],
    temperature=1.0,
    seed=42
)

print('Chat Completion Message:', chat_completion.choices[0].message)
