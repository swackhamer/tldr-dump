# wacaw

> Capture both still pictures and video from an attached camera. More information: <https://webcam-tools.sourceforge.net>.

## Examples

### Take a picture from webcam

```bash
wacaw filename
```

### Record a video

```bash
wacaw --video filename --duration 10
```

### Take a picture with custom resolution

```bash
wacaw --width width --height 100 filename
```

### Copy image just taken to clipboard

```bash
wacaw --to-clipboard
```

### List the devices available

```bash
wacaw --list-devices
```
