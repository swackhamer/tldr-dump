# virsh-help

> Display information about `virsh` commands or command groups. See also: `virsh`. More information: <https://manned.org/virsh>.

## Examples

### List the `virsh` commands grouped into related categories

```bash
virsh help
```

### List the command categories

```bash
virsh help | grep "keyword"
```

### List the commands in a category

```bash
virsh help category_keyword
```

### Display help for a command

```bash
virsh help command
```
