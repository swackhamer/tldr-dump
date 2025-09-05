# kubectl-api-resources

> Print the supported API resources on the server. More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#api-resources>.

## Examples

### Print the supported API resources

```bash
kubectl api-resources
```

### Print the supported API resources with more information

```bash
kubectl api-resources [-o|--output] wide
```

### Print the supported API resources sorted by a column

```bash
kubectl api-resources --sort-by name
```

### Print the supported namespaced resources

```bash
kubectl api-resources --namespaced
```

### Print the supported non-namespaced resources

```bash
kubectl api-resources --namespaced=false
```

### Print the supported API resources with a specific API group

```bash
kubectl api-resources --api-group=api_group
```
