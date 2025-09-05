# composer-audit

> Analyze a PHP project's dependencies to detect known security vulnerabilities and list affected packages. See also: `composer`. More information: <https://getcomposer.org/doc/03-cli.md#audit>.

## Examples

### Check for security vulnerabilities in your current project

```bash
composer audit
```

### Omit dev dependencies in the audit

```bash
composer audit --no-dev
```

### Filter vulnerabilities by output format

```bash
composer audit --format table|plain|json|summary
```

### Output audit results to a file in JSON format

```bash
composer audit --format json > audit_report.json
```

### Verify whether a specific package in your project is affected by security issues

```bash
composer audit vendor/package
```
