# expr

> Evaluate expressions and manipulate strings. More information: <https://www.gnu.org/software/coreutils/manual/html_node/expr-invocation.html>.

## Examples

### Get the length of a specific string

```bash
expr length "string"
```

### Get the substring of a string with a specific length

```bash
expr substr "string" from length
```

### Match a specific substring against an anchored pattern

```bash
expr match "string" 'pattern'
```

### Get the first char position from a specific set in a string

```bash
expr index "string" "chars"
```

### Calculate a specific mathematic expression

```bash
expr expression1 +|-|*|/|% expression2
```

### Get the first expression if its value is non-zero and not null otherwise get the second one

```bash
expr expression1 \| expression2
```

### Get the first expression if both expressions are non-zero and not null otherwise get zero

```bash
expr expression1 \& expression2
```
