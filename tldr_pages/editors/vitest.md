# vitest

> Fast, modern testing framework built for Vite, offering seamless integration, TypeScript support, and a Jest-compatible API for unit, integration, and snapshot testing. More information: <https://vitest.dev/guide>.

## Examples

### Run all available tests

```bash
vitest run
```

### Run the test suites from the given files

```bash
vitest run path/to/file1 path/to/file2 ...
```

### Run the test suites from files within the current and subdirectories, whose paths match the given `regex`

```bash
vitest run regex1 regex2
```

### Run the tests whose names match the given `regex`

```bash
vitest run --testNamePattern regex
```

### Watch files for changes and automatically re-run related tests

```bash
vitest
```

### Run tests with coverage

```bash
vitest run --coverage
```

### Run all tests but stops immediately after the first test failure

```bash
vitest run --bail=1
```

### Display help

```bash
vitest --help
```
