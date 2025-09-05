# az-account

> Manage Azure subscription information. Part of `azure-cli` (also known as `az`). More information: <https://learn.microsoft.com/cli/azure/account>.

## Examples

### List all subscriptions for the logged in account

```bash
az account list
```

### Set a `subscription` to be the currently active subscription

```bash
az account set [-s|--subscription] subscription_id
```

### List supported regions for the currently active subscription

```bash
az account list-locations
```

### Print an access token to be used with `MS Graph API`

```bash
az account get-access-token --resource-type ms-graph
```

### Print details of the currently active subscription in a specific format

```bash
az account show [-o|--output] json|tsv|table|yaml
```
