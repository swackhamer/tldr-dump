# prowler-kubernetes

> Assess Kubernetes cluster security best practices and configurations. See also: `prowler`, `prowler-aws`, `prowler-azure`, `prowler-gcp`, `prowler-m365`, `prowler-github`. More information: <https://docs.prowler.com/projects/prowler-open-source/en/latest/>.

## Examples

### Run the default checks using the default kubeconfig location

```bash
prowler kubernetes
```

### Specify a custom kubeconfig file for scanning

```bash
prowler kubernetes --kubeconfig-file path/to/kubeconfig
```

### Specify a specific Kubernetes context to scan

```bash
prowler kubernetes --context my-context
```

### Scan specific namespaces only

```bash
prowler kubernetes --namespaces default kube-system
```

### Run checks for selected Kubernetes services

```bash
prowler kubernetes [-s|--services] ietcd apiserver ...
```

### Run a specific Kubernetes check

```bash
prowler kubernetes [-c|--checks] etcd_encryption
```

### Exclude specific checks or services

```bash
prowler kubernetes [-e|--excluded-checks] etcd_encryption --exclude-services ietcd apiserver ...
```
