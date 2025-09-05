# podman-rmi

> Remove Podman images. More information: <https://docs.podman.io/en/latest/markdown/podman-rmi.1.html>.

## Examples

### Remove one or more images given their names

```bash
podman rmi image:tag image2:tag ...
```

### Force remove an image

```bash
podman rmi --force image
```

### Remove an image without deleting untagged parents

```bash
podman rmi --no-prune image
```

### Display help

```bash
podman rmi
```
