# kustomize

> Easily deploy resources for Kubernetes. More information: <https://github.com/kubernetes-sigs/kustomize>.

## Examples

### Create a kustomization file with resources and namespace

```bash
kustomize create --resources deployment.yaml,service.yaml --namespace staging
```

### Build a kustomization file and deploy it with `kubectl`

```bash
kustomize build . | kubectl apply [-f|--filename] -
```

### Set an image in the kustomization file

```bash
kustomize edit set image busybox=alpine:3.6
```

### Search for Kubernetes resources in the current directory to be added to the kustomization file

```bash
kustomize create --autodetect
```
