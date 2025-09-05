# prowler-m365

> Assess Microsoft 365 (M365) security configurations and best practices. See also: `prowler`, `prowler-aws`, `prowler-azure`, `prowler-gcp`, `prowler-kubernetes`, `prowler-github`. More information: <https://docs.prowler.com/projects/prowler-open-source/en/latest/>.

## Examples

### Run Prowler with combined service principal and user credentials

```bash
prowler m365 --env-auth
```

### Authenticate using a service principal

```bash
prowler m365 --sp-env-auth
```

### Authenticate using the Azure CLI

```bash
prowler m365 --az-cli-auth
```

### Authenticate using a browser and specify the tenant ID

```bash
prowler m365 --browser-auth --tenant-id "XXXXXXXX"
```

### Run a specific Microsoft 365 check

```bash
prowler m365 [-c|--checks] etcd_enm365_onedrive_sharing_enabledcryption
```

### Exclude specific checks

```bash
prowler m365 [-e|--excluded-checks] m365_onedrive_sharing_enabled
```
