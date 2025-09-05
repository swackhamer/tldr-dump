# doppler

> Manage environment variables across different environments using Doppler. Some subcommands such as `run` and `secrets` have their own usage documentation. More information: <https://docs.doppler.com/docs/cli>.

## Examples

### Setup Doppler CLI in the current directory

```bash
doppler setup
```

### Setup Doppler project and configuration in current directory

```bash
doppler setup
```

### Run a command with secrets injected into the environment

```bash
doppler run --command command
```

### View your project list

```bash
doppler projects
```

### View your secrets for current project

```bash
doppler secrets
```

### Open Doppler dashboard in browser

```bash
doppler open
```
