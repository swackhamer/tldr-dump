# ctest

> CMake test driver program. More information: <https://gitlab.kitware.com/cmake/community/wikis/doc/ctest/Testing-With-CTest>.

## Examples

### Run all tests defined in the CMake project, executing 4 [j]obs at a time in parallel

```bash
ctest [-j|--parallel] 4 --output-on-failure
```

### List available tests

```bash
ctest [-N|--show-only]
```

### Run a single test based on its name, or filter on a `regex`

```bash
ctest --output-on-failure [-R|--tests-regex] '^test_name$'
```
