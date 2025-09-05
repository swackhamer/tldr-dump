# vboxmanage-export

> Export virtual machines to a virtual appliance (ISO) or a cloud service. More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-export>.

## Examples

### Specify the target OVA file

```bash
VBoxManage export --output path/to/filename.ova
```

### Export in OVF 0.9 legacy mode

```bash
VBoxManage export --legacy09
```

### Export in OVF (0.9|1.0|2.0) format

```bash
VBoxManage export --ovf09|ovf10|ovf20
```

### Create manifest of the exported files

```bash
VBoxManage export --manifest
```

### Specify a description of the VM

```bash
VBoxManage export --description "vm_description"
```
