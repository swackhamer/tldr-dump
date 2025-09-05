# virsh-list

> List the ID, name, and state of virtual machines. See also: `virsh`. More information: <https://manned.org/virsh>.

## Examples

### List information about running virtual machines

```bash
virsh list
```

### List information about virtual machines regardless of state

```bash
virsh list --all
```

### List information about virtual machines with autostart either enabled or disabled

```bash
virsh list --all --autostart|no-autostart
```

### List information about virtual machines either with or without snapshots

```bash
virsh list --all --with-snapshot|without-snapshot
```
