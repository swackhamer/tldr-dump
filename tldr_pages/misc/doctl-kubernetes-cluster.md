# doctl-kubernetes-cluster

> Manage Kubernetes clusters and view configuration options relating to clusters. More information: <https://docs.digitalocean.com/reference/doctl/reference/kubernetes/cluster/>.

## Examples

### Create a Kubernetes cluster

```bash
doctl [k|kubernetes] [c|cluster] [c|create] --count 3 --region nyc1 --size s-1vcpu-2gb --version latest cluster_name
```

### List all Kubernetes clusters

```bash
doctl [k|kubernetes] [c|cluster] [ls|list]
```

### Fetch and save the kubeconfig

```bash
doctl [k|kubernetes] [c|cluster] [cfg|kubeconfig] [s|save] cluster_name
```

### Check for available upgrades

```bash
doctl [k|kubernetes] [c|cluster] [gu|get-upgrades] cluster_name
```

### Upgrade a cluster to a new Kubernetes version

```bash
doctl [k|kubernetes] [c|cluster] upgrade cluster_name
```

### Delete a cluster

```bash
doctl [k|kubernetes] [c|cluster] [d|delete] cluster_name
```
