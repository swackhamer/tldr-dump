# aws-glue

> CLI for AWS Glue. Define the public endpoint for the AWS Glue service. More information: <https://docs.aws.amazon.com/cli/latest/reference/glue/>.

## Examples

### List jobs

```bash
aws glue list-jobs
```

### Start a job

```bash
aws glue start-job-run --job-name job_name
```

### Start running a workflow

```bash
aws glue start-workflow-run --name workflow_name
```

### List triggers

```bash
aws glue list-triggers
```

### Start a trigger

```bash
aws glue start-trigger --name trigger_name
```

### Create a dev endpoint

```bash
aws glue create-dev-endpoint --endpoint-name name --role-arn role_arn_used_by_endpoint
```
