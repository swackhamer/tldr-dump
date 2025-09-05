# man

> Format and display manual pages. More information: <https://manned.org/man>.

## Examples

### Display the man page for a command

```bash
man command
```

### Open the man page for a command in a browser (`BROWSER` environment variable can replace `=browser_name`)

```bash
man [-Hbrowser_name|--html=browser_name] command
```

### Display the man page for a command from section 7

```bash
man 7 command
```

### List all available sections for a command

```bash
man [-f|--whatis] command
```

### Display the path searched for manpages

```bash
man [-w|--path]
```

### Display the location of a manpage rather than the manpage itself

```bash
man [-w|--where] command
```

### Display the man page using a specific locale

```bash
man [-L|--locale] locale command
```

### Search for manpages containing a search string

```bash
man [-k|--apropos] "search_string"
```
