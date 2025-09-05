# radare2

> A set of reverse engineering tools. More information: <https://www.radare.org/r/docs.html>.

## Examples

### Open a file in write mode without parsing the file format headers

```bash
radare2 -nw path/to/binary
```

### Debug a program

```bash
radare2 -d path/to/binary
```

### Run a script before entering the interactive CLI

```bash
radare2 -i path/to/script.r2 path/to/binary
```

### Display help text for any command in the interactive CLI

```bash
radare2_command?
```

### Run a shell command from the interactive CLI

```bash
!shell_command
```

### Dump raw bytes of current block to a file

```bash
> pr > path/to/file.bin
```
