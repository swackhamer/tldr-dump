# vboxmanage-showvminfo

> Show information about registered virtual machine. More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-showvminfo>.

## Examples

### Show information about a particular virtual machine

```bash
VBoxManage showvminfo vm_name|uuid
```

### Show more detailed information about a particular virtual machine

```bash
VBoxManage showvminfo --details vm_name|uuid
```

### Show information in a machine readable format

```bash
VBoxManage showvminfo --machinereadable vm_name|uuid
```

### Specify password ID if the virtual machine is encrypted

```bash
VBoxManage showvminfo --password-id password_id vm_name|uuid
```

### Specify the password file if the virtual machine is encrypted

```bash
VBoxManage showvminfo --password path/to/password_file vm_name|uuid
```

### Show the logs of a specific virtual machine

```bash
VBoxManage showvminfo --log vm_name|uuid
```
