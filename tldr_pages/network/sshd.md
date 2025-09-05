# sshd

> Secure Shell Daemon - allows remote machines to securely log in to the current machine. Remote machines can execute commands as it is executed at this machine. More information: <https://man.openbsd.org/sshd>.

## Examples

### Start daemon in the background

```bash
sshd
```

### Run sshd in the foreground

```bash
sshd -D
```

### Run with verbose output (for debugging)

```bash
sshd -D -d
```

### Run on a specific port

```bash
sshd -p port
```
