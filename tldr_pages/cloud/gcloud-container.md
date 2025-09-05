# gcloud-container

> Manage containerized applications on Kubernetes and clusters. See also: `gcloud`. More information: <https://cloud.google.com/sdk/gcloud/reference/container>.

## Examples

### Register `gcloud` as a Docker credential helper

```bash
gcloud auth configure-docker
```

### Create a cluster to run GKE containers

```bash
gcloud container clusters create cluster_name
```

### List clusters for running GKE containers

```bash
gcloud container clusters list
```

### Update kubeconfig to get `kubectl` to use a GKE cluster

```bash
gcloud container clusters get-credentials cluster_name
```

### List tag and digest metadata for a container image

```bash
gcloud container images list-tags image
```

### Describe an existing cluster for running containers

```bash
gcloud container clusters describe cluster_name
```
