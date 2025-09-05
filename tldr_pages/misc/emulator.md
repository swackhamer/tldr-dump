# emulator

> Manage Android emulators. More information: <https://developer.android.com/studio/run/emulator-commandline>.

## Examples

### Start an Android emulator device

```bash
emulator -avd name
```

### Display the webcams on your development computer that are available for emulation

```bash
emulator -avd name -webcam-list
```

### Start an emulator overriding the facing back camera setting (use `-camera-front` for front camera)

```bash
emulator -avd name -camera-back none|emulated|webcamN
```

### Start an emulator, with a maximum network speed

```bash
emulator -avd name -netspeed gsm|hscsd|gprs|edge|hsdpa|lte|evdo|full
```

### Start an emulator with network latency

```bash
emulator -avd name -netdelay gsm|hscsd|gprs|edge|hsdpa|lte|evdo|none
```

### Start an emulator, making all TCP connections through a specified HTTP/HTTPS proxy (port number is required)

```bash
emulator -avd name -http-proxy http://example.com:80
```

### Start an emulator with a given SD card partition image file

```bash
emulator -avd name -sdcard path/to/sdcard.img
```

### Display help

```bash
emulator -help
```
