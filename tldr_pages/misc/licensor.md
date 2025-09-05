# licensor

> Write licenses to `stdout`. More information: <https://github.com/raftario/licensor>.

## Examples

### Write the MIT license to a file named `LICENSE`

```bash
licensor MIT > LICENSE
```

### Write the MIT license with a placeholder copyright notice to a file named `LICENSE`

```bash
licensor [-p|--keep-placeholder] MIT > LICENSE
```

### Specify a copyright holder named Bobby Tables

```bash
licensor MIT "Bobby Tables" > LICENSE
```

### Specify licence exceptions with a WITH expression

```bash
licensor "Apache-2.0 WITH LLVM-exception" > LICENSE
```

### List all available licenses

```bash
licensor [-l|--licenses]
```

### List all available exceptions

```bash
licensor [-e|--exceptions]
```
