# sendmail

> Send email. More information: <https://manned.org/sendmail>.

## Examples

### Send a message with the content of `message.txt` to the mail directory of local user `username`

```bash
sendmail username < message.txt
```

### Send an email from you@yourdomain.com (assuming the mail server is configured for this) to test@gmail.com containing the message in `message.txt`

```bash
sendmail -f you@yourdomain.com test@gmail.com < message.txt
```

### Send an email from you@yourdomain.com (assuming the mail server is configured for this) to test@gmail.com containing the file `file.zip`

```bash
sendmail -f you@yourdomain.com test@gmail.com < file.zip
```
