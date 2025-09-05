# doppler-run

> Run a command with Doppler secrets injected into the environment. More information: <https://docs.doppler.com/docs/cli#run-a-command-with-secrets-populated-in-environment>.

## Examples

### Run a command

```bash
doppler run --command command
```

### Run multiple commands

```bash
doppler run --command command1 && command2
```

### Run a script

```bash
doppler run path/to/command.sh
```

### Run command with specified project and config

```bash
doppler run -p project_name -c config_name -- command
```

### Automatically restart process when secrets change

```bash
doppler run --watch command
```
