# orb

> Interface for OrbStack, a fast and lightweight container and virtual machine runtime for macOS. Provides Docker-compatible commands and Linux VM management. More information: <https://docs.orbstack.dev/>.

## Examples

### List all containers and VMs

```bash
orb list
```

### Create and start a Linux virtual machine

```bash
orb create vm_name
```

### Create a VM with a specific Linux distribution

```bash
orb create vm_name ubuntu|fedora|arch|debian
```

### Start or stop a virtual machine

```bash
orb start|stop vm_name
```

### Connect to a VM via SSH

```bash
orb ssh vm_name
```

### Execute a command in a VM

```bash
orb exec vm_name command
```

### Delete a virtual machine

```bash
orb delete vm_name
```

### Show system status and resource usage

```bash
orb status
```
