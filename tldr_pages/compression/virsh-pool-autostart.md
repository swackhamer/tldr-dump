# virsh-pool-autostart

> Enable or disable autostart for a virtual machine storage pool. See also: `virsh`. More information: <https://manned.org/virsh>.

## Examples

### Enable autostart for the storage pool specified by name or UUID (determine using `virsh pool-list`)

```bash
virsh pool-autostart --pool name|uuid
```

### Disable autostart for the storage pool specified by name or UUID

```bash
virsh pool-autostart --pool name|uuid --disable
```
