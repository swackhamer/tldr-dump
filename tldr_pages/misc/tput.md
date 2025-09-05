# tput

> View and modify terminal settings and capabilities. More information: <https://manned.org/tput>.

## Examples

### Move the cursor to a screen location

```bash
tput cup row column
```

### Set foreground (af) or background (ab) color

```bash
tput setaf|setab ansi_color_code
```

### Reverse text and background colors

```bash
tput rev
```

### Reset all terminal text attributes

```bash
tput sgr0
```

### Show number of columns, lines, or colors

```bash
tput cols|lines|colors
```

### Enable or disable word wrap

```bash
tput smam|rmam
```

### Hide or show the terminal cursor

```bash
tput civis|cnorm
```

### Save or restore terminal text status (smcup also captures scroll wheel events)

```bash
tput smcup|rmcup
```
