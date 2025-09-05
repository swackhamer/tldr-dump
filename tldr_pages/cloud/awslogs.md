# awslogs

> Queries groups, streams and events from Amazon CloudWatch logs. More information: <https://github.com/jorgebastida/awslogs>.

## Examples

### List log groups

```bash
awslogs groups
```

### List existing streams for the specified group

```bash
awslogs streams /var/log/syslog
```

### Get logs for any streams in the specified group between 1 and 2 hours ago

```bash
awslogs get /var/log/syslog [-s|--start] '2h ago' [-e|--end] '1h ago'
```

### Get logs that match a specific CloudWatch Logs Filter pattern

```bash
awslogs get /aws/lambda/my_lambda_group --filter-pattern 'ERROR'
```

### Watch logs for any streams in the specified group

```bash
awslogs get /var/log/syslog ALL --watch
```
