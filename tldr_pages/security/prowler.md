# prowler

> Performs security best practices assessments, audits and compliance checks across AWS, Azure, Google Cloud, and Kubernetes. See also: `prowler-aws`, `prowler-azure`, `prowler-gcp`, `prowler-kubernetes`, `prowler-m365`, `prowler-github`. More information: <https://docs.prowler.com/projects/prowler-open-source/en/latest/>.

## Examples

### Run an AWS, Azure, GCP, Kubernetes - as provider - audit with default checks

```bash
prowler provider
```

### Show all available checks for a specific provider

```bash
prowler provider [-l|--list-checks]
```

### Show all available services for a specific provider

```bash
prowler provider --list-services
```

### Generate output in multiple formats, including JSON-ASFF for AWS Security Hub

```bash
prowler provider --output-modes csv,json-asff,html,...
```

### Execute in verbose mode

```bash
prowler provider --verbose
```

### Filter findings by status

```bash
prowler provider --status PASS,FAIL,MANUAL
```

### Display help

```bash
prowler --help
```

### Display version

```bash
prowler [-v|--version]
```
