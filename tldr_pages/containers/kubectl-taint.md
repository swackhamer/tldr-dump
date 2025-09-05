# kubectl-taint

> Update the taints on nodes. More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#taint>.

## Examples

### Apply taint to a node

```bash
kubectl taint [no|nodes] node_name label_key=label_value:effect
```

### Remove taint from a node

```bash
kubectl taint [no|nodes] node_name label_key:effect-
```

### Remove all taints from a node

```bash
kubectl taint [no|nodes] node_name label_key-
```
