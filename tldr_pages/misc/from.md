# from

> Print mail header lines from the current user's mailbox. More information: <https://mailutils.org/manual/html_chapter/Programs.html#frm-and-from>.

## Examples

### List mail

```bash
from
```

### Display the number of messages stored

```bash
from --count
```

### List mail in the specified mailbox directory

```bash
MAIL=path/to/mailbox from
```

### Print the mail from the specified address

```bash
from --sender=me@example.com
```
