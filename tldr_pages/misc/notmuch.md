# notmuch

> Index, search, read, and tag large collections of email messages. More information: <https://notmuchmail.org/manpages/>.

## Examples

### Configure for first use

```bash
notmuch setup
```

### Add a tag for all messages matching a search term

```bash
notmuch tag +custom_tag "search_term"
```

### Remove a tag for all messages matching a search term

```bash
notmuch tag -custom_tag "search_term"
```

### Count messages matching the given search term

```bash
notmuch count --output=messages|threads "search_term"
```

### Search for messages matching the given search term

```bash
notmuch search --format=json|text --output=summary|threads|messages|files|tags "search_term"
```

### Limit the number of search results to X

```bash
notmuch search --format=json|text --output=summary|threads|messages|files|tags --limit=X "search_term"
```

### Create a reply template for a set of messages

```bash
notmuch reply --format=default|headers-only --reply-to=sender|all "search_term"
```
