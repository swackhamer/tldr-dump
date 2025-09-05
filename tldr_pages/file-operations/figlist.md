# figlist

> List the figlet fonts and control files. See also: `figlet`, `showfigfonts`, `chkfont`. More information: <https://manned.org/figlist>.

## Examples

### List all available fonts using the default font directory

```bash
figlist
```

### List fonts from a custom directory

```bash
figlist -d path/to/directory
```

### Search for a font by keyword

```bash
figlist -d path/to/directory | grep keyword
```

### Count the total number of available fonts in a specified directory

```bash
figlist -d path/to/directory | wc [-l|--lines]
```
