# exo-iam

> Manage the Exoscale IAM service. More information: <https://community.exoscale.com/product/iam/>.

## Examples

### List all of the IAM roles

```bash
exo iam role list
```

### Create a new API key

```bash
exo iam api-key create api_key_name iam_role_name
```

### Create a new IAM role

```bash
cat path/to/policy.json | exo iam role create iam_role_name --editable --policy -
```

### Show the policy of an existing IAM role

```bash
exo iam role show iam_role_name --policy [-O|--output-format] json | jq .
```

### Update the default Organization policy (the default Organization policy will be applied to all of the API keys within the Organization)

```bash
cat path/to/policy.json | exo iam org-policy update -
```
