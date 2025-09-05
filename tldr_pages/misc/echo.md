# echo

> Print given arguments. See also: `printf`. More information: <https://www.gnu.org/software/coreutils/manual/html_node/echo-invocation.html>.

## Examples

### Print a text message. Note: Quotes are optional

```bash
echo "Hello World"
```

### Print a message with environment variables

```bash
echo "My path is $PATH"
```

### Print a message without the trailing newline

```bash
echo -n "Hello World"
```

### Append a message to the file

```bash
echo "Hello World" >> file.txt
```

### Enable interpretation of backslash escapes (special characters)

```bash
echo -e "Column 1\tColumn 2"
```

### Print the exit status of the last executed command (Note: In Windows Command Prompt and PowerShell the equivalent commands are `echo %errorlevel%` and `$lastexitcode` respectively)

```bash
echo $?
```
