# nnn

> Interactive terminal file manager and disk usage analyzer. More information: <https://github.com/jarun/nnn/wiki/Usage#program-options>.

## Examples

### Open the current directory (or specify one as the first argument)

```bash
nnn
```

### Start in detailed mode

```bash
nnn -d
```

### Show hidden files

```bash
nnn -H
```

### Open an existing bookmark (defined in the `NNN_BMS` environment variable)

```bash
nnn -b bookmark_name
```

### Sort files on [a]pparent disk usage / [d]isk usage / [e]xtension / [r]everse / [s]ize / [t]ime / [v]ersion

```bash
nnn -T a|d|e|r|s|t|v
```

### Open a file you have selected. Select the file then press `<o>`, and type a program to open the file in

```bash
nnn -o
```
