# kubectl-describe

> Show details of Kubernetes objects and resources. More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe>.

## Examples

### Show details of pods in a namespace

```bash
kubectl describe [po|pods] [-n|--namespace] namespace
```

### Show details of nodes in a namespace

```bash
kubectl describe [no|nodes] [-n|--namespace] namespace
```

### Show the details of a specific pod in a namespace

```bash
kubectl describe [po|pods] pod_name [-n|--namespace] namespace
```

### Show the details of a specific node in a namespace

```bash
kubectl describe [no|nodes] node_name [-n|--namespace] namespace
```

### Show details of Kubernetes objects defined in a YAML manifest file

```bash
kubectl describe [-f|--filename] path/to/manifest.yaml
```
