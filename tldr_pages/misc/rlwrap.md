# rlwrap

> Add line editing, persistent history and prompt completion to a REPL command. More information: <https://manned.org/rlwrap>.

## Examples

### Run a REPL command with line editing, persistent history and prompt completion

```bash
rlwrap command
```

### Use all words seen on input and output for prompt completion

```bash
rlwrap [-r|--remember] command
```

### Better prompt completion if prompts contain ANSI colour codes

```bash
rlwrap [-A|--ansi-colour-aware] command
```

### Enable filename completion (case sensitive)

```bash
rlwrap [-c|--complete-filenames] command
```

### Add coloured prompts, use colour name, or an ASCI-conformant colour specification. Use an uppercase colour name for bold styling

```bash
rlwrap [-p|--prompt-colour=]black|red|green|yellow|blue|cyan|purple|white|colour_spec command
```
