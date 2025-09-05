# pnpm-audit

> Scan project dependencies. Check for known security issues with the installed packages. More information: <https://pnpm.io/cli/audit>.

## Examples

### Identify vulnerabilities in the project

```bash
pnpm audit
```

### Automatically fix vulnerabilities

```bash
pnpm audit fix
```

### Generate a security report in JSON format

```bash
pnpm audit --json > path/to/audit-report.json
```

### Audit only dev dependencies

```bash
pnpm audit [-D|--dev]
```

### Audit only production dependencies

```bash
pnpm audit [-P|--prod]
```

### Exclude optional dependencies from the audit

```bash
pnpm audit --no-optional
```

### Ignore registry errors during the audit process

```bash
pnpm audit --ignore-registry-errors
```

### Filter advisories by severity (low, moderate, high, critical)

```bash
pnpm audit --audit-level severity
```
