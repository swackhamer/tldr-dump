# getarch.py

> Determine the OS architecture (x86 or x64) of a remote Windows system. Part of the Impacket suite. More information: <https://github.com/fortra/impacket>.

## Examples

### Check the architecture of a single target system

```bash
getArch.py -target target
```

### Check the architecture of multiple targets from a file (one per line)

```bash
getArch.py -targets path/to/targets_file
```

### Set a custom socket timeout (default is 2 seconds)

```bash
getArch.py -target target -timeout seconds
```

### Enable debug mode for detailed output

```bash
getArch.py -target target -debug
```
