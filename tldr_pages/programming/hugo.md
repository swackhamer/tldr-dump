# hugo

> Template-based static site generator. Uses modules, components, and themes. Some subcommands such as `server` have their own usage documentation. More information: <https://gohugo.io/commands/>.

## Examples

### Create a new Hugo site

```bash
hugo new site path/to/site
```

### Create a new Hugo theme (themes may also be downloaded from <https://themes.gohugo.io/>)

```bash
hugo new theme theme_name
```

### Create a new page

```bash
hugo new section_name/page_name
```

### Build a site to the `./public/` directory

```bash
hugo
```

### Build a site including pages that are marked as a "draft"

```bash
hugo [-D|--buildDrafts]
```

### Build a site on your local IP

```bash
hugo server --bind local_ip --baseURL http://local_ip
```

### Build a site to a given directory

```bash
hugo [-d|--destination] path/to/destination
```

### Build a site, start up a webserver to serve it, and automatically reload when pages are edited

```bash
hugo server
```
