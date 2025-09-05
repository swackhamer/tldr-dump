# ffsend

> Easily and securely share files. More information: <https://gitlab.com/timvisee/ffsend>.

## Examples

### Upload a file

```bash
ffsend upload path/to/file
```

### Download a file

```bash
ffsend download url
```

### Upload a file with password

```bash
ffsend upload path/to/file [-p|--password] password
```

### Download a file protected by password

```bash
ffsend download url [-p|--password] password
```

### Upload a file and allow 4 downloads

```bash
ffsend upload path/to/file [-d|--downloads] 4
```
