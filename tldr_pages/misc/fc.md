# fc

> Open the most recent command for editing and then run it. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-fc>.

## Examples

### Open the last command in the default system editor and run it after editing

```bash
fc
```

### Specify an editor to open with

```bash
fc -e 'emacs'
```

### List recent commands from history

```bash
fc -l
```

### List recent commands in reverse order

```bash
fc -l -r
```

### Edit and run a command from history

```bash
fc number
```

### Edit commands in a given interval and run them

```bash
fc '416' '420'
```

### Display help

```bash
fc --help
```
