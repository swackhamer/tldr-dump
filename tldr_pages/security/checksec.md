# checksec

> Check security properties of executables. More information: <https://github.com/slimm609/checksec.sh>.

## Examples

### List security properties of an executable binary file

```bash
checksec --file=path/to/binary
```

### List security properties recursively of all executable files in a directory

```bash
checksec --dir=path/to/directory
```

### List security properties of a process

```bash
checksec --proc=pid
```

### List security properties of the running kernel

```bash
checksec --kernel
```
