# trivy

> Scanner for vulnerabilities in container images, file systems, and Git repositories, as well as for configuration issues. More information: <https://aquasecurity.github.io/trivy>.

## Examples

### Scan a Docker image for vulnerabilities and exposed secrets

```bash
trivy image image:tag
```

### Scan a Docker image filtering the output by severity

```bash
trivy image [-s|--severity] HIGH,CRITICAL alpine:3.15
```

### Scan a Docker image ignoring any unfixed/unpatched vulnerabilities

```bash
trivy image --ignore-unfixed alpine:3.15
```

### Scan the filesystem for vulnerabilities and misconfigurations

```bash
trivy fs --security-checks vuln,config path/to/project_directory
```

### Scan a IaC (Terraform, CloudFormation, ARM, Helm and Dockerfile) directory for misconfigurations

```bash
trivy config path/to/iac_directory
```

### Scan a local or remote Git repository for vulnerabilities

```bash
trivy repo path/to/local_repository_directory|remote_repository_URL
```

### Scan a Git repository up to a specific commit hash

```bash
trivy repo --commit commit_hash repository
```

### Generate output with a SARIF template

```bash
trivy image [-f|--format] template [-t|--template] "@sarif.tpl" [-o|--output] path/to/report.sarif image:tag
```
