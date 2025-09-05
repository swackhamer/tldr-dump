# herd-list

> List available commands in the Herd PHP platform. See also: `herd`. More information: <https://herd.laravel.com>.

## Examples

### List all available commands

```bash
herd list
```

### List all available commands in a specific namespace

```bash
herd list namespace
```

### List all commands in raw format (useful for embedding a command runner)

```bash
herd list --raw
```

### Display the list in a specific output format

```bash
herd list --format txt|xml|json|md
```

### List all commands without describing their arguments

```bash
herd list --short
```
