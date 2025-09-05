# mixxx

> Free and open source cross-platform DJ software. See also: `lmms`. More information: <https://mixxx.org/manual/latest/chapters/appendix.html#command-line-options>.

## Examples

### Start the Mixxx GUI in fullscreen

```bash
mixxx --fullScreen
```

### Start in safe developer mode to debug a crash

```bash
mixxx --developer --safeMode
```

### Debug a malfunction

```bash
mixxx --debugAssertBreak --developer --loglevel trace
```

### Start Mixxx using the specified settings file

```bash
mixxx --resourcePath mixxx/res/controllers --settingsPath path/to/settings-file
```

### Debug a custom controller mapping

```bash
mixxx --controllerDebug --resourcePath path/to/mapping-directory
```

### Display help

```bash
mixxx --help
```
