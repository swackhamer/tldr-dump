# vboxmanage-createvm

> Create a new virtual machine. More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-createvm>.

## Examples

### Create a new VM with default settings

```bash
VBoxManage createvm --name vm_name
```

### Set the base folder where the VM configuration will be stored

```bash
VBoxManage createvm --name vm_name --basefolder path/to/directory
```

### Set the guest OS type (one of `VBoxManage list ostypes`) for the imported VM

```bash
VBoxManage createvm --name vm_name --ostype ostype
```

### Register the created VM in VirtualBox

```bash
VBoxManage createvm --name vm_name --register
```

### Set the VM to the specified groups

```bash
VBoxManage createvm --name vm_name --group group1,group2,...
```

### Set the Universally Unique Identifier (UUID) of the VM

```bash
VBoxManage createvm --name vm_name --uuid uuid
```

### Set the cipher to use for encryption

```bash
VBoxManage createvm --name vm_name --cipher AES-128|AES-256
```
