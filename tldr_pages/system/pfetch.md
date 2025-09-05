# pfetch

> Display system information. More information: <https://github.com/dylanaraps/pfetch>.

## Examples

### Display the ASCII art and default fields

```bash
pfetch
```

### Display only the ASCII art and color palette fields

```bash
PF_INFO="ascii palette" pfetch
```

### Display all possible fields

```bash
PF_INFO="ascii title os host kernel uptime pkgs memory shell editor wm de palette" pfetch
```

### Display a different username and hostname

```bash
USER="user" HOSTNAME="hostname" pfetch
```

### Display without colors

```bash
PF_COLOR=0 pfetch
```
