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

agent = ConversableAgent(
    'chatbot',
    llm_config=ollama_config,
    code_execution_config=False,
    function_map=None,
    human_input_mode='NEVER',
)

reply = agent.generate_reply(
    messages=[{'role': 'user', 'content': 'What is an LLM?'}])
print(reply)
