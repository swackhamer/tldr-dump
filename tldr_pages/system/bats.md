# bats

> Bash Automated Testing System: a TAP (<https://testanything.org/>) compliant testing framework for Bash. More information: <https://bats-core.readthedocs.io/en/stable/usage.html>.

## Examples

### Run a BATS test script and output results in the TAP (Test Anything Protocol) format

```bash
bats [-t|--tap] path/to/test.bats
```

### Count test cases of a test script without running any tests

```bash
bats [-c|--count] path/to/test.bats
```

### Run BATS test cases recursively (files with a `.bats` extension)

```bash
bats [-r|--recursive] path/to/directory
```

### Output results in a specific format

```bash
bats [-F|--formatter] pretty|tap|tap13|junit path/to/test.bats
```

### Add timing information to tests

```bash
bats [-T|--timing] path/to/test.bats
```

### Run specific number of jobs in parallel (requires GNU `parallel` to be installed)

```bash
bats [-j|--jobs] number path/to/test.bats
```
