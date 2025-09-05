# mutt

> Command-line email client. More information: <http://mutt.org/doc/mutt.1.txt>.

## Examples

### Open the specified mailbox

```bash
mutt -f mailbox
```

### Send an email and specify a subject and a cc recipient

```bash
mutt -s subject -c cc@example.com recipient@example.com
```

### Send an email with files attached

```bash
mutt -a file1 file2 ... -- recipient@example.com
```

### Specify a file to include as the message body

```bash
mutt -i path/to/file recipient@example.com
```

### Specify a draft file containing the header and the body of the message, in RFC 5322 format

```bash
mutt -H path/to/file recipient@example.com
```
