# vt

> Interface for VirusTotal. API key from a VirusTotal account is required for this command. More information: <https://github.com/VirusTotal/vt-cli>.

## Examples

### Scan a specific file for viruses

```bash
vt scan file path/to/file
```

### Scan a URL for viruses

```bash
vt scan url url
```

### Display information from a specific analysis

```bash
vt analysis file_id|analysis_id
```

### Download files in encrypted Zip format (requires premium account)

```bash
vt download file_id --output path/to/directory --zip --zip-password password
```

### Initialize or re-initialize `vt` to enter API key interactively

```bash
vt init
```

### Display information about a domain

```bash
vt domain url
```

### Display information for a specific URL

```bash
vt url url
```

### Display information for a specific IP address

```bash
vt domain ip_address
```
