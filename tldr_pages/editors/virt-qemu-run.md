# virt-qemu-run

> Experimental tool to run a QEMU Guest VM independent of `libvirtd`. More information: <https://libvirt.org/manpages/virt-qemu-run.html>.

## Examples

### Run a QEMU virtual machine

```bash
virt-qemu-run path/to/guest.xml
```

### Run a QEMU virtual machine and store the state in a specific directory

```bash
virt-qemu-run [-r|--root] path/to/directory path/to/guest.xml
```

### Run a QEMU virtual machine and display verbose information about the startup

```bash
virt-qemu-run [-v|--verbose] path/to/guest.xml
```

### Display help

```bash
virt-qemu-run [-h|--help]
```
