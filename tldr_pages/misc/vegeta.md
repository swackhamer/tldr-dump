# vegeta

> A utility and a library for HTTP load testing. See also: `ab`. More information: <https://github.com/tsenart/vegeta>.

## Examples

### Launch an attack lasting 30 seconds

```bash
echo "GET https://example.com" | vegeta attack -duration=30s
```

### Launch an attack on a server with a self-signed HTTPS certificate

```bash
echo "GET https://example.com" | vegeta attack -insecure -duration=30s
```

### Launch an attack with a rate of 10 requests per second

```bash
echo "GET https://example.com" | vegeta attack -duration=30s -rate=10
```

### Launch an attack and display a report

```bash
echo "GET https://example.com" | vegeta attack -duration=30s | vegeta report
```

### Launch an attack and plot the results on a graph (latency over time)

```bash
echo "GET https://example.com" | vegeta attack -duration=30s | vegeta plot > path/to/results.html
```

### Launch an attack against multiple URLs from a file

```bash
vegeta attack -duration=30s -targets=requests.txt | vegeta report
```
