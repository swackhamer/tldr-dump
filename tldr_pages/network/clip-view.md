# clip-view

> Command Line Interface Pages render. Render for a TlDr-like project with much a more extensive syntax and several render modes. More information: <https://github.com/command-line-interface-pages/v2-tooling/tree/main/clip-view>.

## Examples

### Render specific local pages

```bash
clip-view path/to/page1.clip path/to/page2.clip ...
```

### Render specific remote pages

```bash
clip-view page_name1 page_name2 ...
```

### Render pages by a specific render

```bash
clip-view --render tldr|tldr-colorful|docopt|docopt-colorful page_name1 page_name2 ...
```

### Render pages with a specific color theme

```bash
clip-view --theme path/to/local_theme.yaml|remote_theme_name page_name1 page_name2 ...
```

### Clear a page or theme cache

```bash
clip-view --clear-page|theme-cache
```

### Display help

```bash
clip-view --help
```

### Display version

```bash
clip-view --version
```
