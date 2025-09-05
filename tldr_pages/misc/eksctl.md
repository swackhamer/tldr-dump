# eksctl

> The official CLI for Amazon EKS. More information: <https://eksctl.io>.

## Examples

### Create a basic cluster

```bash
eksctl create cluster
```

### List the details about a cluster or all of the clusters

```bash
eksctl get cluster --name=name --region=region
```

### Create a cluster passing all configuration information in a file

```bash
eksctl create cluster --config-file=path/to/file
```

### Create a cluster using a configuration file and skip creating nodegroups until later

```bash
eksctl create cluster --config-file=<path> --without-nodegroup
```

### Delete a cluster

```bash
eksctl delete cluster --name=name --region=region
```

### Create cluster and write cluster credentials to a file other than the default

```bash
eksctl create cluster --name=name --nodes=4 --kubeconfig=path/to/config.yaml
```

### Create a cluster and prevent storing cluster credentials locally

```bash
eksctl create cluster --name=name --nodes=4 --write-kubeconfig=false
```

### Create a cluster and let `eksctl` manage cluster credentials under the `~/.kube/eksctl/clusters` directory

```bash
eksctl create cluster --name=name --nodes=4 --auto-kubeconfig
```
