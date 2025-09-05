# dolt-config

> Read and write local (per repository) and global (per user) Dolt configuration variables. More information: <https://docs.dolthub.com/cli-reference/cli#dolt-config>.

## Examples

### List all local and global configuration options and their values

```bash
dolt config --list
```

### Display the value of a local or global configuration variable

```bash
dolt config --get name
```

### Modify the value of a local configuration variable, creating it if it doesn't exist

```bash
dolt config --add name value
```

### Modify the value of a global configuration variable, creating it if it doesn't exist

```bash
dolt config --global --add name value
```

### Delete a local configuration variable

```bash
dolt config --unset name
```

### Delete a global configuration variable

```bash
dolt config --global --unset name
```
