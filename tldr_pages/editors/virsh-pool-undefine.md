# virsh-pool-undefine

> Delete the configuration file in `/etc/libvirt/storage` for a stopped virtual machine storage pool. See also: `virsh`, `virsh-pool-destroy`. More information: <https://manned.org/virsh>.

## Examples

### Delete the configuration for the storage pool specified name or UUID (determine using `virsh pool-list`)

```bash
virsh pool-undefine --pool name|uuid
```
