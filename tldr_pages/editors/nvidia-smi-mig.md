# nvidia-smi-mig

> Manage Nvidia multi-instance GPUs. More information: <https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html>.

## Examples

### Create a compute instance from device 0

```bash
nvidia-smi mig [-cgi|--create-gpu-instance] 0 [-C|--default-compute-instance]
```

### List GPU instances

```bash
nvidia-smi mig [-lgi|--list-gpu-instances]
```

### Display help

```bash
nvidia-smi mig [-h|--help]
```
