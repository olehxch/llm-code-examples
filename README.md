# LLMs: Code Examples

🚀 This repository contains various code examples with methods and approaches to work with LLMs from my learning and personal experience.

🎓 You are free to use these code examples for educational or work purposes. Please credit all book and supplementary material authors if you use their code examples, figures, pictures or citations.

## Table of Contents

- [Large Language Models at Work: Enhancing Software Systems with Language Models](#large-language-models-at-work-enhancing-software-systems-with-language-models)
- [AutoGEN with Ollama](#autogen-with-ollama)

## Large Language Models at Work: Enhancing Software Systems with Language Models

This is an awesome book on developing applications based on LLMs. This book covers many development topics and usage cases. Most of the code examples are provided in the next sections.

[Large Language Models at Work: Enhancing Software Systems with Language Models by Vlad Rișcuția](https://vladris.com/llm-book)

Before using these code examples please create `.env` file inside each folder. For these examples I use OpenAI APIs and ChatGPT models.

```
OPENAI_API_KEY=<YOUR_KEY>
OPENAI_ORG_ID=<YOUR_ORG_ID>
```

### A Few Words About Prompts

The industry is still refining the best prompt strategies for large language models, but a good prompt generally includes several key elements. These elements are specifying the role for the model, providing additional context, identifying the target audience, describing the desired output format, giving instructions on how to generate the output, offering examples to illustrate expectations, and ensuring proper syntax with correct grammar and punctuation.

### Basic Prompt Execution

Large Language Model (LLM) is a model trained on massive datasets containing diverse text sources, allowing it to learn language patterns, context, grammar, and even subtle nuances. LLMs can perform a wide range of natural language processing tasks, including text completion, translation, summarization, and question answering. It processes and generates human-like text based on the input it receives.

Completion refers to the generation of text based on a given prompt. Chat completion, involves an interactive, conversational format where the model retains the context of the ongoing conversation. The model generates responses that are coherent with previous exchanges, making it suitable for dialogue systems, customer support, and interactive applications.

[Basic Prompt Execution Code Examples](/llm-book-examples/0-basic-prompt-execution/)

### Zero-Shot Learning
Zero-Shot Learning refers to an approach, where LLM can generate the answer even when it was not trained to answer these questions before. Instead, the model uses semantic information, such as descriptions or attributes, to make inferences about these unseen classes.

[Zero Shot Learning Code Examples](/llm-book-examples/1-zero-shot-learning/)

### One-Shot Learning
One-Shot Learning involves providing one example of the correct answer in the prompt. This is particularly useful in scenarios where data collection is expensive or impractical. The model leverages prior knowledge and learning techniques to generalize from this single example effectively.

[One Shot Learning Code Examples](/llm-book-examples/2-one-shot-learning/)

### Few-Shot Learning
Few-Shot Learning is a broader approach where the model learns to make predictions with only a few examples of each category within the prompt.

[Few Shot Learning Code Examples](/llm-book-examples/3-few-shot-learning/)

### Fine-tuning

Fine-tuning is a process where a pre-trained model is further trained on a specific dataset to adapt it to a particular task or domain. This approach leverages the extensive knowledge the model has already acquired during its initial training on large, diverse datasets, thus requiring less data and computational resources for the additional training. Fine-tuning adjusts the model's weights to better align with the specific nuances and requirements of the new task, enhancing its performance in that context.

[Fine-Tuning Code Examples](/llm-book-examples/4-fine-tuning/)

### Memory

Memory in machine learning refers to a model’s ability to retain and utilize information from previous interactions. This capability allows the model to maintain context over multiple exchanges, making it essential for tasks like chatbots and virtual assistants. By remembering past inputs and outputs, models can produce coherent and contextually appropriate responses, significantly enhancing user experience and interaction quality.

[Memory Code Examples](/llm-book-examples/5-memory/)

### Embeddings

Embeddings are high-dimensional vector representations of words, phrases, or documents that capture their semantic meanings and relationships. By converting textual data into numerical vectors, embeddings enable models to understand and process language in a more nuanced way. This technique is crucial for tasks such as similarity detection, sentiment analysis, and language translation, allowing AI systems to perform these tasks with greater accuracy and efficiency.

[Embeddings Code Examples](/llm-book-examples/6-embeddings/)

### Vector Databases

Vector databases are specialized databases designed to store, index, and query high-dimensional vectors efficiently. These vectors often represent complex data types such as images, text, or embeddings from machine learning models. Vector databases enable rapid similarity searches, making them ideal for applications in recommendation systems, natural language processing, image retrieval, and more.

[Vector Database Code Examples](/llm-book-examples/7-vector-database/)

### Function Calling

Function calling for Large Language Models refers to the capability of these models to execute predefined functions or APIs. This enhances the model's utility by allowing it to perform specific tasks, such as interfacing with external systems.

[Vector Database Code Examples](/llm-book-examples/8-function-calling/)

### Function Libraries inside Vector Database

To handle token limits efficiently, we use memory by storing all available functions in a vector database indexed by description embeddings. Instead of including all functions in a completion call, we select a subset of the most relevant functions based on the user's request. Relevance is determined by measuring the cosine distance between embeddings, ensuring that only the necessary functions are used, optimizing performance and reducing token consumption.

[Function Libraries inside Vector Database Code Examples](/llm-book-examples/9-functions-vector-database/)

### Multiple Steps Planning

Multiple steps planning for Large Language Models involve strategic steps to ensure efficient task execution. At first, the complex task is divided into smaller chunks and then each subtask is executed, results are gathered, summarized and forwarded to the next tasks where needed. Having a good execution plan provides better results and correctness of the responses.

[Multiple Steps Planning Code Examples](/llm-book-examples/10-multiple-steps-planning/)

### Auto-Generated Plans

Auto-generated plans created by Large Language Models automate the process of plan creation. These models can analyze input data, user requirements, and specific goals to generate comprehensive and detailed plans. By automating plan creation, LLMs enhance efficiency, reduce manual effort, and ensure consistency and accuracy in the planning process.

[Auto-Generated Plans Code Examples](/llm-book-examples/11-auto-generated-plans/)

### LLM Hallucinations

LLM hallucinations refer to instances where they generate information that is incorrect, misleading, or entirely fabricated, despite being presented in a plausible and confident manner. These hallucinations occur because LLMs predict text based on patterns in the data they were trained on, rather than verifying facts against a reliable knowledge base. Such inaccuracies can be problematic, particularly in contexts requiring high precision, such as legal, medical, or technical fields.

[LLM Hallucinations Code Examples](/llm-book-examples/12-hallucinations/)

### Explainable AI

Explainable AI, also known as Interpretable AI, refers to artificial intelligence systems that allow humans to understand the reasoning behind their decisions or predictions. This contrasts with black box models, where even designers cannot explain the AI's conclusions.

[Explainable AI Code Examples](/llm-book-examples/13-explainable-ai/)

### Prompt Injection

Prompt injection is a technique used to manipulate the output of a language model by strategically crafting input prompts. This method exploits the model's tendency to generate responses based on the given context, allowing users to influence the AI to produce specific results or behave in certain ways. Prompt injection can be used for various purposes, such as guiding the model to follow a desired format, and maliciously, to coerce the AI into generating inappropriate or harmful content.

[Prompt Injection Code Examples](/llm-book-examples/14-prompt-injection/)

### Prompt Leaking

In a large language model-based solution, a prompt is dynamically constructed from multiple components, including user input, instructions, memories retrieved from external storage like vector databases, and few-shot examples. While users provide the input, they typically do not see the entire prompt sent to the model. Prompt leaking is a form of prompt injection where an attacker manipulates the model to reveal details of the prompt, potentially exposing confidential or proprietary information.

[Prompt Leaking Code Examples](/llm-book-examples/15-prompt-leaking/)

### Jailbreaking

Large language models have content policies to restrict users from asking about illegal or harmful topics Jailbreaking is a type of prompt injection that attempts to bypass these content policies, causing the model to generate disallowed output.

[Jailbreaking Code Examples](/llm-book-examples/16-jailbreaking/)

## AutoGEN with Ollama

The *AutoGEN* is an open-source programming framework for agentic AI. It implements all necessary approaches and tools for easy implementation of AI agents based on various LLMs. 

*Ollama* is an open-source tool for running LLM models locally. Ollama model library contains many modern LLM models including Llama3, Phi3, StarCoder and others. Models are running locally without the need of external connections.

### A few notes about agent types

> **ConversableAgent** is a class for generic conversable agents which can be configured as assistant or user proxy.
>
> --- [Conversable Agent](https://microsoft.github.io/autogen/docs/reference/agentchat/conversable_agent/#conversableagent)


> **UserProxyAgent** class is a subclass of ConversableAgent with human_input_mode=ALWAYS and llm_config=False – it always requests human input for every message and does not use LLM. It also comes with default description field for each of the human_input_mode setting. This class is a convenient short-cut for creating an agent that is intended to be used as a code executor.
>
> --- [User Proxy Agent](https://microsoft.github.io/autogen/docs/tutorial/code-executors#user-proxy-agent)

> **AssistantAgent** class is a subclass of ConversableAgent with human_input_mode=NEVER and code_execution_config=False – it never requests human input and does not use code executor. It also comes with default system_message and description fields. This class is a convenient short-cut for creating an agent that is intended to be used as a code writer and does not execute code.
>
> --- [Assistant Agent](https://microsoft.github.io/autogen/docs/tutorial/code-executors#assistant-agent)


### Basic Prompt Execution

This example implements one agent, executes one prompt and prints the result. Ollama is used as LLM model host.

[Basic Prompt Execution Code Examples](/autogen-examples/0-basic-prompt-execution/)

### Two Conversational Agents

This example implements two conversational agents with a simple task - to provide an estimate for a simple Hello World microservice. 

[Two Conversational Agents Code Examples](/autogen-examples/1-two-agents/)

### Terminating Conversations Between Agents

This code provides two examples how to terminate the chat between the agents by using `max_consecutive_auto_reply` and `is_termination_msg` properties.

[Terminating Conversations Between Agents Code Examples](/autogen-examples/2-terminating-conversation/)

### Human Input Modes

Human input is a way of interacting with agents based on asking the human to enter the text in the terminal. These examples show how to use `human_input_mode` property with three values - `NEVER`, `TERMINATE` and `ALWAYS`. 

In `NEVER` mode human input is never requested. Agents act fully autonomous. In `TERMINATE` mode human input is only requested when a termination condition is met. When human replies in this mode, `max_consecutive_auto_reply` counter is reset. In `ALWAYS` mode human input is always requested. In this mode `max_consecutive_auto_reply` is ignored.

[Human Input Modes Code Examples](/autogen-examples/3-human-input/)

### Code Executors

A code executor processes input messages containing code, executes the code, and outputs the results. AutoGEN offers two built-in executors: a command line executor for running code in environments like a UNIX shell and a Jupyter executor for interactive Jupyter kernels. Each executor can execute code locally on the host platform or within a Docker container. Local execution is suitable for development and testing, while Docker container execution is preferred for production to handle arbitrary code safely.

> Executing LLM-generated code locally poses a security risk to your host environment.

> The choice between command line and Jupyter code executor depends on the nature of the code blocks in agents’ conversation. If each code block is a “script” that does not use variables from previous code blocks, the command line code executor is a good choice. If some code blocks contain expensive computations (e.g., training a machine learning model and loading a large amount of data), and you want to keep the state in memory to avoid repeated computations, the Jupyter code executor is a better choice.
>
> --- [Command Line or Jupyter Code Executor?](https://microsoft.github.io/autogen/docs/tutorial/code-executors#command-line-or-jupyter-code-executor)

[Code Executors Code Examples](/autogen-examples/4-code-executors/)
