# op

> Official CLI for 1Password's desktop app. More information: <https://developer.1password.com/docs/cli/reference>.

## Examples

### Sign in to a 1Password account

```bash
op signin
```

### List all vaults

```bash
op vault list
```

### Print item details in JSON format

```bash
op item get item_name --format json
```

### Create a new item with a category in the default vault

```bash
op item create --category category_name
```

### Print a referenced secret to `stdout`

```bash
op read secret_reference
```

### Pass secret references from exported environment variables to a command

```bash
op run -- command
```

### Pass secret references from an environment file to a command

```bash
op run --env-file path/to/env_file.env -- command
```

### Read secret references from a file and save plaintext secrets to a file

```bash
op inject --in-file path/to/input_file --out-file path/to/output_file
```
