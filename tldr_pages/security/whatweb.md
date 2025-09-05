# whatweb

> Next-generation web scanner. More information: <https://morningstarsecurity.com/research/whatweb>.

## Examples

### Scan websites/targets for web technologies

```bash
whatweb website1 website2 ...
```

### Read targets/websites from a file

```bash
whatweb [-i|--input-file] targets_file
```

### Scan a website/target in verbose mode

```bash
whatweb [-v|--verbose] example.com
```

### Run an aggressive scan on a website

```bash
whatweb [-a|--aggression] 3 example.com
```

### Scan a network and suppress errors

```bash
whatweb --no-errors 192.168.0.0/24
```

### List plugins

```bash
whatweb [-l|--list-plugins]
```

### List plugin details

```bash
whatweb [-I|--info-plugins] plugin_name
```
