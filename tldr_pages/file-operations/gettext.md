# gettext

> Translates a string using stored translations in a compiled `.mo` file. Translations are stored in `/usr/share/locale/<locale_name>/LC_MESSAGES/` with `domain` being the filename without its extension. See also: `msgfmt`, `msgunfmt`. More information: <https://www.gnu.org/software/gettext/manual/gettext.html#gettext-Invocation>.

## Examples

### Get the translation of a string as specified in the domain file (falls back to given `msgid` if no translation exists)

```bash
LANGUAGE=locale gettext [-d|--domain] domain "msgid"
```

### Display help

```bash
gettext [-h|--help]
```

### Display gettext version

```bash
gettext [-V|--version]
```
