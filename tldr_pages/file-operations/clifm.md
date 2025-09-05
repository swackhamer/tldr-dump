# clifm

> The command-line file manager. See also: `vifm`, `ranger`, `mc`, `nautilus`. More information: <https://github.com/leo-arch/clifm>.

## Examples

### Start CliFM

```bash
clifm
```

### Open the file or directory whose ELN (entry list number) is 12

```bash
12
```

### Create a new file and a new directory

```bash
<n>file dir/
```

### Search for PDF files in the current directory

```bash
</>*.pdf
```

### Select all PNG files in the current directory

```bash
<s> *.png
```

### Remove the previously selected files (use `<t>` to send the files to the recycle bin instead)

```bash
<r>sel
```

### Display help

```bash
<?>
```

### Exit CliFM

```bash
<q>
```
