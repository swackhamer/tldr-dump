# gcloud-logging-logs-list

> List logs in a Google Cloud project. Useful for identifying available logs for monitoring and analysis. See also: `gcloud`. More information: <https://cloud.google.com/sdk/gcloud/reference/logging/logs/list>.

## Examples

### List all logs in the current project

```bash
gcloud logging logs list
```

### List all logs for a specific log bucket and location

```bash
gcloud logging logs list --bucket=bucket_id --location=location
```

### List all logs for a specific view in a log bucket

```bash
gcloud logging logs list --bucket=bucket_id --location=location --view=view_id
```

### List logs with a filter expression

```bash
gcloud logging logs list --filter="expression"
```

### List a specified number of logs

```bash
gcloud logging logs list --limit=number
```

### List logs sorted by a specific field in ascending or descending order (`~` for descending)

```bash
gcloud logging logs list --sort-by="field_name"
```

### List logs sorted by multiple fields

```bash
gcloud logging logs list --sort-by="field1,~field2"
```

### List logs with verbose output, showing additional details

```bash
gcloud logging logs list --verbosity=debug
```
