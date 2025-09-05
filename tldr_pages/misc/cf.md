# cf

> Manage apps and services on Cloud Foundry. More information: <https://docs.cloudfoundry.org>.

## Examples

### Log in to the Cloud Foundry API

```bash
cf login -a api_url
```

### Push an app using the default settings

```bash
cf push app_name
```

### View the services available from your organization

```bash
cf marketplace
```

### Create a service instance

```bash
cf create-service service plan service_name
```

### Connect an application to a service

```bash
cf bind-service app_name service_name
```

### Run a script whose code is included in the app, but runs independently

```bash
cf run-task app_name "script_command" --name task_name
```

### Start an interactive SSH session with a VM hosting an app

```bash
cf ssh app_name
```

### View a dump of recent app logs

```bash
cf logs app_name --recent
```
