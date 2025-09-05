# nhentai

> Download doujinshis from nhentai. More information: <https://github.com/RicterZ/nhentai>.

## Examples

### Set cookies

```bash
nhentai --cookie "csrftoken=TOKEN; sessionid=ID"
```

### Download a specific doujin

```bash
nhentai --id number
```

### Download the first page of your favorites

```bash
nhentai --favorites --download --delay 1
```

### Download specific pages of your favorites

```bash
nhentai --favorites --pages start_page-end_page --download --delay 1
```
