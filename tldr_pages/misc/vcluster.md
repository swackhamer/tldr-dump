# vcluster

> Create and manage lightweight virtual Kubernetes clusters in namespaces. More information: <https://www.vcluster.com/docs/vcluster>.

## Examples

### Create a virtual cluster in a specific namespace

```bash
vcluster create vcluster_name [-n|--namespace] namespace
```

### Connect to a virtual cluster with a local port and insecure mode

```bash
vcluster connect vcluster_name [-n|--namespace] namespace --local-port port --insecure
```

### List all virtual clusters

```bash
vcluster list
```

### Delete a virtual cluster

```bash
vcluster delete vcluster_name
```

### List platform-managed virtual clusters

```bash
vcluster platform list
```

### Create a platform-managed virtual cluster

```bash
vcluster platform create vcluster_name [-n|--namespace] namespace
```

### Connect to a platform-managed virtual cluster

```bash
vcluster platform connect vcluster_name [-n|--namespace] namespace
```

### Delete a platform-managed virtual cluster

```bash
vcluster platform delete vcluster_name [-n|--namespace] namespace
```
