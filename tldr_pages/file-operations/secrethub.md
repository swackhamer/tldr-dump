# secrethub

> Keep secrets out of configuration files. More information: <https://github.com/secrethub/secrethub-cli>.

## Examples

### Print a secret to `stdout`

```bash
secrethub read path/to/secret
```

### Generate a random value and store it as a new or updated secret

```bash
secrethub generate path/to/secret
```

### Store a value from the clipboard as a new or updated secret

```bash
secrethub write --clip path/to/secret
```

### Store a value supplied on `stdin` as a new or updated secret

```bash
echo "secret_value" | secrethub write path/to/secret
```

### Audit a repository or secret

```bash
secrethub audit path/to/repo_or_secret
```
