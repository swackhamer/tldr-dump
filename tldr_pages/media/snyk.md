# snyk

> Find vulnerabilities in your code and remediate risks. More information: <https://docs.snyk.io/snyk-cli/commands>.

## Examples

### Log in to your Snyk account

```bash
snyk auth
```

### Test your code for any known vulnerabilities

```bash
snyk test
```

### Test a local Docker image for any known vulnerabilities

```bash
snyk test --docker docker_image
```

### Record the state of dependencies and any vulnerabilities on snyk.io

```bash
snyk monitor
```

### Auto patch and ignore vulnerabilities

```bash
snyk wizard
```
