# speedtest-rs

> An unofficial Rust-based tool for testing network speeds using speedtest.net, limited to HTTP Legacy Fallback. More information: <https://github.com/nelsonjchen/speedtest-rs>.

## Examples

### Run a full speed test (download and upload)

```bash
speedtest-rs
```

### Display a list of `speedtest.net` servers sorted by distance

```bash
speedtest-rs --list
```

### Run a download test only

```bash
speedtest-rs --no-upload
```

### Run an upload test only

```bash
speedtest-rs --no-download
```

### Generate a shareable link to the test results image

```bash
speedtest-rs --share
```

### Display basic output information only

```bash
speedtest-rs --simple
```
