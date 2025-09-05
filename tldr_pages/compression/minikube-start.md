# minikube-start

> Start `minikube` with different configurations. More information: <https://minikube.sigs.k8s.io/docs/commands/start/>.

## Examples

### Start `minikube` with a specific Kubernetes version

```bash
minikube start --kubernetes-version v1.24.0
```

### Start `minikube` with specific resource allocations (e.g., memory and CPU)

```bash
minikube start --memory 2048 --cpus 2
```

### Start `minikube` with a specific driver (e.g., VirtualBox)

```bash
minikube start --driver virtualbox
```

### Start `minikube` in the background (headless mode)

```bash
minikube start --background
```

### Start `minikube` with custom add-ons (e.g., the metrics server)

```bash
minikube start --addons metrics-server
```
