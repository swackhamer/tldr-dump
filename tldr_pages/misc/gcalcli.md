# gcalcli

> Interact with Google Calendar. Requests Google API authorization upon first launch. More information: <https://github.com/insanum/gcalcli>.

## Examples

### List your events for all your calendars over the next 7 days

```bash
gcalcli agenda
```

### Show events starting from or between specific dates (also takes relative dates e.g. "tomorrow")

```bash
gcalcli agenda mm/dd [mm/dd]
```

### List events from a specific calendar

```bash
gcalcli --calendar calendar_name agenda
```

### Display an ASCII calendar of events by week

```bash
gcalcli calw
```

### Display an ASCII calendar of events for a month

```bash
gcalcli calm
```

### Quick-add an event to your calendar

```bash
gcalcli --calendar calendar_name quick "mm/dd HH:MM event_name"
```

### Add an event to calendar. Triggers interactive prompt

```bash
gcalcli --calendar "calendar_name" add
```
