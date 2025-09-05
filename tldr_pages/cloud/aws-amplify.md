# aws-amplify

> Development platform for building secure, scalable mobile and web applications. More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/index.html>.

## Examples

### Create a new Amplify app

```bash
aws amplify create-app --name app_name --description description --repository repo_url --platform platform --environment-variables env_vars --tags tags
```

### Delete an existing Amplify app

```bash
aws amplify delete-app --app-id app_id
```

### Get details of a specific Amplify app

```bash
aws amplify get-app --app-id app_id
```

### List all Amplify apps

```bash
aws amplify list-apps
```

### Update settings of an Amplify app

```bash
aws amplify update-app --app-id app_id --name new_name --description new_description --repository new_repo_url --environment-variables new_env_vars --tags new_tags
```

### Add a new backend environment to an Amplify app

```bash
aws amplify create-backend-environment --app-id app_id --environment-name env_name --deployment-artifacts artifacts
```

### Remove a backend environment from an Amplify app

```bash
aws amplify delete-backend-environment --app-id app_id --environment-name env_name
```

### List all backend environments in an Amplify app

```bash
aws amplify list-backend-environments --app-id app_id
```
