# php

> PHP command-line interface. More information: <https://php.net>.

## Examples

### Parse and execute a PHP script

```bash
php path/to/file
```

### Check syntax on (i.e. [l]int) a PHP script

```bash
php [-l|--syntax-check] path/to/file
```

### Run PHP inter[a]ctively

```bash
php [-a|--interactive]
```

### Run PHP code (Notes: Don't use <? ?> tags; escape double quotes with backslash)

```bash
php [-r|--run] "code"
```

### Start a PHP built-in web [S]erver in the current directory

```bash
php [-S|--server] host:port
```

### List installed PHP extensions

```bash
php [-m|--modules]
```

### Display information about the current PHP configuration

```bash
php [-i|--info]
```

### Display information about a specific function

```bash
php [--rf|--rfunction] function_name
```
