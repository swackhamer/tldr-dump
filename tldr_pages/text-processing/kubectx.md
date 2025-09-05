# kubectx

> Utility to manage and switch between `kubectl` contexts. More information: <https://manned.org/kubectx>.

## Examples

### List the contexts

```bash
kubectx
```

### Switch to a named context

```bash
kubectx name
```

### Switch to the previous context

```bash
kubectx -
```

### Rename a named context

```bash
kubectx alias=name
```

### Show the current named context

```bash
kubectx [-c|--current]
```

### Delete a named context

```bash
kubectx -d name
```
