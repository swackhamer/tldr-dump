# dcgmi

> Manage and monitor NVIDIA Data Center GPUs. More information: <https://developer.nvidia.com/dcgm>.

## Examples

### Display information on all available GPUs and processes using them

```bash
dcgmi discovery [-l|--list]
```

### List created groups

```bash
dcgmi group [-l|--list]
```

### Display current usage statistics for device 0

```bash
dcgmi dmon [-e|--field-id]1001,1002,1003,1004,1005
```

### Display help

```bash
dcgmi [-h|--help]
```

### Display help for a subcommand

```bash
dcgmi subcommand [-h|--help]
```
