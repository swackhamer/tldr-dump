# az-login

> Log in to Azure. Part of `azure-cli` (also known as `az`). More information: <https://learn.microsoft.com/cli/azure/reference-index#az-login>.

## Examples

### Log in interactively

```bash
az login
```

### Log in with a service principal using a client secret

```bash
az login --service-principal [-u|--username] http://azure-cli-service-principal [-p|--password] secret --tenant someone.onmicrosoft.com
```

### Log in with a service principal using a client certificate

```bash
az login --service-principal [-u|--username] http://azure-cli-service-principal [-p|--password] path/to/cert.pem [-t|--tenant] someone.onmicrosoft.com
```

### Log in using a VM's system assigned identity

```bash
az login [-i|--identity]
```

### Log in using a VM's user assigned identity

```bash
az login [-i|--identity] [-u|--username] /subscriptions/subscription_id/resourcegroups/my_rg/providers/Microsoft.ManagedIdentity/userAssignedIdentities/my_id
```
