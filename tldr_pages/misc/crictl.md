# crictl

> Manage CRI-compatible container runtimes. More information: <https://github.com/kubernetes-sigs/cri-tools/blob/master/docs/crictl.md>.

## Examples

### List all kubernetes pods (Ready and NotReady)

```bash
crictl pods
```

### List all containers (Running and Exited)

```bash
crictl ps [-a|--all]
```

### List all images

```bash
crictl images
```

### Print information about specific containers

```bash
crictl inspect container_id1 container_id2 ...
```

### Open a specific shell inside a running container

```bash
crictl exec [-it|--interactive --tty] container_id sh
```

### Pull a specific image from a registry

```bash
crictl pull image:tag
```

### Print and follow logs of a specific container

```bash
crictl logs [-f|--follow] container_id
```

### Remove one or more images

```bash
crictl rmi image_id1 image_id2 ...
```
