# kubectl-apply

> Manage applications through files defining Kubernetes resources. Create and update resources in a cluster. More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply>.

## Examples

### Apply a configuration to a resource by file name

```bash
kubectl apply [-f|--filename] path/to/filename
```

### Apply a configuration to a resource from `kustomization.yaml` in a directory

```bash
kubectl apply [-k|--kustomize] path/to/directory
```

### Apply a configuration to a resource by `stdin`

```bash
cat pod.json | kubectl apply [-f|--filename] -
```

### Edit the latest last-applied-configuration annotations of resources from the default editor

```bash
kubectl apply edit-last-applied [-f|--filename] path/to/filename
```

### Set the latest last-applied-configuration annotations by setting it to match the contents of a file

```bash
kubectl apply set-last-applied [-f|--filename] path/to/filename
```

### View the latest last-applied-configuration annotations by type/name or file

```bash
kubectl apply view-last-applied [-f|--filename] path/to/filename
```
