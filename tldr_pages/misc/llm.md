# llm

> Interact with Large Language Models (LLMs) via remote APIs and models that can be installed and run on your machine. More information: <https://llm.datasette.io/en/stable/help.html>.

## Examples

### Set up an OpenAI API Key

```bash
llm keys set openai
```

### Run a prompt

```bash
llm "Ten fun names for a pet pelican"
```

### Run a system prompt against a file

```bash
cat path/to/file.py | llm [-s|--system] "Explain this code"
```

### Install packages from PyPI into the same environment as LLM

```bash
llm install package1 package2 ...
```

### Download and run a prompt against a model

```bash
llm [-m|--model] orca-mini-3b-gguf2-q4_0 "What is the capital of France?"
```

### Create a system prompt and save it with a template name

```bash
llm [-s|--system] 'You are a sentient cheesecake' --save sentient_cheesecake
```

### Have an interactive chat with a specific model using a specific template

```bash
llm chat [-m|--model] chatgpt [-t|--template] sentient_cheesecake
```
