# loadtest

> Run a load test on the selected HTTP or WebSockets URL. More information: <https://github.com/alexfernandez/loadtest>.

## Examples

### Run with concurrent users and a specified amount of requests per second

```bash
loadtest [-c|--concurrency] 10 [--rps|--requestsPerSecond] 200 https://example.com
```

### Run with a custom HTTP header

```bash
loadtest --headers "accept:text/plain;text-html" https://example.com
```

### Run with a specific HTTP method

```bash
loadtest [-m|--method] GET https://example.com
```
