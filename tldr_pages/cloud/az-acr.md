# az-acr

> Manage private registries with Azure Container Registries. Part of `azure-cli` (also known as `az`). More information: <https://learn.microsoft.com/cli/azure/acr>.

## Examples

### Create a managed container registry

```bash
az acr create [-n|--name] registry_name [-g|--resource-group] resource_group --sku sku
```

### Login to a registry

```bash
az acr login [-n|--name] registry_name
```

### Tag a local image for ACR

```bash
docker tag image_name registry_name.azurecr.io/image_name:tag
```

### Push an image to a registry

```bash
docker push registry_name.azurecr.io/image_name:tag
```

### Pull an image from a registry

```bash
docker pull registry_name.azurecr.io/image_name:tag
```

### Delete an image from a registry

```bash
az acr repository delete [-n|--name] registry_name --repository image_name:tag
```

### Delete a managed container registry

```bash
az acr delete [-n|--name] registry_name [-g|--resource-group] resource_group [-y|--yes]
```

### List images within a registry

```bash
az acr repository list [-n|--name] registry_name --output table
```
