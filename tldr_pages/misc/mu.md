# mu

> Index and search emails from a local Maildir. More information: <https://man.cx/mu>.

## Examples

### Initialize the email database, optionally specifying the Maildir directory and email addresses

```bash
mu init --maildir=path/to/directory --my-address=name@example.com
```

### Index new emails

```bash
mu index
```

### Find messages using a specific keyword (in message body, subject, sender, ...)

```bash
mu find keyword
```

### Find messages to Alice with subject `jellyfish` containing the words `apples` or `oranges`

```bash
mu find to:alice subject:jellyfish apples OR oranges
```

### Find unread messages about words starting with `soc` (the `*` only works at the end of the search term) in the Sent Items folder

```bash
mu find 'subject:soc*' flag:unread maildir:'/Sent Items'
```

### Find messages from Sam with attached images, between 2 KiB and 2 MiB, written in 2021

```bash
mu find 'mime:image/* size:2k..2m date:20210101..20211231 from:sam
```

### List contacts with `Bob` in either name or email address

```bash
mu cfind Bob
```
