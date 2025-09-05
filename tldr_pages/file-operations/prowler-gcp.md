# prowler-gcp

> Assess Google Cloud Platform (GCP) security best practices, audits, and compliance checks. See also: `prowler`, `prowler-aws`, `prowler-azure`, `prowler-kubernetes`, `prowler-m365`, `prowler-github`. More information: <https://docs.prowler.com/projects/prowler-open-source/en/latest/>.

## Examples

### Run the default set of checks on all accessible GCP projects using default user credentials

```bash
prowler gcp
```

### Authenticate using a service account credentials file

```bash
prowler gcp --credentials-file path/to/credentials.json
```

### Scan specific GCP projects by ID

```bash
prowler gcp --project-ids project_id1 project_id2 ...
```

### Run checks for selected GCP services

```bash
prowler gcp [-s|--services] iam compute ...
```

### Run a specific GCP check

```bash
prowler gcp [-c|--checks] gcp_storage_bucket_logging_enabled
```

### Exclude specific checks or services

```bash
prowler gcp [-e|--excluded-checks] gcp_storage_bucket_logging_enabled --exclude-services iam compute ...
```
