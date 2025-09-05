# func

> Azure Functions Core Tools: develop and test Azure Functions locally. Local functions can connect to live Azure services, and can deploy a function app to an Azure subscription. More information: <https://learn.microsoft.com/azure/azure-functions/functions-run-local>.

## Examples

### Create a new functions project

```bash
func init project
```

### Create a new function

```bash
func new
```

### Run functions locally

```bash
func start
```

### Publish your code to a function app in Azure

```bash
func azure functionapp publish function
```

### Download all settings from an existing function app

```bash
func azure functionapp fetch-app-settings function
```

### Get the connection string for a specific storage account

```bash
func azure storage fetch-connection-string storage_account
```
