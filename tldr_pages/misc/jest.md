# jest

> A zero-configuration JavaScript testing platform. More information: <https://jestjs.io>.

## Examples

### Run all available tests

```bash
jest
```

### Run the test suites from the given files

```bash
jest path/to/file1 path/to/file2 ...
```

### Run the test suites from files within the current and subdirectories, whose paths match the given `regex`

```bash
jest regex1 regex2
```

### Run the tests whose names match the given `regex`

```bash
jest --testNamePattern regex
```

### Run test suites related to a given source file

```bash
jest --findRelatedTests path/to/source_file.js
```

### Run test suites related to all uncommitted files

```bash
jest --onlyChanged
```

### Watch files for changes and automatically re-run related tests

```bash
jest --watch
```

### Display help

```bash
jest --help
```
