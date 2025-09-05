# transmission-edit

> Modify announce URLs from torrent files. See also: `transmission`. More information: <https://manned.org/transmission-edit>.

## Examples

### Add a URL to a torrent's announce list

```bash
transmission-edit [-a|--add] http://example.com path/to/file.torrent
```

### Remove a URL from a torrent's announce list

```bash
transmission-edit [-d|--delete] http://example.com path/to/file.torrent
```

### Update a tracker's passcode in a torrent file

```bash
transmission-edit [-r|--replace] old-passcode new-passcode path/to/file.torrent
```
