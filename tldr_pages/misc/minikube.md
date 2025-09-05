# minikube

> Run Kubernetes locally. More information: <https://minikube.sigs.k8s.io/docs/>.

## Examples

### Start the cluster

```bash
minikube start
```

### Get the IP address of the cluster

```bash
minikube ip
```

### Access a service named my_service exposed via a node port and get the URL

```bash
minikube service my_service --url
```

### Open the Kubernetes dashboard in a browser

```bash
minikube dashboard
```

### Stop the running cluster

```bash
minikube stop
```

### Delete the cluster

```bash
minikube delete
```

### Connect to LoadBalancer services

```bash
minikube tunnel
```
