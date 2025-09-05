# smartctl

> Monitor disk health including SMART data. More information: <https://manned.org/smartctl>.

## Examples

### Display SMART health summary

```bash
sudo smartctl [-H|--health] /dev/sdX
```

### Display device information

```bash
sudo smartctl [-i|--info] /dev/sdX
```

### Start a short/long self-test in the background

```bash
sudo smartctl [-t|--test] short|long /dev/sdX
```

### Display the self-test log

```bash
sudo smartctl [-l|--log] selftest
```

### Display current/last self-test status and other SMART capabilities

```bash
sudo smartctl [-c|--capabilities] /dev/sdX
```

### Display exhaustive SMART data

```bash
sudo smartctl [-a|--all] /dev/sdX
```
