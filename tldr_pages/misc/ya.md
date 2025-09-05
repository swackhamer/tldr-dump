# ya

> Manage Yazi packages and plugins. More information: <https://github.com/sxyazi/yazi>.

## Examples

### Add a package

```bash
ya pack [-a|--all] package
```

### Upgrade all packages

```bash
ya pack [-u|--upgrade]
```

### Subscribe to messages from all remote instances

```bash
ya sub kinds
```

### Publish a message to the current instance with string body

```bash
ya pub --str string_message
```

### Publish a message to the current instance with JSON body

```bash
ya pub --json json_message
```

### Publish a message to the specified instance with string body

```bash
ya pub-to --str message receiver kind
```
