# az-config

> Manage Azure CLI configuration. Part of `azure-cli` (also known as `az`). More information: <https://learn.microsoft.com/cli/azure/config>.

## Examples

### Print all configurations

```bash
az config get
```

### Print configurations for a specific section

```bash
az config get section_name
```

### Set a configuration

```bash
az config set configuration_name=value
```

### Unset a configuration

```bash
az config unset configuration_name
```
