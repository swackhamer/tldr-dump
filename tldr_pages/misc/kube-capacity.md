# kube-capacity

> Provide an overview of resource requests, limits, and utilization in a Kubernetes cluster. Combine the best parts of `kubectl top` and `kubectl describe` into a CLI focused on cluster resources. More information: <https://github.com/robscott/kube-capacity>.

## Examples

### List nodes including the total CPU and Memory resource requests and limits

```bash
kube-capacity
```

### Include pods

```bash
kube-capacity [-p|--pods]
```

### Include utilization

```bash
kube-capacity [-u|--util]
```
