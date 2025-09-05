# az-logicapp

> Manage Logic Apps in Azure Cloud Services. Part of `azure-cli` (also known as `az`). More information: <https://learn.microsoft.com/cli/azure/logicapp>.

## Examples

### Create a logic app

```bash
az logicapp create [-n|--name] name [-g|--resource-group] resource_group [-s|--storage-account] storage_account
```

### Delete a logic app

```bash
az logicapp delete [-n|--name] name [-g|--resource-group] resource_group
```

### List logic apps

```bash
az logicapp list [-g|--resource-group] resource_group
```

### Restart a logic app

```bash
az logicapp restart [-n|--name] name [-g|--resource-group] resource_group
```

### Start a logic app

```bash
az logicapp start [-n|--name] name [-g|--resource-group] resource_group
```

### Stop a logic app

```bash
az logicapp stop [-n|--name] name [-g|--resource-group] resource_group
```
