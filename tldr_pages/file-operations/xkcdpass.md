# xkcdpass

> A flexible and scriptable password generator which generates strong passphrases. Inspired by XKCD 936. More information: <https://github.com/redacted/XKCD-password-generator>.

## Examples

### Generate one passphrase with the default options

```bash
xkcdpass
```

### Generate one passphrase whose first letters of each word match the provided argument

```bash
xkcdpass [-a|--acrostic] acrostic
```

### Generate passwords interactively

```bash
xkcdpass [-i|--interactive]
```
