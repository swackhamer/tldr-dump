# vboxmanage-import

> Import a previously exported virtual machine (VM). More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-import>.

## Examples

### Import a VM from an OVF or OVA file

```bash
VBoxManage import path/to/file.ovf
```

### Set the name of the imported VM

```bash
VBoxManage import path/to/file.ovf --name vm_name
```

### Indicate the folder where the configuration of the imported VM will be stored

```bash
VBoxManage import path/to/file.ovf --basefolder path/to/directory
```

### Register the imported VM in VirtualBox

```bash
VBoxManage import path/to/file.ovf --register
```

### Perform a dry run to check the import without actually importing

```bash
VBoxManage import path/to/file.ovf --dry-run
```

### Set the guest OS type (one of `VBoxManage list ostypes`) for the imported VM

```bash
VBoxManage import path/to/file.ovf --ostype=ostype
```

### Set the memory (in megabytes) for the imported VM

```bash
VBoxManage import path/to/file.ovf --memory=1
```

### Set the number of CPUs for the imported VM

```bash
VBoxManage import path/to/file.ovf --cpus=1
```
