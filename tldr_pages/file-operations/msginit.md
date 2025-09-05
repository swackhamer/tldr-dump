# msginit

> Generate language specific translation files based on Portable Object Templates. More information: <https://www.gnu.org/software/gettext/manual/gettext.html#msginit-Invocation>.

## Examples

### Generate Portable Object files in system locale from `messages.pot`

```bash
msginit
```

### Define locale to generate from a specific template

```bash
msginit [-l|--locale] locale [-i|--input] path/to/messages.pot
```

### Display help

```bash
msginit [-h|--help]
```
