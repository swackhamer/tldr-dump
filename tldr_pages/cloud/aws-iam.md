# aws-iam

> Interact with Identity and Access Management (IAM), a web service for securely controlling access to AWS services. More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>.

## Examples

### List users

```bash
aws iam list-users
```

### List policies

```bash
aws iam list-policies
```

### List groups

```bash
aws iam list-groups
```

### Get users in a group

```bash
aws iam get-group --group-name group_name
```

### Describe an IAM policy

```bash
aws iam get-policy --policy-arn arn:aws:iam::aws:policy/policy_name
```

### List access keys

```bash
aws iam list-access-keys
```

### List access keys for a specific user

```bash
aws iam list-access-keys --user-name user_name
```

### Display help

```bash
aws iam help
```
