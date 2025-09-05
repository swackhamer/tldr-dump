# ledger

> A powerful, double-entry accounting system. More information: <https://www.ledger-cli.org>.

## Examples

### Print a balance report showing totals

```bash
ledger balance --file path/to/ledger.journal
```

### List all postings in Expenses ordered by amount

```bash
ledger register expenses --sorted amount
```

### Print total Expenses other than Drinks and Food

```bash
ledger balance Expenses and not (Drinks or Food)
```

### Print a budget report

```bash
ledger budget
```

### Print summary information about all the postings

```bash
ledger stats
```
