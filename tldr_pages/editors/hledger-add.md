# hledger-add

> Record new transactions with interactive prompting in the console. More information: <https://hledger.org/hledger.html#add>.

## Examples

### Record new transactions, saving to the default journal file

```bash
hledger add
```

### Add transactions to `2024.journal`, but also load `2023.journal` for completions

```bash
hledger add [-f|--file] path/to/2024.journal [-f|--file] path/to/2023.journal
```

### Provide answers for the first four prompts

```bash
hledger add today 'best buy' expenses:supplies '$20'
```

### Show `add`'s options and documentation with `$PAGER`

```bash
hledger add [-h|--help]
```

### Show `add`'s documentation with `info` or `man` if available

```bash
hledger help add
```
