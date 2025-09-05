# incus

> Modern, secure and powerful system container and virtual machine manager. More information: <https://linuxcontainers.org/incus/docs/main>.

## Examples

### List all containers and virtual machines (both running and stopped)

```bash
incus list
```

### Create a container from an image, with a custom name

```bash
incus create image container_name
```

### Start or stop an existing container

```bash
incus start|stop container_name
```

### Open a shell inside an already running container

```bash
incus shell container_name
```

### Remove a stopped container

```bash
incus delete container_name
```

### Pull an image from an image repository (remote) to local

```bash
incus copy remote:image local:custom_image_name
```
