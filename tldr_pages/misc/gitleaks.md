# gitleaks

> Detect secrets and API keys leaked in Git repositories. More information: <https://github.com/gitleaks/gitleaks>.

## Examples

### Scan a remote repository

```bash
gitleaks detect --repo-url https://github.com/username/repository.git
```

### Scan a local directory

```bash
gitleaks detect --source path/to/repository
```

### Output scan results to a JSON file

```bash
gitleaks detect --source path/to/repository --report path/to/report.json
```

### Use a custom rules file

```bash
gitleaks detect --source path/to/repository --config-path path/to/config.toml
```

### Start scanning from a specific commit

```bash
gitleaks detect --source path/to/repository --log-opts --since=commit_id
```

### Scan uncommitted changes before a commit

```bash
gitleaks protect --staged
```

### Display verbose output indicating which parts were identified as leaks during the scan

```bash
gitleaks protect --staged --verbose
```
