# kubectl-get

> Get Kubernetes objects and resources. More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get>.

## Examples

### Get all namespaces in the current cluster

```bash
kubectl get [ns|namespaces]
```

### Get nodes in a specified namespace

```bash
kubectl get [no|nodes] [-n|--namespace] namespace
```

### Get pods in a specified namespace

```bash
kubectl get [po|pods] [-n|--namespace] namespace
```

### Get deployments in a specified namespace

```bash
kubectl get [deploy|deployments] [-n|--namespace] namespace
```

### Get services in a specified namespace

```bash
kubectl get [svc|services] [-n|--namespace] namespace
```

### Get other resources

```bash
kubectl get persistentvolumeclaims|secret|...
```

### Get all resources in all namespaces

```bash
kubectl get all [-A|--all-namespaces]
```

### Get Kubernetes objects defined in a YAML manifest file

```bash
kubectl get [-f|--filename] path/to/manifest.yaml
```
