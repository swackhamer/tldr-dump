# fluxctl

> Tool for Flux v1. More information: <https://fluxcd.io/legacy/flux/references/fluxctl>.

## Examples

### List workloads currently running in the cluster on specific namespace

```bash
fluxctl --k8s-fwd-ns=namespace list-workloads
```

### Show deployed and available images

```bash
fluxctl list-images
```

### Synchronize the cluster with the Git repository

```bash
fluxctl sync
```

### Turn on automatic deployment for a workload

```bash
fluxctl automate
```
