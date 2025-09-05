# arch

> Display the name of the system architecture, or run a command under a different architecture. See also: `uname`. More information: <https://keith.github.io/xcode-man-pages/arch.1.html>.

## Examples

### Display the system's architecture

```bash
arch
```

### Run a command using x86_64

```bash
arch -x86_64 "command"
```

### Run a command using arm

```bash
arch -arm64 "command"
```
