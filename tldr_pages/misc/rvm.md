# rvm

> Easily installing, managing, and working with multiple ruby environments. More information: <https://rvm.io>.

## Examples

### Install one or more versions of Ruby

```bash
rvm install version1 version2 ...
```

### Display a list of installed versions

```bash
rvm list
```

### Use a specific version of Ruby

```bash
rvm use version
```

### Set the default Ruby version

```bash
rvm --default use version
```

### Upgrade a version of Ruby to a new version

```bash
rvm upgrade current_version new_version
```

### Uninstall a version of Ruby and keep its sources

```bash
rvm uninstall version
```

### Remove a version of Ruby and its sources

```bash
rvm remove version
```

### Show specific dependencies for your OS

```bash
rvm requirements
```
