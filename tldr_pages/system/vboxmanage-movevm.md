# vboxmanage-movevm

> Move a virtual machine (VM) to a new location on the host system. More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-movevm>.

## Examples

### Move the specified virtual machine to the current location

```bash
VBoxManage movevm vm_name
```

### Specify the new location (full or relative pathname) of the virtual machine

```bash
VBoxManage movevm vm_name --folder path/to/new_location
```
