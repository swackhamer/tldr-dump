# xidel

> Download and extract data from HTML/XML pages as well as JSON APIs. More information: <https://www.videlibri.de/xidel.html>.

## Examples

### Print all URLs found by a Google search

```bash
xidel https://www.google.com/search?q=test [-e|--extract] "//a/extract(@href, 'url[?]q=([^&]+)&', 1)[. != '']"
```

### Print the title of all pages found by a Google search and download them

```bash
xidel https://www.google.com/search?q=test [-f|--follow] "//a/extract(@href, 'url[?]q=([^&]+)&', 1)[. != '']" [-e|--extract] //title --download '{$host}/'
```

### Follow all links on a page and print the titles, with XPath

```bash
xidel https://example.org [-f|--follow] //a [-e|--extract] //title
```

### Follow all links on a page and print the titles, with CSS selectors

```bash
xidel https://example.org [-f|--follow] "css('a')" --css title
```

### Follow all links on a page and print the titles, with pattern matching

```bash
xidel https://example.org [-f|--follow] "<a>{.}</a>*" [-e|--extract] "<title>{.}</title>"
```

### Read the pattern from example.xml (which will also check if the element containing "ood" is there, and fail otherwise)

```bash
xidel path/to/example.xml [-e|--extract] "<x><foo>ood</foo><bar>{.}</bar></x>"
```

### Print all newest Stack Overflow questions with title and URL using pattern matching on their RSS feed

```bash
xidel http://stackoverflow.com/feeds [-e|--extract] "<entry><title>{title:=.}</title><link>{uri:=@href}</link></entry>+"
```

### Check for unread Reddit mail, Webscraping, combining CSS, XPath, JSONiq, and automatically form evaluation

```bash
xidel https://reddit.com [-f|--follow] "form(css('form.login-form')[1], {'user': '$your_username', 'passwd': '$your_password'})" [-e|--extract] "css('#mail')/@title"
```
