# adb-logcat

> Dump a log of system messages. More information: <https://developer.android.com/tools/logcat>.

## Examples

### Display system logs

```bash
adb logcat
```

### Display lines that match a `reg[e]x`

```bash
adb logcat -e regex
```

### Display logs for a tag in a specific mode ([V]erbose, [D]ebug, [I]nfo, [W]arning, [E]rror, [F]atal, [S]ilent), filtering other tags

```bash
adb logcat tag:mode *:S
```

### Display logs for React Native applications in [V]erbose mode [S]ilencing other tags

```bash
adb logcat ReactNative:V ReactNativeJS:V *:S
```

### Display logs for all tags with priority level [W]arning and higher

```bash
adb logcat *:W
```

### Display logs for a specific PID

```bash
adb logcat --pid pid
```

### Display logs for the process of a specific package

```bash
adb logcat --pid $(adb shell pidof -s package)
```

### Color the log (usually use with filters)

```bash
adb logcat -v color
```
