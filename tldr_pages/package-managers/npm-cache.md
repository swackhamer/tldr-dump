# npm-cache

> Manage the npm package cache. More information: <https://docs.npmjs.com/cli/npm-cache>.

## Examples

### Add a specific package to the cache

```bash
npm cache add package_name
```

### Remove a specific package from the cache

```bash
npm cache remove package_name
```

### Clear a specific cached item by key

```bash
npm cache clean key
```

### Clear the entire npm cache

```bash
npm cache clean --force
```

### List the contents of the npm cache

```bash
npm cache ls
```

### Verify the integrity of the npm cache

```bash
npm cache verify
```

### Show the cache path

```bash
npm [c|config] get cache
```

### Change the cache path

```bash
npm [c|config] set cache path/to/directory
```
