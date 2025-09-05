# npm-token

> Manage and generate authentication tokens for the npm registry. More information: <https://docs.npmjs.com/cli/npm-token>.

## Examples

### Create a new authentication token

```bash
npm token create
```

### List all tokens associated with an account

```bash
npm token list
```

### Delete a specific token using its token ID

```bash
npm token revoke token_id
```

### Create a token with read-only access

```bash
npm token create --read-only
```

### Create a token with publish access

```bash
npm token create --publish
```

### Automatically configure an npm token in your global `.npmrc` file when you log in

```bash
npm login
```

### Remove a token from the global configuration

```bash
npm token revoke token_id
```
