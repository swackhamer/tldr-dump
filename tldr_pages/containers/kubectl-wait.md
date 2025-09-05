# kubectl-wait

> Wait for resource(s) to reach a certain state. More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#wait>.

## Examples

### Wait for a deployment to become available

```bash
kubectl wait --for=condition=available deployment/deployment_name
```

### Wait for all pods with a certain [l]abel to be ready

```bash
kubectl wait --for=condition=ready pod [-l|--selector] label_key=label_value
```

### Wait for a pod to be deleted

```bash
kubectl wait --for=delete pod pod_name
```

### Wait for a job to complete, within 120 seconds (if the condition isn't met on time, the exit status will be unsuccessful)

```bash
kubectl wait --for=condition=complete job/job_name --timeout 120s
```
