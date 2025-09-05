# gyb

> Locally back up Gmail messages using Gmail's API over HTTPS. More information: <https://github.com/GAM-team/got-your-back>.

## Examples

### Estimate the number and the size of all emails on your Gmail account

```bash
gyb --email email@gmail.com --action estimate
```

### Backup a Gmail account to a specific directory

```bash
gyb --email email@gmail.com --action backup --local-folder path/to/directory
```

### Backup only important or starred emails from a Gmail account to the default local folder

```bash
gyb --email email@gmail.com --search "is:important OR is:starred"
```

### Restore from a local folder to a Gmail account

```bash
gyb --email email@gmail.com --action restore --local-folder path/to/directory
```
