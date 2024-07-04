import os
from autogen import ConversableAgent
from autogen.coding import DockerCommandLineCodeExecutor

# generated files will be stored here
current_folder = os.getcwd()
tmp_folder = os.path.join(current_folder, 'tmp')

executor = DockerCommandLineCodeExecutor(
    image="python:3.12-slim",
    timeout=10,
    work_dir=tmp_folder,
)

code_executor_agent = ConversableAgent(
    "code_executor_agent",
    llm_config=False,
    code_execution_config={"executor": executor},
    # Always take human input for this agent for safety.
    human_input_mode="ALWAYS",
)

message_with_code_block = """This is a message with code block.
The code block is below:
```python
print('This is a simple code executed by LLM Agent from AutoGEN')
```
This is the end of the message.
"""

reply = code_executor_agent.generate_reply(
    messages=[{"role": "user", "content": message_with_code_block}])

print('Reply:', reply)

# When the code executor is no longer used, stop it to release the resources.
# executor.stop()
