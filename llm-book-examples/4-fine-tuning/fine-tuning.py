import os
from openai import OpenAI
from dotenv import load_dotenv

# Get the API key and organization ID from the environment
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_ORG_ID = os.getenv('OPENAI_ORG_ID')

client = OpenAI()


def find_file_by_name(sync_page, filename='dataset.jsonl'):
    for file_object in sync_page.data:
        if file_object.filename == filename:
            return file_object
    return None


# 1. Upload a training file
files = client.files.list(purpose='fine-tune')
dataset_file = find_file_by_name(files)

if (dataset_file is None):
    dataset_file = client.files.create(
        file=open('./llm-book-examples/4-fine-tuning/dataset.jsonl', 'rb'),
        purpose='fine-tune'
    )

print('File:', dataset_file)
print('File id:', dataset_file.id)

# 2. Create a fine-tuned model
fine_tuning_job = client.fine_tuning.jobs.create(
    training_file=dataset_file.id,
    model='gpt-3.5-turbo'
)

print('Fine-tuning Job:', fine_tuning_job)

# 3. Wait for the fine-tuning job to complete
jobs = client.fine_tuning.jobs.list()

for job in jobs:
    print('Job:', job.id, job.status, job.training_file, job.fine_tuned_model)

# 4. Get fine-tuned model id from 'job.fine_tuned_model' and use it for prompts
# 5. List all fine-tuned models
ft_models = client.models.list()

for ft_model in ft_models:
    if (ft_model.id.startswith('ft:')):
        print('Fine-tuned Model:', ft_model.id)

        # client.models.delete(ft_model.id)

# Fine-tuning models from OpenAI - gpt-3.5-turbo, davinci-002, babbage-002
# Check a list of available models for tuning here:
# https://openai.com/api/pricing/
