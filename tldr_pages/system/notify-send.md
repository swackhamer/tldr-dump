# notify-send

> Use the current desktop environment's notification system to create a notification. More information: <https://manned.org/notify-send>.

## Examples

### Show a notification with the title "Test" and the content "This is a test"

```bash
notify-send "Test" "This is a test"
```

### Show a notification with a custom icon

```bash
notify-send [-i|--icon] icon.png "Test" "This is a test"
```

### Show a notification for 5 seconds

```bash
notify-send [-t|--expire-time] 5000 "Test" "This is a test"
```

### Show a notification with the specified urgency level (default: normal)

```bash
notify-send [-u|--urgency] low|normal|critical "Test" "This is a test"
```

### Show a notification with an app's icon and name

```bash
notify-send "Test" [-i|--icon] google-chrome [-a|--app-name] "Google Chrome"
```
