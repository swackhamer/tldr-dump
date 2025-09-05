# az-provider

> Manage resource providers. Part of `azure-cli` (also known as `az`). More information: <https://learn.microsoft.com/cli/azure/provider>.

## Examples

### Register a provider

```bash
az provider register [-n|--namespace] Microsoft.PolicyInsights
```

### Unregister a provider

```bash
az provider unregister [-n|--namespace] Microsoft.Automation
```

### List all providers for a subscription

```bash
az provider list
```

### Show information about a specific provider

```bash
az provider show [-n|--namespace] Microsoft.Storage
```

### List all resource types for a specific provider

```bash
az provider list --query "[?namespace=='Microsoft.Network'].resourceTypes[].resourceType"
```
