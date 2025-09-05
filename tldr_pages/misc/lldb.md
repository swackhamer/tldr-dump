# lldb

> The LLVM Low-Level Debugger. More information: <https://lldb.llvm.org/man/lldb.html>.

## Examples

### Debug an executable

```bash
lldb "executable"
```

### Attach `lldb` to a running process with a given PID

```bash
lldb -p pid
```

### Wait for a new process to launch with a given name, and attach to it

```bash
lldb -w -n "process_name"
```
