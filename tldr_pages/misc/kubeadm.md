# kubeadm

> Interface for creating and managing Kubernetes clusters. More information: <https://kubernetes.io/docs/reference/setup-tools/kubeadm>.

## Examples

### Create a Kubernetes control plane

```bash
kubeadm init
```

### Bootstrap a Kubernetes worker node and join it to a cluster

```bash
kubeadm join --token token
```

### Create a new bootstrap token with a TTL of 12 hours

```bash
kubeadm token create --ttl 12h0m0s
```

### Check if the Kubernetes cluster is upgradeable and which versions are available

```bash
kubeadm upgrade plan
```

### Upgrade Kubernetes cluster to a specified version

```bash
kubeadm upgrade apply version
```

### View the kubeadm ConfigMap containing the cluster's configuration

```bash
kubeadm config view
```

### Revert changes made to the host by 'kubeadm init' or 'kubeadm join'

```bash
kubeadm reset
```
