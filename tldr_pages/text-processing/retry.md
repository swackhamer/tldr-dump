# retry

> Repeat command until it succeeds or a criterion is met. More information: <https://github.com/minfrin/retry>.

## Examples

### Retry a command until it succeeds

```bash
retry command
```

### Retry a command every n seconds until it succeeds

```bash
retry --delay=n command
```

### Give up after n attempts

```bash
retry --times=n command
```
