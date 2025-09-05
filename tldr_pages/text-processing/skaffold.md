# skaffold

> Facilitate continuous development for Kubernetes applications. More information: <https://skaffold.dev>.

## Examples

### Build the artifacts

```bash
skaffold build [-f|--filename] skaffold.yaml
```

### Build and deploy your app every time your code changes

```bash
skaffold dev [-f|--filename] skaffold.yaml
```

### Run a pipeline file

```bash
skaffold run [-f|--filename] skaffold.yaml
```

### Run a diagnostic on Skaffold

```bash
skaffold diagnose [-f|--filename] skaffold.yaml
```

### Deploy the artifacts

```bash
skaffold deploy [-f|--filename] skaffold.yaml
```
