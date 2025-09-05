# tart

> Build, run and manage macOS and Linux virtual machines (VMs) on Apple Silicon. More information: <https://github.com/cirruslabs/tart>.

## Examples

### Pull a remote VM image

```bash
tart pull acme.io/org/name:tag
```

### Clone a VM from a local or remote image source

```bash
tart clone source-vm vm-name
```

### Create a new Mac VM from a specific ipsw file

```bash
tart create --from-ipsw latest|path/to/file.ipsw vm-name
```

### Run an existing VM

```bash
tart run vm-name
```

### Run an existing VM with a specific mounted directory

```bash
tart run --dir=path/to/directory:/path/to/local_directory vm-name
```

### List VMs

```bash
tart list
```

### Get IP address of a running VM

```bash
tart ip vm-name
```

### Change a VM's display resolution

```bash
tart set vm-name --display 640x400
```
