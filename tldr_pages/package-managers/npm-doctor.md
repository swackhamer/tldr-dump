# npm-doctor

> Check the health of the npm environment. More information: <https://docs.npmjs.com/cli/npm-doctor>.

## Examples

### Run all default health checks for `npm`

```bash
npm doctor
```

### Check the connection to the `npm` registry

```bash
npm doctor connection
```

### Check the versions of Node.js and `npm` in use

```bash
npm doctor versions
```

### Check for permissions issues with `npm` directories and cache

```bash
npm doctor permissions
```

### Validate the cached package files and checksums

```bash
npm doctor cache
```
