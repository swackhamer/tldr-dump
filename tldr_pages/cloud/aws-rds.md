# aws-rds

> Use AWS Relational Database Service, a web service for setting up, operating and scaling relational databases. More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html>.

## Examples

### Display help for a specific RDS subcommand

```bash
aws rds subcommand help
```

### Stop instance

```bash
aws rds stop-db-instance --db-instance-identifier instance_identifier
```

### Start instance

```bash
aws rds start-db-instance --db-instance-identifier instance_identifier
```

### Modify an RDS instance

```bash
aws rds modify-db-instance --db-instance-identifier instance_identifier parameters --apply-immediately
```

### Apply updates to an RDS instance

```bash
aws rds apply-pending-maintenance-action --resource-identifier database_arn --apply-action system-update --opt-in-type immediate
```

### Change an instance identifier

```bash
aws rds modify-db-instance --db-instance-identifier old_instance_identifier --new-db-instance-identifier new_instance_identifier
```

### Reboot an instance

```bash
aws rds reboot-db-instance --db-instance-identifier instance_identifier
```

### Delete an instance

```bash
aws rds delete-db-instance --db-instance-identifier instance_identifier --final-db-snapshot-identifier snapshot_identifier --delete-automated-backups
```
