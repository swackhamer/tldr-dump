# slackcat

> Utility for passing files and command output to Slack. More information: <https://github.com/bcicen/slackcat#usage>.

## Examples

### Post a file to Slack

```bash
slackcat [-c|--channel] channel_name path/to/file
```

### Post a file to Slack with a custom filename

```bash
slackcat [-c|--channel] channel_name [-n|--filename] filename path/to/file
```

### Pipe command output to Slack as a text snippet

```bash
command | slackcat [-c|--channel] channel_name [-n|--filename] snippet_name
```

### Stream command output to Slack continuously

```bash
command | slackcat [-c|--channel] channel_name [-s|--stream]
```
