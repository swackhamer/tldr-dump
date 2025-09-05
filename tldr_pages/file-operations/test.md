# test

> Check file types and compare values. Returns 0 if the condition evaluates to true, 1 if it evaluates to false. More information: <https://www.gnu.org/software/coreutils/manual/html_node/test-invocation.html>.

## Examples

### Test if a given variable is equal to a given string

```bash
test "$MY_VAR" = "/bin/zsh"
```

### Test if a given variable is empty ([z]ero length)

```bash
test -z "$GIT_BRANCH"
```

### Test if a [f]ile exists

```bash
test -f "path/to/file_or_directory"
```

### Test if a [d]irectory does not exist

```bash
test ! -d "path/to/directory"
```

### If A is true, then do B, or C in the case of an error (notice that C may run even if A fails)

```bash
test condition && echo "true" || echo "false"
```

### Use `test` in a conditional statement

```bash
if test -f "path/to/file"; then echo "File exists"; else echo "File does not exist"; fi
```
