# terminal-notifier

> Send macOS User Notifications. More information: <https://github.com/julienXX/terminal-notifier>.

## Examples

### Send a notification (only the message is required)

```bash
terminal-notifier -group tldr-info -title TLDR -message 'TLDR rocks'
```

### Display piped data with a sound

```bash
echo 'Piped Message Data!' | terminal-notifier -sound default
```

### Open a URL when the notification is clicked

```bash
terminal-notifier -message 'Check your Apple stock!' -open 'http://finance.yahoo.com/q?s=AAPL'
```

### Open an app when the notification is clicked

```bash
terminal-notifier -message 'Imported 42 contacts.' -activate com.apple.AddressBook
```
