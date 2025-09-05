# aws-backup

> Unified backup service designed to protect Amazon Web Services services and their associated data. More information: <https://docs.aws.amazon.com/cli/latest/reference/backup/index.html>.

## Examples

### Return BackupPlan details for a specific BackupPlanId

```bash
aws backup get-backup-plan --backup-plan-id id
```

### Create a backup plan using a specific backup plan name and backup rules

```bash
aws backup create-backup-plan --backup-plan plan
```

### Delete a specific backup plan

```bash
aws backup delete-backup-plan --backup-plan-id id
```

### List all active backup plans for the current account

```bash
aws backup list-backup-plans
```

### Display details about your report jobs

```bash
aws backup list-report-jobs
```
