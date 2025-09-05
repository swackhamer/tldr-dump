# qemu-system-i386

> Emulate the `i386` architecture. More information: <https://www.qemu.org/docs/master/system/target-i386.html>.

## Examples

### Boot from an image emulating the `i386` architecture

```bash
qemu-system-i386 -hda image_name.img -m 4096
```

### Boot a QEMU instance from a live ISO image

```bash
qemu-system-i386 -hda image_name.img -cdrom os_image.iso -boot d -m 4096
```

### Boot from a physical device (e.g. from USB to test a bootable medium)

```bash
qemu-system-i386 -hda /dev/storage_device -m 4096
```

### Do not launch a VNC server

```bash
qemu-system-i386 -hda image_name.img -m 4096 -nographic
```

### Exit non-graphical QEMU

```bash
<Ctrl a><x>
```

### List the supported machine types

```bash
qemu-system-i386 [-M|-machine] help
```
