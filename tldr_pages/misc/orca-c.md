# orca-c

> A C-port of the ORCA live programming environment. ORCA is an esoteric programming language for creating procedural sequencers. More information: <https://github.com/hundredrabbits/Orca-c>.

## Examples

### Start ORCA with an empty workspace

```bash
orca-c
```

### Start ORCA and open a specific file

```bash
orca-c path/to/file.orca
```

### Start ORCA and set a specific tempo (defaults to 120)

```bash
orca-c --bpm beats_per_minute
```

### Start ORCA and set the size of the grid

```bash
orca-c --initial-size columnsxrows
```

### Start ORCA and set the maximum number of undo steps (defaults to 100)

```bash
orca-c --undo-limit limit
```

### Show the main menu inside of ORCA

```bash
<F1>
```

### Show all shortcuts inside of ORCA

```bash
<?>
```

### Show all ORCA operators inside of ORCA

```bash
<Ctrl g>
```
