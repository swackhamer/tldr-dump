# chatgpt

> Shell script to use OpenAI's ChatGPT and DALL-E from the terminal. More information: <https://github.com/0xacx/chatGPT-shell-cli>.

## Examples

### Start in chat mode

```bash
chatgpt
```

### Give a prompt to answer to

```bash
chatgpt [-p|--prompt] "What is the regex to match an email address?"
```

### Start in chat mode using a specific model (default is `gpt-3.5-turbo`)

```bash
chatgpt [-m|--model] gpt-4
```

### Start in chat mode with an initial prompt

```bash
chatgpt [-i|--init-prompt] "You are Rick, from Rick and Morty. Respond to questions using his mannerism and include insulting jokes."
```

### Pipe the result of a command to `chatgpt` as a prompt

```bash
echo "How to view running processes on Ubuntu?" | chatgpt
```

### Generate an image using DALL-E

```bash
chatgpt [-p|--prompt] "image: A white cat"
```
