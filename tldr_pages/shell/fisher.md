# fisher

> Fisher, a fish-shell plugin manager. Install plugins by name or from a managed 'fishfile' for bundled installs. More information: <https://github.com/jorgebucaran/fisher>.

## Examples

### Install one or more plugins

```bash
fisher plugin1 plugin2
```

### Install a plugin from a GitHub gist

```bash
fisher gist_url
```

### Edit 'fishfile' manually with your favorite editor and install multiple plugins

```bash
editor ~/.config/fish/fishfile; fisher
```

### List installed plugins

```bash
fisher ls
```

### Update plugins

```bash
fisher update
```

### Remove one or more plugins

```bash
fisher remove plugin1 plugin2
```
