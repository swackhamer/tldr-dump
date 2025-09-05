# yacas

> Yet Another Computer Algebra System. More information: <https://www.yacas.org>.

## Examples

### Start an interactive `yacas` session

```bash
yacas
```

### While in a `yacas` session, execute a statement

```bash
Integrate(x)Cos(x);
```

### While in a `yacas` session, display an example

```bash
Example();
```

### Quit from a `yacas` session

```bash
quit
```

### Execute one or more `yacas` scripts (without terminal or prompts), then exit

```bash
yacas -p -c path/to/script1 path/to/script2 ...
```

### Execute and print the result of one statement, then exit

```bash
echo "Echo( Deriv(x)Cos(1/x) );" | yacas -p -c /dev/stdin
```
