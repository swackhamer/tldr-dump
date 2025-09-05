# auditd

> This responds to requests from the audit utility and notifications from the kernel. It should not be invoked manually. More information: <https://manned.org/auditd>.

## Examples

### Start the daemon

```bash
auditd
```

### Start the daemon in debug mode

```bash
auditd -d
```

### Start the daemon on-demand from launchd

```bash
auditd -l
```
