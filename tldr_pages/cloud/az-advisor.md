# az-advisor

> Manage Azure subscription information. Part of `azure-cli` (also known as `az`). More information: <https://learn.microsoft.com/cli/azure/advisor>.

## Examples

### List Azure Advisor configuration for the entire subscription

```bash
az advisor configuration list
```

### Show Azure Advisor configuration for the given subscription or resource group

```bash
az advisor configuration show [-g|--resource-group] resource_group
```

### List Azure Advisor recommendations

```bash
az advisor recommendation list
```

### Enable Azure Advisor recommendations

```bash
az advisor recommendation enable [-g|--resource-group] resource_group
```

### Disable Azure Advisor recommendations

```bash
az advisor recommendation disable [-g|--resource-group] resource_group
```
