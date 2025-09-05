# nano

> Text editor. An enhanced `pico` clone. See also: `pico`, `rnano`. More information: <https://nano-editor.org/dist/latest/nano.html>.

## Examples

### Open specific files, moving to the next file after closing the previous one

```bash
nano path/to/file1 path/to/file2 ...
```

### Start the editor without using configuration files

```bash
nano [-I|--ignorercfiles]
```

### Open a file and position the cursor at a specific line and column

```bash
nano +line,column path/to/file
```

### Open a file and enable soft wrapping

```bash
nano [-S|--softwrap] path/to/file
```

### Open a file and indent new lines to the previous line's indentation

```bash
nano [-i|--autoindent] path/to/file
```

### Open a file and create a backup file (`path/to/file~`) on save

```bash
nano [-B|--backup] path/to/file
```

### Open a file in restricted mode (i.e. don't read/write to files not specified on the command-line)

```bash
nano [-R|--restricted] path/to/file
```

### Exit nano

```bash
<Ctrl x>
```
