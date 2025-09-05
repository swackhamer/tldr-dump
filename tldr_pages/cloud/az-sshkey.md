# az-sshkey

> Manage SSH public keys with virtual machines. Part of `azure-cli` (also known as `az`). More information: <https://learn.microsoft.com/cli/azure/sshkey>.

## Examples

### Create a new SSH key

```bash
az sshkey create --name name [-g|--resource-group] resource_group
```

### Upload an existing SSH key

```bash
az sshkey create --name name [-g|--resource-group] resource_group --public-key "@path/to/key.pub"
```

### List all SSH public keys

```bash
az sshkey list
```

### Show information about an SSH public key

```bash
az sshkey show --name name [-g|--resource-group] resource_group
```
