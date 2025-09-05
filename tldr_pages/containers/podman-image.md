# podman-image

> Manage Docker images. See also: `podman build`, `podman import`, `podman pull`. More information: <https://docs.podman.io/en/latest/markdown/podman-image.1.html>.

## Examples

### List local Docker images

```bash
podman image ls
```

### Delete unused local Docker images

```bash
podman image prune
```

### Delete all unused images (not just those without a tag)

```bash
podman image prune --all
```

### Show the history of a local Docker image

```bash
podman image history image
```
