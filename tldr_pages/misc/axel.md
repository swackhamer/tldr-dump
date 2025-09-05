# axel

> Download accelerator. Supports HTTP, HTTPS, and FTP. More information: <https://manned.org/axel>.

## Examples

### Download a URL to a file

```bash
axel url
```

### Download and specify an output file

```bash
axel url [-o|--output] path/to/file
```

### Download with a specific number connections

```bash
axel [-n|--num-connections] connections_num url
```

### Search for mirrors

```bash
axel [-S|--search] mirrors_num url
```

### Limit download speed (bytes per second)

```bash
axel [-s|--max-speed] speed url
```
