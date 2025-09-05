# fastboot

> Communicate with connected Android devices when in bootloader mode (the one place ADB doesn't work). More information: <https://cs.android.com/android/platform/superproject/+/main:system/core/fastboot>.

## Examples

### Unlock the bootloader

```bash
fastboot oem unlock
```

### Relock the bootloader

```bash
fastboot oem lock
```

### Reboot the device from fastboot mode into fastboot mode again

```bash
fastboot reboot bootloader
```

### Flash a given image

```bash
fastboot flash path/to/file.img
```

### Flash a custom recovery image

```bash
fastboot flash recovery path/to/file.img
```

### List connected devices

```bash
fastboot devices
```

### Display all information of a device

```bash
fastboot getvar all
```
