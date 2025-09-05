# vipe

> Run a text editor in the middle of a UNIX pipeline. More information: <https://manned.org/vipe>.

## Examples

### Edit the output of `command1` before piping it into `command2`

```bash
command1 | vipe | command2
```

### Buffer the output of `command1` in a temporary file with the specified file extension in order to aid syntax highlighting

```bash
command1 | vipe --suffix json | command2
```

### Use the specified text editor

```bash
command1 | EDITOR=vim vipe | command2
```
