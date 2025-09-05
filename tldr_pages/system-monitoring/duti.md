# duti

> Set default applications for document types and URL schemes on macOS. More information: <https://github.com/moretension/duti>.

## Examples

### Set Safari as the default handler for HTML documents

```bash
duti -s com.apple.Safari public.html all
```

### Set VLC as the default viewer for files with `.m4v` extensions

```bash
duti -s org.videolan.vlc m4v viewer
```

### Set Finder as the default handler for the ftp:// URL scheme

```bash
duti -s com.apple.Finder "ftp"
```

### Display information about the default application for a given extension

```bash
duti -x ext
```

### Display the default handler for a given UTI

```bash
duti -d uti
```

### Display all handlers of a given UTI

```bash
duti -l uti
```
