# limactl

> Virtual machine manager for Linux guests, with multiple VM templates available. Can be used to run containers on macOS, but also for generic virtual machine use cases on macOS and Linux hosts. More information: <https://github.com/lima-vm/lima>.

## Examples

### List VMs

```bash
limactl list
```

### Create a VM using the default settings and optionally provide a name and/or a template (see `limactl create --list-templates` for available templates)

```bash
limactl create --name vm_name template://debian|fedora|ubuntu|...
```

### Start a VM (this might install some dependencies in it and take a few minutes)

```bash
limactl start vm_name
```

### Open a remote shell inside a VM

```bash
limactl shell vm_name
```

### Run a command inside a VM

```bash
limactl shell vm_name command
```

### Stop/shutdown a VM

```bash
limactl stop vm_name
```

### Delete a VM

```bash
limactl remove vm_name
```
