# loft

> Install and manage multi-tenant Kubernetes environments using virtual clusters. More information: <https://loft.sh/docs/cli/loft/>.

## Examples

### Install or upgrade Loft in the current Kubernetes cluster

```bash
loft start
```

### Authenticate to a remote Loft instance

```bash
loft login https://loft.example.com
```

### Create a virtual cluster with a specific space and cluster

```bash
loft create vcluster vcluster_name [-s|--space] space_name [-c|--cluster] cluster_name
```

### List all virtual clusters

```bash
loft list vclusters
```

### Switch context to a specific virtual cluster

```bash
loft use vcluster vcluster_name
```

### Delete a virtual cluster

```bash
loft delete vcluster vcluster_name
```

### Show the current Loft username

```bash
loft vars username
```

### Uninstall Loft from the cluster

```bash
loft uninstall
```
