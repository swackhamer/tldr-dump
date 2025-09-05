# vboxmanage-unregistervm

> Unregister a virtual machine (VM). More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-unregistervm>.

## Examples

### Unregister an existing VM

```bash
VBoxManage unregistervm uuid|vm_name
```

### Delete hard disk image files, all saved state files, VM logs, and XML VM machine files

```bash
VBoxManage unregistervm uuid|vm_name --delete
```

### Delete all files from the VM

```bash
VBoxManage unregistervm uuid|vm_name --delete-all
```
