# oc

> The OpenShift Container Platform CLI. Allows for application and container management. More information: <https://docs.openshift.com/container-platform/latest/cli_reference/get_started_cli.html>.

## Examples

### Log in to the OpenShift Container Platform server

```bash
oc login
```

### Create a new project

```bash
oc new-project project_name
```

### Switch to an existing project

```bash
oc project project_name
```

### Add a new application to a project

```bash
oc new-app repo_url --name application
```

### Open a remote shell session to a container

```bash
oc rsh pod_name
```

### List pods in a project

```bash
oc get pods
```

### Log out from the current session

```bash
oc logout
```
