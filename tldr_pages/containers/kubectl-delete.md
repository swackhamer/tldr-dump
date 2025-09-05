# kubectl-delete

> Delete Kubernetes resources. More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete>.

## Examples

### Delete a specific pod

```bash
kubectl delete [po|pod] pod_name
```

### Delete a specific deployment

```bash
kubectl delete [deploy|deployment] deployment_name
```

### Delete a specific node

```bash
kubectl delete [no|node] node_name
```

### Delete all pods in a specified namespace

```bash
kubectl delete [po|pods] --all [-n|--namespace] namespace
```

### Delete all deployments and services in a specified namespace

```bash
kubectl delete [deploy|deployment],[svc|services] --all [-n|--namespace] namespace
```

### Delete all nodes

```bash
kubectl delete [no|nodes] --all
```

### Delete resources defined in a YAML manifest

```bash
kubectl delete [-f|--filename] path/to/manifest.yaml
```
