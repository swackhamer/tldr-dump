# trufflehog

> Find and verify credentials in files, Git repositories, S3 buckets, and Docker images. More information: <https://github.com/trufflesecurity/trufflehog>.

## Examples

### Scan a Git repository for verified secrets

```bash
trufflehog git https://github.com/trufflesecurity/test_keys --only-verified
```

### Scan a GitHub organization for verified secrets

```bash
trufflehog github --org trufflesecurity --only-verified
```

### Scan a GitHub repository for verified keys and get JSON output

```bash
trufflehog git https://github.com/trufflesecurity/test_keys --only-verified --json
```

### Scan a GitHub repository along with its Issues and Pull Requests

```bash
trufflehog github --repo https://github.com/trufflesecurity/test_keys --issue-comments --pr-comments
```

### Scan an S3 bucket for verified keys

```bash
trufflehog s3 --bucket bucket name --only-verified
```

### Scan S3 buckets using IAM Roles

```bash
trufflehog s3 --role-arn iam-role-arn
```

### Scan individual files or directories

```bash
trufflehog filesystem path/to/file_or_directory1 path/to/file_or_directory2 ...
```

### Scan a Docker image for verified secrets

```bash
trufflehog docker --image trufflesecurity/secrets --only-verified
```
