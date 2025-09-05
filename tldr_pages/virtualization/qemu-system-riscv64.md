# qemu-system-riscv64

> Emulate `riscv64` architecture. More information: <https://www.qemu.org/docs/master/system/target-riscv.html>.

## Examples

### Boot a kernel emulating `riscv64` architecture

```bash
qemu-system-riscv64 [-M|-machine] virt -bios none -kernel kernel.elf -nographic
```

### List supported machine types

```bash
qemu-system-riscv64 [-M|-machine] help
```

### Exit non-graphical QEMU

```bash
<Ctrl a><x>
```
