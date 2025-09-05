# wget

> Download files from the Web. Supports HTTP, HTTPS, and FTP. More information: <https://www.gnu.org/software/wget/manual/wget.html>.

## Examples

### Download the contents of a URL to a file (named "foo" in this case)

```bash
wget https://example.com/foo
```

### Download the contents of a URL to a file (named "bar" in this case)

```bash
wget [-O|--output-document] bar https://example.com/foo
```

### Download a single web page and all its resources with 3-second intervals between requests (scripts, stylesheets, images, etc.)

```bash
wget [-pkw|--page-requisites --convert-links --wait] 3 https://example.com/some_page.html
```

### Download all listed files within a directory and its sub-directories (does not download embedded page elements)

```bash
wget [-mnp|--mirror --no-parent] https://example.com/some_path/
```

### Limit the download speed and the number of connection retries

```bash
wget --limit-rate 300k [-t|--tries] 100 https://example.com/some_path/
```

### Download a file from an HTTP server using Basic Auth (also works for FTP)

```bash
wget --user username --password password https://example.com
```

### Continue an incomplete download

```bash
wget [-c|--continue] https://example.com
```

### Download all URLs stored in a text file to a specific directory

```bash
wget [-P|--directory-prefix] path/to/directory [-i|--input-file] path/to/URLs.txt
```
