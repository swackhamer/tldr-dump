# npm-org

> Manage organizations. More information: <https://docs.npmjs.com/cli/npm-org>.

## Examples

### Add a new user to an organization

```bash
npm org set organization_name username
```

### Change a user's role in an organization

```bash
npm org set organization_name username developer|admin|owner
```

### Remove a user from an organization

```bash
npm org rm organization_name username
```

### List all users in an organization

```bash
npm org ls organization_name
```

### List all users in an organization, output in JSON format

```bash
npm org ls organization_name --json
```

### Display a user's role in an organization

```bash
npm org ls organization_name username
```
