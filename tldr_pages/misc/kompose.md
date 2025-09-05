# kompose

> Convert docker-compose applications to Kubernetes. More information: <https://github.com/kubernetes/kompose>.

## Examples

### Deploy a dockerized application to Kubernetes

```bash
kompose up [-f|--file] docker-compose.yml
```

### Delete instantiated services/deployments from Kubernetes

```bash
kompose down [-f|--file] docker-compose.yml
```

### Convert a docker-compose file into Kubernetes resources file

```bash
kompose convert [-f|--file] docker-compose.yml
```
