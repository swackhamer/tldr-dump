# devenv

> Fast, Declarative, Reproducible and Composable Developer Environments using Nix. More information: <https://devenv.sh/getting-started/#commands>.

## Examples

### Initialize the environment

```bash
devenv init
```

### Enter the Development Environment with relaxed hermeticity (state of being airtight)

```bash
devenv shell --impure
```

### Get detailed information about the current environment

```bash
devenv info --verbose
```

### Start processes with `devenv`

```bash
devenv up --config path/to/file
```

### Clean the environment variables and re-enter the shell in offline mode

```bash
devenv --clean --offline
```

### Delete the previous shell generations

```bash
devenv gc
```
