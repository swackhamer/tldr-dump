# mise

> Manage language runtimes like Node.js, Python, Ruby, Go, Java, etc and various tools. More information: <https://mise.jdx.dev>.

## Examples

### List all available plugins

```bash
mise plugins list-all
```

### Install a plugin

```bash
mise plugins add name
```

### List runtime versions available for install

```bash
mise ls-remote name
```

### Install a specific version of a package

```bash
mise install name@version
```

### Set global version for a package

```bash
mise use --global name@version
```

### Set local version for a package

```bash
mise use name@version
```

### Set environment variable in configuration

```bash
mise set variable=value
```

### Pass plugin options

```bash
mise use name\[option1=option1_value,option2=option2_value\]@version
```
