# lit

> LLVM integrated tester for executing LLVM and Clang style test suites, summarizing results. Part of LLVM. More information: <https://www.llvm.org/docs/CommandGuide/lit.html>.

## Examples

### Run a specified test case

```bash
lit path/to/test_file.test
```

### Run all test cases in a specified directory

```bash
lit path/to/test_suite
```

### Run all test cases and check the wall time for each cases, then report to summary output

```bash
lit path/to/test_suite --time-tests
```

### Run individual tests with Valgrind (memory check and memory leak test)

```bash
lit path/to/test_file.test --vg --vg-leak --vg-args=args_to_valgrind
```
