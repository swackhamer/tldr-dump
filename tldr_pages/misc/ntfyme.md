# ntfyme

> A notification tool to track and notify you about your long-running termination process. Send notifications with success/error messages with Gmail, Telegram, and more. More information: <https://github.com/AnirudhG07/ntfyme>.

## Examples

### Directly run your command

```bash
ntfyme exec [-c|--cmd] command
```

### Pipe your command and run

```bash
echo command | ntfyme exec
```

### Run multiple commands by enclosing them in quotes

```bash
echo "command1; command2; command3" | ntfyme exec
```

### Track and terminate the process after prolonged suspension

```bash
ntfyme exec [-t|--track-process] [-c|--cmd] command
```

### Setup the tool configurations interactively

```bash
ntfyme setup
```

### Encrypt your password

```bash
ntfyme enc
```

### See the log history

```bash
ntfyme log
```

### Open and edit the configuration file

```bash
ntfyme config
```
