# idevicecrashreport

> Retrieve crash reports from an iOS device. More information: <https://manned.org/idevicecrashreport>.

## Examples

### Retrieve crash reports and move them to a specified directory

```bash
idevicecrashreport path/to/directory
```

### Retrieve crash reports without removing them from the device

```bash
idevicecrashreport --keep path/to/directory
```

### Extract crash reports into separate `.crash` files

```bash
idevicecrashreport --extract path/to/directory
```
