# npm-config

> Manage the `npm` configuration settings. More information: <https://docs.npmjs.com/cli/npm-config>.

## Examples

### Show all configuration settings

```bash
npm [c|config] list
```

### List all configuration settings as `JSON`

```bash
npm [c|config] list --json
```

### Get the value of a specific configuration key

```bash
npm [c|config] get key
```

### Set a configuration key to a specific value

```bash
npm [c|config] set key value
```

### Delete a configuration key

```bash
npm [c|config] delete key
```

### Edit the global npm configuration file in the default editor

```bash
npm [c|config] edit
```

### Attempt to repair invalid configuration items

```bash
npm [c|config] fix
```
