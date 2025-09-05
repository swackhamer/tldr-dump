# ntfy

> Send and receive HTTP POST notifications. More information: <https://github.com/binwiederhier/ntfy>.

## Examples

### Send a message to the `security` topic

```bash
ntfy pub security "Front door has been opened."
```

### Send with a title, priority and tags

```bash
ntfy publish --title="Someone bought your item" --priority=high --tags=duck ebay "Someone just bought your item: Platypus Sculpture"
```

### Send at 8:30am

```bash
ntfy pub --at=8:30am delayed_topic "Time for school, sleepyhead..."
```

### Trigger a webhook

```bash
ntfy trigger my_webhook
```

### Subscribe to a topic (`<Ctrl c>` to stop listening)

```bash
ntfy sub home_automation
```

### Display help

```bash
ntfy --help
```
