# devpod

> Launch reproducible development environments using Docker, Kubernetes, or SSH. More information: <https://devpod.sh/docs/quickstart/devpod-cli/>.

## Examples

### Add a provider such as Docker or Kubernetes

```bash
devpod provider add provider_name
```

### List all available providers

```bash
devpod provider list-available
```

### Start a workspace from a GitHub repository with a specific IDE

```bash
devpod up github.com/user/repo [-i|--ide] vscode
```

### Start a workspace from a local directory

```bash
devpod up path/to/project
```

### Recreate an existing workspace

```bash
devpod up workspace_name [-r|--recreate]
```

### Reset a workspace to a clean state

```bash
devpod up workspace_name [-x|--reset]
```

### Add a custom provider from a GitHub repository

```bash
devpod provider add org/provider-repo
```
