# tmpmail

> A temporary email right from your terminal written in POSIX sh. More information: <https://github.com/sdushantha/tmpmail#usage>.

## Examples

### Create a temporary inbox

```bash
tmpmail [-g|--generate]
```

### List messages and their numeric ID

```bash
tmpmail
```

### Display the most recent received email

```bash
tmpmail [-r|--recent]
```

### Open a specific message

```bash
tmpmail email_id
```

### View email as raw text without HTML tags

```bash
tmpmail [-t|--text]
```

### Open email with a specific browser (default is w3m)

```bash
tmpmail [-b|--browser] browser
```
