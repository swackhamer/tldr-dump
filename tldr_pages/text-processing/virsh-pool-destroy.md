# virsh-pool-destroy

> Stop an active virtual machine storage pool. See also: `virsh`, `virsh-pool-delete`. More information: <https://manned.org/virsh>.

## Examples

### Stop a storage pool specified by name or UUID (determine using `virsh pool-list`)

```bash
virsh pool-destroy --pool name|uuid
```
