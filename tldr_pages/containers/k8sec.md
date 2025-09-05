# k8sec

> Manage Kubernetes secrets. More information: <https://github.com/dtan4/k8sec>.

## Examples

### List all secrets

```bash
k8sec list
```

### List a specific secret as a base64-encoded string

```bash
k8sec list secret_name --base64
```

### Set a secret's value

```bash
k8sec set secret_name key=value
```

### Set a base64-encoded value

```bash
k8sec set --base64 secret_name key=encoded_value
```

### Unset a secret

```bash
k8sec unset secret_name
```

### Load secrets from a file

```bash
k8sec load [-f|--filename] path/to/file secret_name
```

### Dump secrets to a file

```bash
k8sec dump [-f|--filename] path/to/file secret_name
```
