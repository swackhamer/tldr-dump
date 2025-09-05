# aws-vault

> A vault for securely storing and accessing AWS credentials in development environments. More information: <https://github.com/99designs/aws-vault>.

## Examples

### Add credentials to the secure keystore

```bash
aws-vault add profile
```

### Execute a command with AWS credentials in the environment

```bash
aws-vault exec profile -- aws s3 ls
```

### Open a browser window and login to the AWS Console

```bash
aws-vault login profile
```

### List profiles, along with their credentials and sessions

```bash
aws-vault list
```

### Rotate AWS credentials

```bash
aws-vault rotate profile
```

### Remove credentials from the secure keystore

```bash
aws-vault remove profile
```
