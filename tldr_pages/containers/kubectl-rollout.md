# kubectl-rollout

> Manage the rollout of a Kubernetes resource (deployments, daemonsets, and statefulsets). More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#rollout>.

## Examples

### Start a rolling restart of a resource

```bash
kubectl rollout restart resource_type/resource_name
```

### Watch the rolling update status of a resource

```bash
kubectl rollout status resource_type/resource_name
```

### Roll back a resource to the previous revision

```bash
kubectl rollout undo resource_type/resource_name
```

### View the rollout history of a resource

```bash
kubectl rollout history resource_type/resource_name
```
