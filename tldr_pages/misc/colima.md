# colima

> Container runtimes for macOS and Linux with minimal setup. More information: <https://github.com/abiosoft/colima>.

## Examples

### Start the daemon in the background

```bash
colima start
```

### Create a configuration file and use it

```bash
colima start --edit
```

### Start and setup containerd (install `nerdctl` to use containerd via `nerdctl`)

```bash
colima start --runtime containerd
```

### Start with Kubernetes (`kubectl` is required)

```bash
colima start --kubernetes
```

### Customize CPU count, RAM memory and disk space (in GiB)

```bash
colima start --cpu number --memory memory --disk storage_space
```

### Use Docker via Colima (Docker is required)

```bash
colima start
```

### List containers with their information and status

```bash
colima list
```

### Show runtime status

```bash
colima status
```
