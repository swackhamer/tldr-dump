# kubectl-logs

> Show logs for containers in a pod. More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs>.

## Examples

### Show logs for a single-container pod

```bash
kubectl logs pod_name
```

### Show logs for a specified container in a pod

```bash
kubectl logs [-c|--container] container_name pod_name
```

### Show logs for all containers in a pod

```bash
kubectl logs --all-containers=true pod_name
```

### Stream pod logs

```bash
kubectl logs [-f|--follow] pod_name
```

### Show pod logs newer than a relative time like `10s`, `5m`, or `1h`

```bash
kubectl logs --since=relative_time pod_name
```

### Show the 10 most recent logs in a pod

```bash
kubectl logs --tail=10 pod_name
```

### Show all pod logs for a given deployment

```bash
kubectl logs deployment/deployment_name
```
