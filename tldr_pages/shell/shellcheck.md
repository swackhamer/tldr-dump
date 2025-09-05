# shellcheck

> Statically check shell scripts for errors, usage of deprecated/insecure features, and bad practices. More information: <https://github.com/koalaman/shellcheck/wiki>.

## Examples

### Check a shell script

```bash
shellcheck path/to/script.sh
```

### Check a shell script interpreting it as the specified shell dialect (overrides the shebang at the top of the script)

```bash
shellcheck [-s|--shell] sh|bash|dash|ksh path/to/script.sh
```

### Ignore one or more error types

```bash
shellcheck [-e|--exclude] SC1009,SC1073,... path/to/script.sh
```

### Also check any sourced shell scripts

```bash
shellcheck [-a|--check-sourced] path/to/script.sh
```

### Display output in the specified format (defaults to `tty`)

```bash
shellcheck [-f|--format] tty|checkstyle|diff|gcc|json|json1|quiet path/to/script.sh
```

### Enable one or more [o]ptional checks

```bash
shellcheck [-o|--enable] add-default-case,avoid-nullary-conditions,... path/to/script.sh
```

### List all available optional checks that are disabled by default

```bash
shellcheck --list-optional
```

### Adjust the level of severity to consider (defaults to `style`)

```bash
shellcheck [-S|--severity] error|warning|info|style path/to/script.sh
```
