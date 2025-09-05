# npm-access

> Set access level on published packages. More information: <https://docs.npmjs.com/cli/npm-access>.

## Examples

### List packages for a user or scope

```bash
npm access list packages user|scope|scope:team package_name
```

### List collaborators on a package

```bash
npm access list collaborators package_name username
```

### Get status of a package

```bash
npm access get status package_name
```

### Set package status (public or private)

```bash
npm access set status public|private package_name
```

### Grant access to a package

```bash
npm access grant read-only|read-write scope:team package_name
```

### Revoke access to a package

```bash
npm access revoke scope:team package_name
```

### Configure two-factor authentication requirement

```bash
npm access set mfa none|publish|automation package_name
```
