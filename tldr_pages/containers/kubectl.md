# kubectl

> Run commands against Kubernetes clusters. Some subcommands such as `run` have their own usage documentation. More information: <https://kubernetes.io/docs/reference/kubectl/>.

## Examples

### List information about a resource with more details

```bash
kubectl get pod|service|deployment|ingress|... [-o|--output] wide
```

### Update specified pod with the label 'unhealthy' and the value 'true'

```bash
kubectl label pods name unhealthy=true
```

### List all resources with different types

```bash
kubectl get all
```

### Display resource (CPU/Memory/Storage) usage of nodes or pods

```bash
kubectl top pod|node
```

### Print the address of the master and cluster services

```bash
kubectl cluster-info
```

### Display an explanation of a specific field

```bash
kubectl explain pods.spec.containers
```

### Print the logs for a container in a pod or specified resource

```bash
kubectl logs pod_name
```

### Run command in an existing pod

```bash
kubectl exec pod_name -- ls /
```
