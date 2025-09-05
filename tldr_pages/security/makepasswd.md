# makepasswd

> Generate and encrypt passwords. More information: <https://manpages.debian.org/latest/makepasswd/makepasswd.1.en.html>.

## Examples

### Generate a random password (8 to 10 characters long, containing letters and numbers)

```bash
makepasswd
```

### Generate a 10 characters long password

```bash
makepasswd --chars 10
```

### Generate a 5 to 10 characters long password

```bash
makepasswd --minchars 5 --maxchars 10
```

### Generate a password containing only the characters "b", "a" or "r"

```bash
makepasswd --string bar
```
