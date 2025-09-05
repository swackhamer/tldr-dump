# par2

> File verification and repair using PAR 2.0 compatible parity archives (.par2 files). More information: <https://github.com/Parchive/par2cmdline/>.

## Examples

### Create a parity archive with a set percentage level of redundancy

```bash
par2 create -r1..100 -- path/to/file
```

### Create a parity archive with a chosen number of volume files (in addition to the index file)

```bash
par2 create -n1..32768 -- path/to/file
```

### Verify a file with a parity archive

```bash
par2 verify -- path/to/file.par2
```

### Repair a file with a parity archive

```bash
par2 repair -- path/to/file.par2
```
