# screencapture

> Utility to take screenshots and screen recordings. More information: <https://keith.github.io/xcode-man-pages/screencapture.1.html>.

## Examples

### Take a screenshot and save it to a file

```bash
screencapture path/to/file.png
```

### Take a screenshot including the mouse cursor

```bash
screencapture -C path/to/file.png
```

### Take a screenshot and open it in Preview, instead of saving

```bash
screencapture -P
```

### Take a screenshot of a selected rectangular area

```bash
screencapture -i path/to/file.png
```

### Take a screenshot after a delay

```bash
screencapture -T seconds path/to/file.png
```

### Make a screen recording and save it to a file

```bash
screencapture -v path/to/file.mp4
```
