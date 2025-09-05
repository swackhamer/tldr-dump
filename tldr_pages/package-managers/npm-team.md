# npm-team

> Manage teams in an organization on the `npm` registry. More information: <https://docs.npmjs.com/cli/npm-team>.

## Examples

### Add a user to a team in an organization

```bash
npm team add organization:team username
```

### Remove a user from a team

```bash
npm team rm organization:team username
```

### Create a new team in an organization

```bash
npm team create organization:team
```

### Delete a team from an organization

```bash
npm team destroy organization:team
```

### List all teams in an organization

```bash
npm team ls organization
```

### List all users in a specific team

```bash
npm team ls organization:team
```
