# az-aks

> Manage Azure Kubernetes Service (AKS) clusters. Part of `azure-cli` (also known as `az`). More information: <https://learn.microsoft.com/cli/azure/aks>.

## Examples

### List AKS clusters

```bash
az aks list [-g|--resource-group] resource_group
```

### Create a new AKS cluster

```bash
az aks create [-g|--resource-group] resource_group [-n|--name] name [-c|--node-count] count --node-vm-size size
```

### Delete an AKS cluster

```bash
az aks delete [-g|--resource-group] resource_group [-n|--name] name
```

### Get the access credentials for an AKS cluster

```bash
az aks get-credentials [-g|--resource-group] resource_group [-n|--name] name
```

### Get the upgrade versions available for an AKS cluster

```bash
az aks get-upgrades [-g|--resource-group] resource_group [-n|--name] name
```
