import os
from openai import OpenAI
from dotenv import load_dotenv

# Get the API key and organization ID from the environment
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_ORG_ID = os.getenv('OPENAI_ORG_ID')

client = OpenAI()

goal = 'Write a novel consisting of multiple chapters, with a complex plot and multiple characters on the theme of AI ethics.'
plan = [
    {'Step': 'Step 1: Brainstorm ideas for a complex plot that explores the ethical implications of AI.', 'Recall': []},
    {'Step': 'Step 2: Create a detailed outline for the novel, noting the key plot points, character arcs, and themes.',
        'Recall': ['Step 1']},
    {'Step': 'Step 3: Create a list of main and secondary characters, giving each a unique personality, background, and motivations.',
        'Recall': ['Step 2']},
    {'Step': 'Step 4: Write Chapter 1, focusing on introducing the world, the main characters, and setting up the ethical dilemma.',
        'Recall': ['Step 2', 'Step 3']},
    {'Step': 'Step 5: Write Chapter 2, highlighting the ethical challenges faced by the characters and the conflicts arising from AI decisions.',
        'Recall': ['Step 2', 'Step 3', 'Step 4']},
    {'Step': 'Step 6: Write Chapter 3, focusing on character growth and escalating the conflicts related to AI ethics.',
        'Recall': ['Step 2', 'Step 3', 'Step 5']},
    {'Step': 'Step 7: Write Chapter 4, incorporating unexpected plot twists and deepening the ethical dilemmas faced by the characters.',
        'Recall': ['Step 2', 'Step 3', 'Step 6']},
    {'Step': 'Step 8: Write Chapter 5, intensifying the ethical conflicts, forcing characters to make difficult choices.',
        'Recall': ['Step 2', 'Step 3', 'Step 7']},
    {'Step': 'Step 9: Write Chapter 6, ratcheting up the suspense and focusing on the ethical reckoning at hand.',
        'Recall': ['Step 2', 'Step 3', 'Step 8']},
    {'Step': 'Step 10: Write Chapter 7, culminating in a high-stakes confrontation that tests the characters\' convictions.',
        'Recall': ['Step 2', 'Step 3', 'Step 9']},
    {'Step': 'Step 11: Write Chapter 8, resolving the ethical conflicts, addressing character arcs, and offering closure.', 'Recall': ['Step 2', 'Step 3', 'Step 10']}]

memory = {}
chat = []
for i, step in enumerate(plan):
    prompt = []
    prompt.append({'role': 'user', 'content': goal})

    for recall in step['Recall']:
        memory_recall = memory.get(recall)

        if memory_recall:
            print('Recall:', recall, memory_recall)
            prompt.append(
                {'role': 'user', 'content': f'Here is some information that will help you: {memory_recall}'})
    prompt.append({'role': 'user', 'content': step['Step']})

    print('Prompt', prompt)

    chat_completion = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=prompt,
        temperature=0.1,
        seed=42
    )

    # execute prompt
    message = chat_completion.choices[0].message
    print(message.content)
    print('-------')

    # save response to memory
    memory[f'Step {i+1}'] = message.content
