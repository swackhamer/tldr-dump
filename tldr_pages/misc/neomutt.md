# neomutt

> NeoMutt email client. More information: <https://neomutt.org/guide/reference.html>.

## Examples

### Open the specified mailbox

```bash
neomutt -f path/to/mailbox
```

### Start writing an email and specify a subject and a `cc` recipient

```bash
neomutt -s "subject" -c cc@example.com recipient@example.com
```

### Send an email with files attached

```bash
neomutt -a path/to/file1 path/to/file2 ... -- recipient@example.com
```

### Specify a file to include as the message body

```bash
neomutt -i path/to/file recipient@example.com
```

### Specify a draft file containing the header and the body of the message, in RFC 5322 format

```bash
neomutt -H path/to/file recipient@example.com
```
