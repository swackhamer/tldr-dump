# aws-lightsail

> Manage Amazon Lightsail resources. More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html>.

## Examples

### List all virtual private servers, or instances

```bash
aws lightsail get-instances
```

### List all bundles (instance plans)

```bash
aws lightsail list-bundles
```

### List all available instance images, or blueprints

```bash
aws lightsail list-blueprints
```

### Create an instance

```bash
aws lightsail create-instances --instance-names name --availability-zone region --bundle-id nano_2_0 --blueprint-id blueprint_id
```

### Print the state of a specific instance

```bash
aws lightsail get-instance-state --instance-name name
```

### Stop a specific instance

```bash
aws lightsail stop-instance --instance-name name
```

### Delete a specific instance

```bash
aws lightsail delete-instance --instance-name name
```
