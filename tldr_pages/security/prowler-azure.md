# prowler-azure

> Assess Azure security best practices, perform audits, compliance checks, and generate reports. See also: `prowler`, `prowler-aws`, `prowler-gcp`, `prowler-kubernetes`, `prowler-m365`, `prowler-github`. More information: <https://docs.prowler.com/projects/prowler-open-source/en/latest/>.

## Examples

### Run the default set of checks on the current Azure account using Azure CLI authentication

```bash
prowler azure --az-cli-auth
```

### Run checks for specific Azure subscriptions

```bash
prowler azure --az-cli-auth --subscription-ids subscription_id1 subscription_id2 ...
```

### Authenticate using a service principal via environment variables

```bash
prowler azure --sp-env-auth
```

### Authenticate using browser login and specify a tenant ID

```bash
prowler azure --browser-auth --tenant-id "XXXXXXXX"
```

### Authenticate using a managed identity (e.g. for Azure VM)

```bash
prowler azure --managed-identity-auth
```

### Run checks for selected Azure services

```bash
prowler azure [-s|--services] defender iam ...
```

### Run a specific Azure check

```bash
prowler azure [-c|--checks] storage_blob_public_access_level_is_disabled
```

### Exclude specific checks or services

```bash
prowler azure [-e|--excluded-checks] storage_blob_public_access_level_is_disabled --exclude-services defender iam ...
```
