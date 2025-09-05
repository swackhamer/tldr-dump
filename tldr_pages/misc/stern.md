# stern

> Tail multiple pods and containers from Kubernetes. More information: <https://github.com/stern/stern>.

## Examples

### Tail all pods within a current namespace

```bash
stern .
```

### Tail all pods with a specific status

```bash
stern . --container-state running|waiting|terminated
```

### Tail all pods that matches a given `regex`

```bash
stern pod_query
```

### Tail matched pods from all namespaces

```bash
stern pod_query --all-namespaces
```

### Tail matched pods from 15 minutes ago

```bash
stern pod_query --since 15m
```

### Tail matched pods with a specific label

```bash
stern pod_query --selector release=canary
```
