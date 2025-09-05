# k3d

> A wrapper to easily create k3s clusters inside Docker. More information: <https://k3d.io>.

## Examples

### Create a cluster

```bash
k3d cluster create cluster_name
```

### Delete a cluster

```bash
k3d cluster delete cluster_name
```

### Create a new containerized k3s node

```bash
k3d node create node_name
```

### Import an image from Docker into a k3d cluster

```bash
k3d image import image_name --cluster cluster_name
```

### Create a new registry

```bash
k3d registry create registry_name
```
