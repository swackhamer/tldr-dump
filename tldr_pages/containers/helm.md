# helm

> A package manager for Kubernetes. Some subcommands such as `install` have their own usage documentation. More information: <https://helm.sh/docs/helm/>.

## Examples

### Create a helm chart

```bash
helm create chart_name
```

### Add a new helm repository

```bash
helm repo add repository_name
```

### List helm repositories

```bash
helm repo [ls|list]
```

### Update helm repositories

```bash
helm repo [up|update]
```

### Delete a helm repository

```bash
helm repo [rm|remove] repository_name
```

### Install a helm chart

```bash
helm install name repository_name/chart_name
```

### Download helm chart as a tar archive

```bash
helm get chart_release_name
```

### Update helm dependencies

```bash
helm [dep|dependency] [up|update]
```
