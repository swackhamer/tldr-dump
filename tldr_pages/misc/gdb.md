# gdb

> The GNU Debugger. More information: <https://sourceware.org/gdb/current/onlinedocs/gdb#Invocation>.

## Examples

### Debug an executable

```bash
gdb executable
```

### Attach a process to gdb

```bash
gdb [-p|--pid] procID
```

### Debug with a core file

```bash
gdb [-c|--core] core executable
```

### Execute given GDB commands upon start

```bash
gdb [-ex|--eval-command] "commands" executable
```

### Start `gdb` and pass arguments to the executable

```bash
gdb --args executable argument1 argument2
```

### Skip debuginfod and pagination prompts and then print the backtrace

```bash
gdb [-c|--core] core executable -iex 'set debuginfod enabled on' -iex 'set pagination off' -ex bt
```
