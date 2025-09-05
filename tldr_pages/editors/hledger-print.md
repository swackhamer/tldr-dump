# hledger-print

> Show full journal entries, representing transactions. More information: <https://hledger.org/hledger.html#print>.

## Examples

### Show all transactions in the default journal file

```bash
hledger print
```

### Show transactions, with any implied amounts or costs made explicit

```bash
hledger print [-x|--explicit] --infer-costs
```

### Show transactions from two specified files, with amounts converted to cost

```bash
hledger print [-f|--file] path/to/2023.journal [-f|--file] path/to/2024.journal [-B|--cost]
```

### Show `$` transactions in `*food*` but not `*groceries*` accounts this month

```bash
hledger print cur:\\$ food not:groceries date:thismonth
```

### Show transactions of amount 50 or more, with `whole foods` in their description

```bash
hledger print amt:'>50' desc:'whole foods'
```

### Show cleared transactions, with `EUR` amounts rounded and with decimal commas

```bash
hledger print [-C|--cleared] --commodity '1000, EUR' --round hard
```

### Write transactions from `foo.journal` as a CSV file

```bash
hledger print [-f|--file] path/to/foo.journal [-o|--output-file] path/to/output_file.csv
```
