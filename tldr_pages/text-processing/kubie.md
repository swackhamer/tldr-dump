# kubie

> Utility to switch between `kubectl` contexts and namespaces. More information: <https://github.com/sbstp/kubie>.

## Examples

### Display a selectable menu of contexts

```bash
kubie ctx
```

### Switch current shell to the given context

```bash
kubie ctx context
```

### Switch current shell to the given namespace

```bash
kubie ns namespace
```

### Switch current shell to the given context and namespace

```bash
kubie ctx context -n namespace
```

### Execute a command in the given context and namespace, without spawning a shell

```bash
kubie exec context namespace command
```

### Check the Kubernetes configuration files for issues

```bash
kubie lint
```
