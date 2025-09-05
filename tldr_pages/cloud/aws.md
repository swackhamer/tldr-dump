# aws

> The official CLI tool for Amazon Web Services. Some subcommands such as `s3` have their own usage documentation. More information: <https://aws.amazon.com/cli>.

## Examples

### Configure the AWS Command-line

```bash
aws configure wizard
```

### Configure the AWS Command-line using SSO

```bash
aws configure sso
```

### Get the caller identity (used to troubleshoot permissions)

```bash
aws sts get-caller-identity
```

### List AWS resources in a region and output in YAML

```bash
aws dynamodb list-tables --region us-east-1 --output yaml
```

### Use auto prompt to help with a command

```bash
aws iam create-user --cli-auto-prompt
```

### Get an interactive wizard for an AWS resource

```bash
aws dynamodb wizard new_table
```

### Generate a JSON CLI Skeleton (useful for infrastructure as code)

```bash
aws dynamodb update-table --generate-cli-skeleton
```

### Display help for a specific command

```bash
aws command help
```
