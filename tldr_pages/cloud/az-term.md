# az-term

> Manage marketplace agreement with marketplaceordering. Part of `azure-cli` (also known as `az`). More information: <https://learn.microsoft.com/cli/azure/term>.

## Examples

### Print marketplace terms

```bash
az term show --product "product_identifier" --plan "plan_identifier" --publisher "publisher_identifier"
```

### Accept marketplace terms

```bash
az term accept --product "product_identifier" --plan "plan_identifier" --publisher "publisher_identifier"
```
