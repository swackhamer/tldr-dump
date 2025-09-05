# theharvester

> A tool designed to be used in the early stages of a penetration test. More information: <https://github.com/laramies/theHarvester>.

## Examples

### Gather information on a domain using Google

```bash
theHarvester --domain domain_name --source google
```

### Gather information on a domain using multiple sources

```bash
theHarvester --domain domain_name --source duckduckgo,bing,crtsh
```

### Change the limit of results to work with

```bash
theHarvester --domain domain_name --source google --limit 200
```

### Save the output to two files in XML and HTML format

```bash
theHarvester --domain domain_name --source google --file output_file_name
```

### Display help

```bash
theHarvester --help
```
