# hledger-ui

> A terminal interface (TUI) for `hledger`, a robust, friendly plain text accounting app. More information: <https://hledger.org/hledger-ui.html>.

## Examples

### Start in the main menu screen, reading from the default journal file

```bash
hledger-ui
```

### Start with a different color theme

```bash
hledger-ui --theme terminal|greenterm|dark
```

### Start in the balance sheet accounts screen, showing hierarchy down to level 3

```bash
hledger-ui --bs [-t|--tree] [-3|--depth 3]
```

### Start in this account's screen, showing cleared transactions, and reload on change

```bash
hledger-ui --register assets:bank:checking [-C|--cleared] [-w|--watch]
```

### Read two journal files, and show amounts as current value when known

```bash
hledger-ui [-f|--file] path/to/2024.journal [-f|--file] path/to/2024-prices.journal --value now
```

### Show the manual in Info format, if possible

```bash
hledger-ui --info
```

### Display help

```bash
hledger-ui [-h|--help]
```
