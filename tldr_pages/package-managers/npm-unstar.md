# npm-unstar

> Remove the favorite/star mark from a package. More information: <https://docs.npmjs.com/cli/npm-unstar>.

## Examples

### Unstar a public package from the default registry

```bash
npm unstar package_name
```

### Unstar a package within a specific scope

```bash
npm unstar @scope/package_name
```

### Unstar a package from a specific registry

```bash
npm unstar package_name --registry registry_url
```

### Unstar a private package that requires authentication

```bash
npm unstar package_name --auth-type legacy|oauth|web|saml
```

### Unstar a package by providing an OTP for two-factor authentication

```bash
npm unstar package_name --otp otp
```

### Unstar a package with a specific logging level

```bash
npm unstar package_name --loglevel silent|error|warn|notice|http|timing|info|verbose|silly
```
