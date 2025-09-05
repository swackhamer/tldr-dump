# php-cs-fixer

> Automatic coding style fixer for PHP. More information: <https://github.com/FriendsOfPHP/PHP-CS-Fixer>.

## Examples

### Execute code style fixing in the current directory

```bash
php-cs-fixer fix
```

### Execute code style fixing for a specific directory

```bash
php-cs-fixer fix path/to/directory
```

### Execute code style linting without applying changes

```bash
php-cs-fixer fix --dry-run
```

### Execute code style fixes using specific rules

```bash
php-cs-fixer fix --rules=rules
```

### Display the rules that have been applied

```bash
php-cs-fixer fix --verbose
```

### Output the results in a different format

```bash
php-cs-fixer fix --format=txt|json|xml|checkstyle|junit|gitlab
```

### Display files that require fixing

```bash
php-cs-fixer list-files
```

### Describe a rule or ruleset

```bash
php-cs-fixer describe rule
```
