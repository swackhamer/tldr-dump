# kubectl-edit

> Edit Kubernetes resources. More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#edit>.

## Examples

### Edit a pod in the default namespace

```bash
kubectl edit [po|pod]/pod_name
```

### Edit a deployment in the default namespace

```bash
kubectl edit [deploy|deployment]/deployment_name
```

### Edit a service in the default namespace

```bash
kubectl edit [svc|service]/service_name
```

### Edit all entries of a given resource in a given namespace

```bash
kubectl edit resource [-n|--namespace] namespace
```

### Edit a resource using a specific editor

```bash
KUBE_EDITOR=nano kubectl edit resource/resource_name
```

### Edit a resource in JSON format

```bash
kubectl edit resource/resource_name [-o|--output] json
```
