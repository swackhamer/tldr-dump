# az-tag

> Manage tags on a resource. Part of `azure-cli` (also known as `az`). More information: <https://learn.microsoft.com/cli/azure/tag>.

## Examples

### Create a tag value

```bash
az tag add-value [-n|--name] tag_name --value tag_value
```

### Create a tag in the subscription

```bash
az tag create [-n|--name] tag_name
```

### Delete a tag from the subscription

```bash
az tag delete [-n|--name] tag_name
```

### List all tags on a subscription

```bash
az tag list --resource-id /subscriptions/subscription_id
```

### Delete a tag value for a specific tag name

```bash
az tag remove-value [-n|--name] tag_name --value tag_value
```
