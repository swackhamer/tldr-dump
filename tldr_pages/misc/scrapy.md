# scrapy

> Web-crawling framework. More information: <https://scrapy.org>.

## Examples

### Create a project

```bash
scrapy startproject project_name
```

### Create a spider (in project directory)

```bash
scrapy genspider spider_name website_domain
```

### Edit spider (in project directory)

```bash
scrapy edit spider_name
```

### Run spider (in project directory)

```bash
scrapy crawl spider_name
```

### Fetch a webpage as Scrapy sees it and print the source to `stdout`

```bash
scrapy fetch url
```

### Open a webpage in the default browser as Scrapy sees it (disable JavaScript for extra fidelity)

```bash
scrapy view url
```

### Open Scrapy shell for URL, which allows interaction with the page source in a Python shell (or IPython if available)

```bash
scrapy shell url
```
