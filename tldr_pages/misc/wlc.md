# wlc

> Manage localization projects on a Weblate instance. More information: <https://docs.weblate.org/en/latest/wlc.html#commands>.

## Examples

### List projects using a configuration file

```bash
wlc [-c|--config] path/to/file list-projects
```

### List components in a project, and override API URL and API key

```bash
wlc [-u|--url] URL [-k|--key] key ls project
```

### List translations from a component in a specific format

```bash
wlc [-f|--format] text|csv|json|html ls project/component
```

### Print statistics for a project

```bash
wlc stats project
```

### Display help

```bash
wlc [-h|--help]
```
