# kubectl-label

> Label Kubernetes resources. More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#label>.

## Examples

### Label a pod

```bash
kubectl label [po|pod] pod_name key=value
```

### Update a pod label by overwriting the existing value

```bash
kubectl label --overwrite pod pod_name key=value
```

### Label all pods in the namespace

```bash
kubectl label [po|pods] --all key=value
```

### Label a pod identified by the pod definition file

```bash
kubectl label [-f|--filename] pod_definition_file key=value
```

### Remove the label from a pod

```bash
kubectl label [po|pod] pod_name key-
```
