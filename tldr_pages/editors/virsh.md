# virsh

> Manage `virsh` guest domains. (Note: `guest_id` can be the ID, name or UUID of the guest). Some subcommands such as `list` have their own usage documentation. More information: <https://libvirt.org/manpages/virsh.html>.

## Examples

### Connect to a hypervisor session

```bash
virsh connect qemu:///system
```

### Activate a network named `default`

```bash
sudo virsh net-start default
```

### List all domains

```bash
virsh list --all
```

### Create a guest from a configuration file

```bash
virsh create path/to/config_file.xml
```

### Edit a guest's configuration file (editor can be changed with $EDITOR)

```bash
virsh edit guest_id
```

### Start/reboot/shutdown/suspend/resume a guest

```bash
virsh command guest_id
```

### Save the current state of a guest to a file

```bash
virsh save guest_id filename
```

### Delete a running guest

```bash
virsh destroy guest_id && virsh undefine guest_id
```
