# f3fix

> Edit the partition table of a fake flash drive. See also: `f3probe`, `f3write`, `f3read`. More information: <https://oss.digirati.com.br/f3/>.

## Examples

### Fill a fake flash drive with a single partition that matches its real capacity

```bash
sudo f3fix /dev/device_name
```

### Mark the partition as bootable

```bash
sudo f3fix --boot /dev/device_name
```

### Specify the filesystem

```bash
sudo f3fix --fs-type=filesystem_type /dev/device_name
```
