# npm-audit

> Scan for known vulnerabilities in project dependencies. Reports vulnerabilities and suggests remediation. More information: <https://docs.npmjs.com/cli/npm-audit>.

## Examples

### Scan the project's dependencies for known vulnerabilities

```bash
npm audit
```

### Automatically fix vulnerabilities in the project's dependencies

```bash
npm audit fix
```

### Force an automatic fix to dependencies with vulnerabilities

```bash
npm audit fix [-f|--force]
```

### Update the lock file without modifying the `node_modules` directory

```bash
npm audit fix --package-lock-only
```

### Perform a dry run. Simulate the fix process without making any changes

```bash
npm audit fix --dry-run
```

### Output audit results in JSON format

```bash
npm audit --json
```

### Configure the audit to only fail on vulnerabilities above a specified severity

```bash
npm audit --audit-level info|low|moderate|high|critical
```
