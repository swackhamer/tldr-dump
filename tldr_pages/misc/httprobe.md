# httprobe

> Take a list of domains and probe for working HTTP and HTTPS servers. More information: <https://github.com/tomnomnom/httprobe>.

## Examples

### Probe a list of domains from a text file

```bash
cat input_file | httprobe
```

### Only check for HTTP if HTTPS is not working

```bash
cat input_file | httprobe --prefer-https
```

### Probe additional ports with a given protocol

```bash
cat input_file | httprobe -p https:2222
```

### Display help

```bash
httprobe --help
```
