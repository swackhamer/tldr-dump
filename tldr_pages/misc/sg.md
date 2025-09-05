# sg

> Ast-grep is a tool for code structural search, lint, and rewriting. More information: <https://ast-grep.github.io/guide/introduction.html>.

## Examples

### Scan for possible queries using interactive mode

```bash
sg scan --interactive
```

### Rewrite code in the current directory using patterns

```bash
sg run --pattern 'foo' --rewrite 'bar' --lang python
```

### Visualize possible changes without applying them

```bash
sg run --pattern 'useState<number>($A)' --rewrite 'useState($A)' --lang typescript
```

### Output results as JSON, extract information using `jq` and interactively view it using `jless`

```bash
sg run --pattern 'Some($A)' --rewrite 'None' --json | jq '.[].replacement' | jless
```
