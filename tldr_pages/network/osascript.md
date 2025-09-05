# osascript

> Run AppleScript or JavaScript for Automation (JXA). More information: <https://keith.github.io/xcode-man-pages/osascript.1.html>.

## Examples

### Run an AppleScript command

```bash
osascript -e 'say "Hello world"'
```

### Run multiple AppleScript commands

```bash
osascript -e 'say "Hello"' -e 'say "world"'
```

### Run a compiled (`*.scpt`), bundled (`*.scptd`), or plaintext (`*.applescript`) AppleScript file

```bash
osascript path/to/apple.scpt
```

### Get the bundle identifier of an application (useful for `open -b`)

```bash
osascript -e 'id of app "Application"'
```

### Run a JavaScript command

```bash
osascript -l JavaScript -e "console.log('Hello world');"
```

### Run a JavaScript file

```bash
osascript -l JavaScript path/to/script.js
```
