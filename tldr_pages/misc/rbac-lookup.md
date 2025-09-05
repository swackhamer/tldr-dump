# rbac-lookup

> Find roles and cluster roles attached to any user, service account or group name in your Kubernetes cluster. More information: <https://github.com/reactiveops/rbac-lookup>.

## Examples

### View all RBAC bindings

```bash
rbac-lookup
```

### View RBAC bindings that match a given expression

```bash
rbac-lookup search_term
```

### View all RBAC bindings along with the source role binding

```bash
rbac-lookup [-o|--output] wide
```

### View all RBAC bindings filtered by subject

```bash
rbac-lookup [-k|--kind] user|group|serviceaccount
```

### View all RBAC bindings along with IAM roles (if you are using GKE)

```bash
rbac-lookup --gke
```
