# kubectl-autoscale

> Create an autoscaler to intelligently scale pod count based on kubernetes cluster demands. More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#autoscale>.

## Examples

### Auto scale a deployment with no target CPU utilization specified

```bash
kubectl autoscale [deploy|deployment] deployment_name --min=min_replicas --max=max_replicas
```

### Auto scale a deployment with target CPU utilization

```bash
kubectl autoscale [deploy|deployment] deployment_name --max=max_replicas --cpu-percent=target_cpu
```
