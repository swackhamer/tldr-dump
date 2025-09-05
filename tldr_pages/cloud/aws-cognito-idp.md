# aws-cognito-idp

> Configure an Amazon Cognito user pool and its users and groups and authenticate them. More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html>.

## Examples

### Create a new Cognito user pool

```bash
aws cognito-idp create-user-pool --pool-name name
```

### List all user pools

```bash
aws cognito-idp list-user-pools --max-results 10
```

### Delete a specific user pool

```bash
aws cognito-idp delete-user-pool --user-pool-id user_pool_id
```

### Create a user in a specific pool

```bash
aws cognito-idp admin-create-user --username username --user-pool-id user_pool_id
```

### List the users of a specific pool

```bash
aws cognito-idp list-users --user-pool-id user_pool_id
```

### Delete a user from a specific pool

```bash
aws cognito-idp admin-delete-user --username username --user-pool-id user_pool_id
```
