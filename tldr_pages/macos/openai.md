# openai

> CLI tool providing access to the OpenAI API. More information: <https://github.com/openai/openai-python>.

## Examples

### List models

```bash
openai api models.list
```

### Create a completion

```bash
openai api completions.create --model ada --prompt "Hello world"
```

### Create a chat completion

```bash
openai api chat_completions.create --model gpt-3.5-turbo --message user "Hello world"
```

### Generate images via DALL·E API

```bash
openai api image.create --prompt "two dogs playing chess, cartoon" --num-images 1
```
