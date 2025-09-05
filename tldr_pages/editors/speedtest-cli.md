# speedtest-cli

> Test internet bandwidth using <https://speedtest.net>. See also: `speedtest` for the official CLI. More information: <https://github.com/sivel/speedtest-cli>.

## Examples

### Run a speed test

```bash
speedtest-cli
```

### Run a speed test and display values in bytes, instead of bits

```bash
speedtest-cli --bytes
```

### Run a speed test using `HTTPS`, instead of `HTTP`

```bash
speedtest-cli --secure
```

### Run a speed test without performing download tests

```bash
speedtest-cli --no-download
```

### Run a speed test and generate an image of the results

```bash
speedtest-cli --share
```

### List all `speedtest.net` servers, sorted by distance

```bash
speedtest-cli --list
```

### Run a speed test to a specific speedtest.net server

```bash
speedtest-cli --server server_id
```

### Run a speed test and display the results as JSON (suppresses progress information)

```bash
speedtest-cli --json
```
