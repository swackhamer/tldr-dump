# timew

> A time tracking tool used to measure the duration of activities. More information: <https://timewarrior.net/docs>.

## Examples

### Start tracking an activity

```bash
timew start
```

### Tag the current activity

```bash
timew tag activity_tag
```

### Start tracking and tag a new activity

```bash
timew start activity_tag
```

### Stop the current activity

```bash
timew stop
```

### Track an activity in the past

```bash
timew track start_time - end_time activity_tag
```

### View tracked items of the day

```bash
timew summary
```

### View report for the last day, week, current month, etc.

```bash
timew summary :today|yesterday|week|lastweek|month|lastmonth|year|lastyear
```
