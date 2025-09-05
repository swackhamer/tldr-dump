# qwen

> Launch an interactive prompt with Qwen3-Coder. See also: `gemini`. More information: <https://github.com/QwenLM/qwen-code>.

## Examples

### Start a REPL session to chat interactively

```bash
qwen
```

### Send the output of another command to Qwen and exit immediately

```bash
echo "Summarize the history of Rome" | qwen [-p|--prompt]
```

### Override the default model (default: qwen3-coder-max)

```bash
qwen [-m|--model] model_name
```

### Run inside a sandbox container

```bash
qwen [-s|--sandbox]
```

### Execute a prompt then stay in interactive mode

```bash
qwen [-i|--prompt-interactive] "Give me an example of recursion in Python"
```

### Include all files in context

```bash
qwen [-a|--all-files]
```

### Show memory usage in status bar

```bash
qwen --show-memory-usage
```
