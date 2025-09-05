# salt-call

> Invoke salt locally on a salt minion. More information: <https://docs.saltproject.io/en/latest/ref/cli/salt-call.html>.

## Examples

### Perform a highstate on this minion

```bash
salt-call state.highstate
```

### Perform a highstate dry-run, compute all changes but don't actually perform them

```bash
salt-call state.highstate test=true
```

### Perform a highstate with verbose debugging output

```bash
salt-call [-l|--log-level] debug state.highstate
```

### List this minion's grains

```bash
salt-call grains.items
```
