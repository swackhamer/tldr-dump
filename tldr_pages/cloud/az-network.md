# az-network

> Manage Azure Network resources. Part of `azure-cli` (also known as `az`). More information: <https://learn.microsoft.com/cli/azure/network>.

## Examples

### List network resources in a region that are used against a subscription quota

```bash
az network list-usages
```

### List all virtual networks in a subscription

```bash
az network vnet list
```

### Create a virtual network

```bash
az network vnet create --address-prefixes 10.0.0.0/16 [-n|--name] vnet [-g|--resource-group] group_name --submet-name subnet --subnet-prefixes 10.0.0.0/24
```

### Enable accelerated networking for a network interface card

```bash
az network nic update --accelerated-networking true [-n|--name] nic [-g|--resource-group] resource_group
```
