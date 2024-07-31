# LLMs: Code Examples

🚀 This repository contains various code examples with methods and approaches to work with LLMs from my learning and personal experience.

🎓 You are free to use these code examples for educational or work purposes. Please credit all book and supplementary material authors if you use their code examples, figures, pictures or citations.

⚡️ You can subscribe to my Medium account to read articles about artificial intelligence, cloud computing, state-of-the-art technologies, and also audio engineering! Here is a link:

[My Articles on Medium](https://medium.com/@olehch)

🙌 This collection was created by Oleh Chaplia and is constantly updated.

## Table of Contents

- [OpenAI with ChromaDB](#openai-with-chromadb)
- [AutoGEN with Ollama](#autogen-with-ollama)
- [Nvidia NIM](#nvidia-nim)

## OpenAI with ChromaDB

These examples covered from an awesome book on developing applications based on LLMs titled *"Large Language Models at Work: Enhancing Software Systems with Language Models"*. This book covers many development topics and usage cases. Most of the code examples are provided in the next sections.

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

[Chromadb](https://www.trychroma.com) is used for storing text embeddings.

[Vector Database Code Examples](/llm-book-examples/7-vector-database/)

### Function Calling

Function calling for Large Language Models refers to the capability of these models to execute predefined functions or APIs. This enhances the model's utility by allowing it to perform specific tasks, such as interfacing with external systems.

[Vector Database Code Examples](/llm-book-examples/8-function-calling/)

### Function Libraries inside Vector Database

To handle token limits efficiently, we use memory by storing all available functions in a vector database indexed by description embeddings. Instead of including all functions in a completion call, we select a subset of the most relevant functions based on the user's request. Relevance is determined by measuring the cosine distance between embeddings, ensuring that only the necessary functions are used, optimizing performance and reducing token consumption.

[Chromadb](https://www.trychroma.com) is used for storing function embeddings.

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

> [**ConversableAgent**](https://microsoft.github.io/autogen/docs/reference/agentchat/conversable_agent/#conversableagent) is a class for generic conversable agents which can be configured as assistant or user proxy.


> [**UserProxyAgent**](https://microsoft.github.io/autogen/docs/tutorial/code-executors#user-proxy-agent) class is a subclass of ConversableAgent with human_input_mode=ALWAYS and llm_config=False – it always requests human input for every message and does not use LLM. It also comes with default description field for each of the human_input_mode setting. This class is a convenient short-cut for creating an agent that is intended to be used as a code executor.

> [**AssistantAgent**](https://microsoft.github.io/autogen/docs/tutorial/code-executors#assistant-agent) class is a subclass of ConversableAgent with human_input_mode=NEVER and code_execution_config=False – it never requests human input and does not use code executor. It also comes with default system_message and description fields. This class is a convenient short-cut for creating an agent that is intended to be used as a code writer and does not execute code.


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

[Code Executors Code Examples](/autogen-examples/4-code-executors/)

> The choice between command line and Jupyter code executor depends on the nature of the code blocks in agents’ conversation. If each code block is a “script” that does not use variables from previous code blocks, the command line code executor is a good choice. If some code blocks contain expensive computations (e.g., training a machine learning model and loading a large amount of data), and you want to keep the state in memory to avoid repeated computations, the Jupyter code executor is a better choice.
>
> --- [Command Line or Jupyter Code Executor?](https://microsoft.github.io/autogen/docs/tutorial/code-executors#command-line-or-jupyter-code-executor)

### Tool Use

Tools are pre-defined functions that agents use to perform specific actions like web searches, calculations, file reading, or API calls. By controlling the available tools, you can manage the actions an agent can execute.

> Tool use is currently only available for LLMs that support OpenAI-compatible tool call API.
>
> --- [Tool Use Note](https://microsoft.github.io/autogen/docs/tutorial/tool-use)

[Tool Use Code Examples](/autogen-examples/5-tool-use/)

### Conversation Patterns

There are several [conversation patterns](https://microsoft.github.io/autogen/docs/tutorial/conversation-patterns#an-overview) for agents: 

1. [**Two-agent chat:**](https://microsoft.github.io/autogen/docs/tutorial/conversation-patterns#two-agent-chat-and-chat-result) Simple interaction between two agents.
2. [**Sequential chat:**](https://microsoft.github.io/autogen/docs/tutorial/conversation-patterns#sequential-chats) A series of chats between two agents, with summaries from previous chats carried over to the next.
3. [**Group chat:**](https://microsoft.github.io/autogen/docs/tutorial/conversation-patterns#group-chat) Involving more than two agents, with strategies for selecting the next speaker such as round-robin, random, manual, and auto (agent decides). Custom functions can also determine the next speaker to create deterministic workflows.
4. [**Nested chat:**](https://microsoft.github.io/autogen/docs/tutorial/conversation-patterns#nested-chats) Embedding a workflow within a single agent for reuse in larger workflows.

[Conversation Patterns Code Examples](/autogen-examples/6-conversation-patterns/)

## Nvidia NIM

> Instantly Deploy Generative AI With NVIDIA NIM
> 
> Explore the latest community-built AI models with an API optimized and accelerated by NVIDIA, then deploy anywhere with NVIDIA NIM inference microservices.
>
> Part of NVIDIA AI Enterprise, NVIDIA NIM is a set of easy-to-use inference microservices for accelerating the deployment of foundation models on any cloud or data center and helping to keep your data secure.
>
> --- [Nvidia AI](https://www.nvidia.com/en-us/ai/)

Nvidia provides APIs for accessing various LLMs, implement integrations. Nvidia NIM inference microservice API is compatible with OpenAI API.

[NVIDIA NIM Offers Optimized Inference Microservices for Deploying AI Models at Scale](https://developer.nvidia.com/blog/nvidia-nim-offers-optimized-inference-microservices-for-deploying-ai-models-at-scale/)

[A list of Nvidia LLM models](https://docs.api.nvidia.com/nim/reference/nvidia-nemotron-4-340b-reward)

Before using these code examples please create `.env` file inside each folder. For these examples please use Nvidia API Key generated from the main page.

```
OPENAI_API_KEY=<YOUR_KEY>
```

### Reasoning and Text Generation

Here are basic examples of prompt execution with and without response streaming. 
Nvidia NIM APIs are the same as in OpenAI.

- [llama3-70b-instruct](https://build.nvidia.com/meta/llama3-70b/modelcard) powers complex conversations with superior contextual understanding, reasoning and text generation.
- [mixtral-8x7b-instruct-v0.1](https://build.nvidia.com/mistralai/mixtral-8x7b-instruct/modelcard) is an MOE LLM that follows instructions, completes requests, and generates creative text.
- [mistral-large](https://build.nvidia.com/mistralai/mistral-large/modelcard) excels in complex multilingual reasoning tasks, including text understanding, and code generation.
- [gemma-2-27b-it](https://build.nvidia.com/google/gemma-2-27b-it/modelcard) is a cutting-edge text generation model text understanding, transformation, and code generation.
- [phi-3-mini-128k-instruct](https://build.nvidia.com/microsoft/phi-3-mini/modelcard) is lightweight, state-of-the-art open LLM with strong math and logical reasoning skills.
- [solar-10.7b-instruct](https://build.nvidia.com/upstage/solar-10_7b-instruct/modelcard) excels in NLP tasks, particularly in instruction-following, reasoning, and mathematics.

[Basic Prompt Execution Code Examples](/nvidia-examples/0-basic-prompt-execution/)


### Code Generation

Here are some examples of prompt execution that generates source code in Python and JavaScript languages. 

- [starcoder2-15b](https://build.nvidia.com/bigcode/starcoder2-15b) is an advanced programming model for code completion, summarization, and generation
- [codestral-22b-instruct-v0.1](https://build.nvidia.com/mistralai/codestral-22b-instruct-v01/modelcard) is a model for writing and interacting with code across a wide range of programming languages and tasks.
- [granite-34b-code-instruct](https://build.nvidia.com/ibm/granite-34b-code-instruct/modelcard) is a software programming LLM for code generation, completion, explanation, and multi-turn conversion.
- [codegemma-1.1-7b](https://build.nvidia.com/google/codegemma-1-1-7b/modelcard) is an advanced programming model for code generation, completion, reasoning, and instruction following.
- [deepseek-coder-6.7b-instruct](https://build.nvidia.com/deepseek-ai/deepseek-coder-6_7b-instruct/modelcard) is a powerful coding model offering advanced capabilities in code generation, completion, and infilling.
- [codellama-70b](https://build.nvidia.com/meta/codellama-70b/modelcard) is an LLM capable of generating code from natural language and vice versa.
- [arctic](https://build.nvidia.com/snowflake/arctic/modelcard) delivers high efficiency inference for enterprise applications focused on SQL generation and coding.
- [nemotron-4-340b-instruct](https://build.nvidia.com/nvidia/nemotron-4-340b-instruct/modelcard) creates diverse synthetic data that mimics the characteristics of real-world data.

[Code Generation Code Examples](/nvidia-examples/1-code-generation/)


### Recognize Content in Images with Vision Models

Here are some examples of recognizing the content in the images.

- [Kosmos-2](https://build.nvidia.com/microsoft/microsoft-kosmos-2/modelcard) model is a groundbreaking multimodal model designed to understand and reason about visual elements in images.
- [neva-22b](https://build.nvidia.com/nvidia/neva-22b/modelcard) is a multi-modal vision-language model that understands text/images and generates informative responses
- [deplot](https://build.nvidia.com/google/google-deplot/modelcard) is a one-shot visual language understanding 
model that translates images of plots into tables.
- [fuyu-8b](https://build.nvidia.com/adept/fuyu-8b/modelcard) is a multi-modal model for a wide range of tasks, including image understanding and language generation.
- [llava-v1.6-34b](https://build.nvidia.com/liuhaotian/llava16-34b/modelcard) is a multi-modal vision-language model that understands text/images and generates informative responses.

[Recognize Content in Images Code Examples](/nvidia-examples/1-code-generation/)

### Generate High-Quality Embeddings

Here are some examples with models that generate embeddings used for the data retrieval and similarity search.

- [bge-m3](https://build.nvidia.com/baai/bge-m3/modelcard) is an embedding model for text retrieval tasks, excelling in dense, multi-vector, and sparse retrieval.
- [embed-qa-4](https://build.nvidia.com/nvidia/embed-qa-4/modelcard) is a GPU-accelerated generation of text embeddings used for question-answering retrieval.
- [nv-embed-v1](https://build.nvidia.com/nvidia/nv-embed-v1/modelcard) generates high-quality numerical embeddings from text inputs.
- [rerank-qa-mistral-4b](https://build.nvidia.com/nvidia/rerank-qa-mistral-4b/modelcard) is a GPU-accelerated model optimized for providing a probability score that a given passage contains the information to answer a question.
- [arctic-embed-l](https://build.nvidia.com/snowflake/arctic-embed-l/modelcard) is a GPU-accelerated generation of text embeddings.

