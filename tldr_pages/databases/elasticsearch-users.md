# elasticsearch-users

> Manage native realm users in Elasticsearch, including creating, updating, and deleting users. More information: <https://www.elastic.co/guide/en/elasticsearch/reference/current/users-command.html>.

## Examples

### Add a new user interactively (prompts for password)

```bash
elasticsearch-users useradd username
```

### Add a new user and specify roles

```bash
elasticsearch-users useradd username -r role1,role2
```

### Change the password for an existing user

```bash
elasticsearch-users passwd username
```

### Delete a user

```bash
elasticsearch-users userdel username
```

### List all users in the native realm

```bash
elasticsearch-users list
```
