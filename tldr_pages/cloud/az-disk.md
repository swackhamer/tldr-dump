# az-disk

> Manage Azure Managed Disks. Part of `azure-cli` (also known as `az`). More information: <https://learn.microsoft.com/cli/azure/disk>.

## Examples

### Create a managed disk

```bash
az disk create [-g|--resource-group] resource_group [-n|--name] disk_name [-z|--size-gb]size_in_gb
```

### List managed disks in a resource group

```bash
az disk list [-g|--resource-group] resource_group
```

### Delete a managed disk

```bash
az disk delete [-g|--resource-group] resource_group [-n|--name] disk_name
```

### Grant read or write access to a managed disk (for export)

```bash
az disk grant-access [-g|--resource-group] resource_group [-n|--name] disk_name [--access|--access-level] Read|Write --duration-in-seconds seconds
```

### Update disk size

```bash
az disk update [-g|--resource-group] resource_group [-n|--name] disk_name [-z|--size-gb] new_size_in_gb
```
