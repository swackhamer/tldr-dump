# fswebcam

> Small and simple webcam for *nix. More information: <https://www.sanslogic.co.uk/fswebcam>.

## Examples

### Take a picture

```bash
fswebcam filename
```

### Take a picture with custom resolution

```bash
fswebcam [-r|--resolution] widthxheight filename
```

### Take a picture from selected device(Default is `/dev/video0`)

```bash
fswebcam [-d|--device] device filename
```

### Take a picture with timestamp(timestamp string is formatted by strftime)

```bash
fswebcam --timestamp timestamp filename
```
