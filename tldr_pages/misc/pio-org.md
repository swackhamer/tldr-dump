# pio-org

> Manage PlatformIO organizations and their owners. More information: <https://docs.platformio.org/en/latest/core/userguide/org/>.

## Examples

### Create a new organization

```bash
pio org create organization_name
```

### Delete an organization

```bash
pio org destroy organization_name
```

### Add a user to an organization

```bash
pio org add organization_name username
```

### Remove a user from an organization

```bash
pio org remove organization_name username
```

### List all organizations the current user is a member of and their owners

```bash
pio org list
```

### Update the name, email or display name of an organization

```bash
pio org update --orgname new_organization_name --email new_email --displayname new_display_name organization_name
```
