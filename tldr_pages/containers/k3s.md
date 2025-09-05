# k3s

> Install and manage lightweight Kubernetes clusters. More information: <https://docs.k3s.io/cli>.

## Examples

### Run the embedded `kubectl` command

```bash
k3s kubectl get nodes
```

### Take an etcd snapshot of the cluster

```bash
k3s etcd-snapshot save
```

### Rotate the CA certificate

```bash
k3s certificate rotate-ca
```

### Manage bootstrap tokens

```bash
k3s token list
```

### Uninstall K3s and remove all components

```bash
k3s-uninstall.sh
```
