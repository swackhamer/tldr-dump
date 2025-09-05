# az-apim

> Manage Azure API Management services. Part of `azure-cli` (also known as `az`). More information: <https://learn.microsoft.com/cli/azure/apim>.

## Examples

### List API Management services within a resource group

```bash
az apim list [-g|--resource-group] resource_group
```

### Create an API Management service instance

```bash
az apim create [-n|--name] name [-g|--resource-group] resource_group --publisher-email email --publisher-name name
```

### Delete an API Management service

```bash
az apim delete [-n|--name] name [-g|--resource-group] resource_group
```

### Show details of an API Management service instance

```bash
az apim show [-n|--name] name [-g|--resource-group] resource_group
```

### Update an API Management service instance

```bash
az apim update [-n|--name] name [-g|--resource-group] resource_group
```
