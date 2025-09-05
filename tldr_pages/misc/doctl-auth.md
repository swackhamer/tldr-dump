# doctl-auth

> Authenticate `doctl` with API tokens. More information: <https://docs.digitalocean.com/reference/doctl/reference/auth/>.

## Examples

### Open a prompt to enter an API token and label its context

```bash
doctl auth init --context token_label
```

### List authentication contexts (API tokens)

```bash
doctl auth [ls|list]
```

### Switch contexts (API tokens)

```bash
doctl auth switch --context token_label
```

### Remove a stored authentication context (API token)

```bash
doctl auth remove --context token_label
```

### Show available commands

```bash
doctl auth [-h|--help]
```
