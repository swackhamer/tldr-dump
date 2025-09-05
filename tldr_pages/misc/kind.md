# kind

> Run local Kubernetes clusters using Docker container "nodes". Designed for testing Kubernetes itself, but may be used for local development or continuous integration. More information: <https://github.com/kubernetes-sigs/kind>.

## Examples

### Create a local Kubernetes cluster

```bash
kind create cluster --name cluster_name
```

### Delete one or more clusters

```bash
kind delete clusters cluster_name
```

### Get details about clusters, nodes, or the kubeconfig

```bash
kind get clusters|nodes|kubeconfig
```

### Export the kubeconfig or the logs

```bash
kind export kubeconfig|logs
```
