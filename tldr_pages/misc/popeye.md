# popeye

> Report potential issues with Kubernetes deployment manifests. More information: <https://github.com/derailed/popeye>.

## Examples

### Scan the current Kubernetes cluster

```bash
popeye
```

### Scan a specific namespace

```bash
popeye [-n|--namespace] namespace
```

### Scan specific Kubernetes context

```bash
popeye --context context
```

### Use a spinach configuration file for scanning

```bash
popeye [-f|--file] spinach.yaml
```
