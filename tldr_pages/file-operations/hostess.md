# hostess

> Manage the `/etc/hosts` file. More information: <https://github.com/cbednarski/hostess>.

## Examples

### List domains, target IP addresses and on/off status

```bash
hostess list
```

### Add a domain pointing to your machine to your hosts file

```bash
hostess add local.example.com 127.0.0.1
```

### Remove a domain from your hosts file

```bash
hostess del local.example.com
```

### Disable a domain (but don't remove it)

```bash
hostess off local.example.com
```
