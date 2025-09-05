# phive

> The Phar Installation and Verification Environment for secure PHP application deployment. More information: <https://phar.io/#Usage>.

## Examples

### Display a list of available aliased Phars

```bash
phive list
```

### Install a specified Phar to the local directory

```bash
phive install alias|url
```

### Install a specified Phar globally

```bash
phive install alias|url [-g|--global]
```

### Install a specified Phar to a target directory

```bash
phive install alias|url [-t|--target] path/to/directory
```

### Update all Phar files to the latest version

```bash
phive update
```

### Remove a specified Phar file

```bash
phive remove alias|url
```

### Remove unused Phar files

```bash
phive purge
```

### List all available commands

```bash
phive help
```
