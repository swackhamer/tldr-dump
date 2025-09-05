# icalbuddy

> Command-line utility for printing events and tasks from the macOS calendar database. More information: <https://hasseg.org/icalBuddy/>.

## Examples

### Show events later today

```bash
icalBuddy --includeOnlyEventsFromNowOn eventsToday
```

### Show uncompleted tasks

```bash
icalBuddy uncompletedTasks
```

### Show a formatted list separated by calendar for all events today

```bash
icalBuddy --formatOutput --separateByCalendar eventsToday
```

### Show tasks for a specified number of days

```bash
icalBuddy --includeOnlyEventsFromNowOn "tasksDueBefore:today+number_of_days"
```

### Show events in a time range

```bash
icalBuddy eventsFrom:start_date to:end_date
```
