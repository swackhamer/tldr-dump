# zmv

> Move or rename files matching a specified extended glob pattern. See also: `zcp`, `zln`. More information: <https://zsh.sourceforge.net/Doc/Release/User-Contributions.html>.

## Examples

### Move files using a `regex`-like pattern

```bash
zmv '(*).log' '$1.txt'
```

### Preview the result of a move, without making any actual changes

```bash
zmv -n '(*).log' '$1.txt'
```

### Interactively move files, with a prompt before every change

```bash
zmv -i '(*).log' '$1.txt'
```

### Verbosely print each action as it's being executed

```bash
zmv -v '(*).log' '$1.txt'
```
