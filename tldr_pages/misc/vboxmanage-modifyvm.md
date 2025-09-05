# vboxmanage-modifyvm

> Change settings for a virtual machine that is stopped. More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-modifyvm>.

## Examples

### Rename the VM

```bash
VBoxManage modifyvm uuid|vm_name --name new_name
```

### Adjust memory and CPU

```bash
VBoxManage modifyvm uuid|vm_name --memory 2048 --cpus 2
```

### Enable Remote Display (VRDE)

```bash
VBoxManage modifyvm uuid|vm_name --vrde on
```

### Enable session recording

```bash
VBoxManage modifyvm uuid|vm_name --recording on
```
