# podman-machine

> Create and manage virtual machines running Podman. Included with Podman version 4 or greater. More information: <https://docs.podman.io/en/latest/markdown/podman-machine.1.html>.

## Examples

### List existing machines

```bash
podman machine ls
```

### Create a new default machine

```bash
podman machine init
```

### Create a new machine with a specific name

```bash
podman machine init name
```

### Create a new machine with different resources

```bash
podman machine init --cpus=4 --memory=4096 --disk-size=50
```

### Start or stop a machine

```bash
podman machine start|stop name
```

### Connect to a running machine via SSH

```bash
podman machine ssh name
```

### Inspect information about a machine

```bash
podman machine inspect name
```
