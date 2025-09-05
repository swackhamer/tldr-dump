# gpgconf

> Modify .gnupg home directories. More information: <https://www.gnupg.org/documentation/manuals/gnupg/gpgconf.html>.

## Examples

### List all components

```bash
gpgconf --list-components
```

### List the directories used by gpgconf

```bash
gpgconf [-L|--list-dirs]
```

### List all options of a component

```bash
gpgconf --list-options component
```

### List programs and test whether they are runnable

```bash
gpgconf --check-programs
```

### Reload a component

```bash
gpgconf --reload component
```
