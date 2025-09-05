# gcpdiag

> Google Cloud Platform troubleshooting and diagnostics tool. Run in a Docker container or in GCP Cloudshell. More information: <https://github.com/GoogleCloudPlatform/gcpdiag>.

## Examples

### Run `gcpdiag` on your project, returning all rules

```bash
gcpdiag lint --project=gcp_project_id
```

### Hide rules that are ok

```bash
gcpdiag lint --project=gcp_project_id --hide-ok
```

### Authenticate using a service account private key file

```bash
gcpdiag lint --project=gcp_project_id --auth-key path/to/private_key
```

### Search logs and metrics from a number of days back (default: 3 days)

```bash
gcpdiag lint --project=gcp_project_id --within-days number
```

### Display help

```bash
gcpdiag lint --help
```
