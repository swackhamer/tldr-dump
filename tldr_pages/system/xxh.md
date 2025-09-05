# xxh

> Bring your shell with all of your customizations through SSH sessions. Note: `xxh` does not install anything into system directories on the target machine; removing `~/.xxh` will clear all traces of xxh on the target machine. More information: <https://github.com/xxh/xxh#usage>.

## Examples

### Connect to a host and run the current shell

```bash
xxh "host"
```

### Install the current shell into the target machine without prompting

```bash
xxh "host" ++install
```

### Run the specified shell on the target machine

```bash
xxh "host" ++shell xonsh|zsh|fish|bash|osquery
```

### Use a specific xxh configuration directory on the target machine

```bash
xxh "host" ++host-xxh-home ~/.xxh
```

### Use the specified configuration file on the host machine

```bash
xxh "host" ++xxh-config ~/.config/xxh/config.xxhc
```

### Specify a password to use for the SSH connection

```bash
xxh "host" ++password "password"
```

### Install an xxh package on the target machine

```bash
xxh "host" ++install-xxh-packages package
```

### Set an environment variable for the shell process on the target machine

```bash
xxh "host" ++env name=value
```
