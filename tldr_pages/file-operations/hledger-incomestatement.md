# hledger-incomestatement

> Show revenue inflows and expense outflows during the report period. Amounts are shown with normal positive sign, as in conventional financial statements. More information: <https://hledger.org/hledger.html#incomestatement>.

## Examples

### Show revenues and expenses (changes in `Revenue` and `Expense` accounts)

```bash
hledger [is|incomestatement]
```

### Show revenues and expenses each month

```bash
hledger [is|incomestatement] [-M|--monthly]
```

### Show monthly revenues/expenses/totals, largest first, summarised to 2 levels

```bash
hledger [is|incomestatement] [-MTAS|--monthly --row-total --average --sort-amount] [-2|--depth 2]
```

### Same as above, and generate HTML output in `is.html`

```bash
hledger [is|incomestatement] [-MTAS|--monthly --row-total --average --sort-amount] [-2|--depth 2] [-o|--output-file] is.html
```
