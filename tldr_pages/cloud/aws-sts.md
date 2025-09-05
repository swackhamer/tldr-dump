# aws-sts

> Security Token Service (STS) allows to request temporary credentials for (IAM) users or federated users. More information: <https://docs.aws.amazon.com/cli/latest/reference/sts/>.

## Examples

### Get temporary security credentials to access specific AWS resources

```bash
aws sts assume-role --role-arn aws_role_arn
```

### Get an IAM user or role whose credentials are used to call the operation

```bash
aws sts get-caller-identity
```
