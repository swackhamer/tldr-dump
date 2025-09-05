# kube-fzf

> Shell commands for command-line fuzzy searching of Kubernetes Pods. See also: `kubectl` for related commands. More information: <https://github.com/thecasualcoder/kube-fzf>.

## Examples

### Get pod details (from current namespace)

```bash
findpod
```

### Get pod details (from all namespaces)

```bash
findpod -a
```

### Describe a pod

```bash
describepod
```

### Tail pod logs

```bash
tailpod
```

### Exec into a pod's container

```bash
execpod shell_command
```

### Port-forward a pod

```bash
pfpod port_number
```
