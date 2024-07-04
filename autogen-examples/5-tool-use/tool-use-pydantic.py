from pydantic import BaseModel, Field
from autogen import register_function
from typing import Annotated, Literal
import os
from autogen import ConversableAgent

ollama_config = {
    'config_list': [
        {
            'model': 'llama3',
            'temperature': 1.0,
            'api_key': 'llama3',  # Not needed
            'base_url': 'http://localhost:11434/v1'
        }
    ],
}

Operator = Literal["+", "-", "*", "/"]


class CalculatorInput(BaseModel):
    a: Annotated[int, Field(description="The first number.")]
    b: Annotated[int, Field(description="The second number.")]
    operator: Annotated[Operator, Field(description="The operator.")]


def calculator(input: Annotated[CalculatorInput, "Input to the calculator."]) -> int:
    if input.operator == "+":
        return input.a + input.b
    elif input.operator == "-":
        return input.a - input.b
    elif input.operator == "*":
        return input.a * input.b
    elif input.operator == "/":
        return int(input.a / input.b)
    else:
        raise ValueError("Invalid operator")


# Let's first define the assistant agent that suggests tool calls.
assistant = ConversableAgent(
    name="Assistant",
    system_message="You are a helpful AI assistant. "
    "You can help with simple calculations. "
    "Suggest a tool call 'calculator' when you need to calculate math operations."
    "Return 'TERMINATE' when the task is done.",
    llm_config=ollama_config,
)

# The user proxy agent is used for interacting with the assistant agent
# and executes tool calls.
user_proxy = ConversableAgent(
    name="User",
    llm_config=False,
    is_termination_msg=lambda msg: msg.get(
        "content") is not None and "TERMINATE" in msg["content"],
    human_input_mode="NEVER",
)

# Register the tool signature with the assistant agent.
assistant.register_for_llm(
    name="calculator", description="A simple calculator")(calculator)

# Register the tool function with the user proxy agent.
user_proxy.register_for_execution(name="calculator")(calculator)

# Print the assistant's tool list and schemas. Schemas are valid for OpenAI too.
print(assistant.llm_config["tools"])

chat_result = user_proxy.initiate_chat(
    assistant, message="What is (44232 + 13312 / (232 - 32)) * 5?", max_turns=2)
