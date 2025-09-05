# aws-ce

> Run cost management operations through the AWS Cost Explorer service. More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/index.html>.

## Examples

### Create anomaly monitor

```bash
aws ce create-anomaly-monitor --monitor monitor_name --monitor-type monitor_type
```

### Create anomaly subscription

```bash
aws ce create-anomaly-subscription --subscription subscription_name --monitor-arn monitor_arn --subscribers subscribers
```

### Get anomalies

```bash
aws ce get-anomalies --monitor-arn monitor_arn --start-time start_time --end-time end_time
```

### Get cost and usage

```bash
aws ce get-cost-and-usage --time-period start_date/end_date --granularity granularity --metrics metrics
```

### Get cost forecast

```bash
aws ce get-cost-forecast --time-period start_date/end_date --granularity granularity --metric metric
```

### Get reservation utilization

```bash
aws ce get-reservation-utilization --time-period start_date/end_date --granularity granularity
```

### List cost category definitions

```bash
aws ce list-cost-category-definitions
```

### Tag resource

```bash
aws ce tag-resource --resource-arn resource_arn --tags tags
```
