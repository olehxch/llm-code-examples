import os
from autogen import ConversableAgent

ollama_config = {
    'config_list': [
        {
            'model': 'llama3',
            'temperature': 0.0,
            'api_key': 'llama3',  # Not needed
            'base_url': 'http://localhost:11434/v1'
        }
    ],
}

agent_pm = ConversableAgent(
    'Project Manager',
    system_message="""
    Your are a project manager for a software application. 
    You communicate with backend developer. 
    Your provide tasks and requirements to the backend developer. 
    """,
    llm_config=ollama_config,
    code_execution_config=False,
    function_map=None,
    human_input_mode='NEVER',
)

agent_dev = ConversableAgent(
    'Backend Developer',
    system_message="""
    Your are a backend developer for a software application. 
    You communicate with project manager. 
    Your provide estimates in hours for the received tasks.
    """,
    llm_config=ollama_config,
    code_execution_config=False,
    function_map=None,
    human_input_mode='NEVER',
)

initial_message = 'Your task is to implement simple backend microservice that has one REST API endpoint that returns "Hello World" test message. The microservice should be implemented in Node.js using Express.js framework.'
result = agent_pm.initiate_chat(
    agent_dev, message=initial_message, max_turns=5)
