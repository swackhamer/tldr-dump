# checkov

> Checkov is a static code analysis tool for Infrastructure as Code (IaC). It is also a software composition analysis (SCA) tool for images and open source packages. More information: <https://www.checkov.io/1.Welcome/Quick%20Start.html>.

## Examples

### Scan a directory containing IaC (Terraform, Cloudformation, ARM, Ansible, Bicep, Dockerfile, etc)

```bash
checkov --directory path/to/directory
```

### Scan an IaC file, omitting code blocks in the output

```bash
checkov --compact --file path/to/file
```

### List all checks for all IaC types

```bash
checkov --list
```
