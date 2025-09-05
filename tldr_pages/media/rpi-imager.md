# rpi-imager

> Flash images onto storage devices. More information: <https://github.com/raspberrypi/rpi-imager>.

## Examples

### Write a specific image to a specific block device

```bash
rpi-imager --cli path/to/image.zip /dev/sdX
```

### Write a specific image to a block device, disabling the checksum verification

```bash
rpi-imager --cli --disable-verify path/to/image.zip /dev/sdX
```

### Write a specific image to a block device, which will expect a specific checksum when running the verification

```bash
rpi-imager --cli --sha256 expected_hash path/to/image.zip /dev/sdX
```
