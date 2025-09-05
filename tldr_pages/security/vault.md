# vault

> Interact with HashiCorp Vault. More information: <https://www.vaultproject.io/docs/commands>.

## Examples

### Connect to a Vault server and initialize a new encrypted data store

```bash
vault init
```

### Unseal (unlock) the vault, by providing one of the key shares needed to access the encrypted data store

```bash
vault unseal key-share-x
```

### Authenticate the CLI client against the Vault server, using an authentication token

```bash
vault auth authentication_token
```

### Store a new secret in the vault, using the generic back-end called "secret"

```bash
vault write secret/hello value=world
```

### Read a value from the vault, using the generic back-end called "secret"

```bash
vault read secret/hello
```

### Read a specific field from the value

```bash
vault read -field=field_name secret/hello
```

### Seal (lock) the Vault server, by removing the encryption key of the data store from memory

```bash
vault seal
```
