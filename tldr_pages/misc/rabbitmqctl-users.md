# rabbitmqctl-users

> Manage RabbitMQ users, their permissions, and tags. More information: <https://www.rabbitmq.com/management.html>.

## Examples

### List all users

```bash
rabbitmqctl list_users
```

### Add a new user with a password

```bash
rabbitmqctl add_user username password
```

### Delete an existing user

```bash
rabbitmqctl delete_user username
```

### Change the password for a user

```bash
rabbitmqctl change_password username new_password
```

### Set permissions for a user on a specific virtual host

```bash
rabbitmqctl set_permissions [-p|--vhost] vhost username read write configure
```

### Clear all permissions for a user on a specific virtual host

```bash
rabbitmqctl clear_permissions [-p|--vhost] vhost username
```

### Assign one or more tags (e.g., administrator) to a user

```bash
rabbitmqctl set_user_tags username tag1 [tag2]
```
