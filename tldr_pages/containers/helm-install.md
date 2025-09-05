# helm-install

> Install a helm chart. More information: <https://helm.sh/docs/intro/using_helm/#helm-install-installing-a-package>.

## Examples

### Install a helm chart

```bash
helm install name repository_name/chart_name
```

### Install a helm chart from an unpacked chart directory

```bash
helm install name path/to/source_directory
```

### Install a helm chart from a URL

```bash
helm install package_name https://example.com/charts/packagename-1.2.3.tgz
```

### Install a helm chart and generate a name

```bash
helm install repository_name/chart_name [-g|--generate-name]
```

### Perform a dry run

```bash
helm install name repository_name/chart_name --dry-run
```

### Install a helm chart with custom values

```bash
helm install name repository_name/chart_name --set parameter1=value1,parameter2=value2
```

### Install a helm chart passing a custom values file

```bash
helm install name repository_name/chart_name [-f|--values] path/to/values.yaml
```
