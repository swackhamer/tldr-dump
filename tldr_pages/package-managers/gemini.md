# gemini

> Launch an interactive prompt with Gemini AI. More information: <https://github.com/google-gemini/gemini-cli>.

## Examples

### Start a REPL session to chat interactively

```bash
gemini
```

### Send the output of another command to Gemini and exit immediately

```bash
echo "Summarize the history of Rome" | gemini [-p|--prompt]
```

### Override the default model (default: gemini-2.5-pro)

```bash
gemini [-m|--model] gemini-2.5-flash
```

### Run inside a sandbox container

```bash
gemini [-s|--sandbox]
```

### Execute a prompt then stay in interactive mode

```bash
gemini [-i|--prompt-interactive] "Give me an example of recursion in Python"
```

### Include all files in context

```bash
gemini [-a|--all-files]
```

### Show memory usage in status bar

```bash
gemini --show-memory-usage
```
