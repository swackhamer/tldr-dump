# vboxmanage-clonevm

> Create a clone of an existing virtual machine (VM). More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-clonevm>.

## Examples

### Clone the specified VM

```bash
VBoxManage clonevm vm_name
```

### Specify a new name for the new VM

```bash
VBoxManage clonevm vm_name --name new_vm_name
```

### Indicate the folder where the new VM configuration is saved

```bash
VBoxManage clonevm vm_name --basefolder path/to/directory
```

### Register the cloned VM in VirtualBox

```bash
VBoxManage clonevm vm_name --register
```
