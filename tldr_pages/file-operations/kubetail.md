# kubetail

> Utility to tail multiple Kubernetes pod logs at the same time. More information: <https://github.com/johanhaleby/kubetail>.

## Examples

### Tail the logs of multiple pods (whose name starts with "my_app") in one go

```bash
kubetail my_app
```

### Tail only a specific container from multiple pods

```bash
kubetail my_app [-c|--container] my_container
```

### To tail multiple containers from multiple pods

```bash
kubetail my_app [-c|--container] my_container_1 [-c|--container] my_container_2
```

### To tail multiple applications at the same time separate them by comma

```bash
kubetail my_app_1,my_app_2
```
