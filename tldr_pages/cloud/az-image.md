# az-image

> Manage custom Virtual Machine Images in Azure. Part of `azure-cli` (also known as `az`). More information: <https://learn.microsoft.com/cli/azure/image>.

## Examples

### List the custom images under a resource group

```bash
az image list [-g|--resource-group] resource_group
```

### Create a custom image from managed disks or snapshots

```bash
az image create [-g|--resource-group] resource_group [-n|--name] name --os-type windows|linux --source os_disk_source
```

### Delete a custom image

```bash
az image delete [-n|--name] name [-g|--resource-group] resource_group
```

### Show details of a custom image

```bash
az image show [-n|--name] name [-g|--resource-group] resource_group
```

### Update custom images

```bash
az image update [-n|--name] name [-g|--resource-group] resource_group --set property=value
```
