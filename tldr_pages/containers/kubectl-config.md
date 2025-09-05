# kubectl-config

> Manage Kubernetes configuration (kubeconfig) files for accessing clusters via `kubectl` or the Kubernetes API. By default, the Kubernetes will get its configuration from `${HOME}/.kube/config`. See also: `kubectx`, `kubens`. More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#config>.

## Examples

### Get all contexts in the default kubeconfig file

```bash
kubectl config get-contexts
```

### Get all clusters/contexts/users in a custom kubeconfig file

```bash
kubectl config get-clusters|get-contexts|get-users --kubeconfig path/to/kubeconfig.yaml
```

### Get the current context

```bash
kubectl config current-context
```

### Set the default namespace of the current context

```bash
kubectl config set-context --current --namespace namespace
```

### Switch to another context

```bash
kubectl config use|use-context context_name
```

### Delete clusters/contexts/users

```bash
kubectl config delete-cluster|delete-context|delete-user cluster|context|user
```

### Permanently add custom kubeconfig files

```bash
export KUBECONFIG="$HOME.kube/config:path/to/custom/kubeconfig.yaml" kubectl config get-contexts
```
