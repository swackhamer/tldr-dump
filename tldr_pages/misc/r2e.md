# r2e

> Forwards RSS feeds to an email address. Requires a configured `sendmail` or smtp setup. More information: <https://manned.org/r2e>.

## Examples

### Create a new feed database that sends email to an email address

```bash
r2e new email_address
```

### Subscribe to a feed

```bash
r2e add feed_name feed_URI
```

### Send new stories to an email address

```bash
r2e run
```

### List all feeds

```bash
r2e list
```

### Delete a feed at a specified index

```bash
r2e delete index
```

### Display help

```bash
r2e [-h|--help]
```
