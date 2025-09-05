# tox

> Automate Python testing across multiple Python versions. Use tox.ini to configure environments and test command. More information: <https://github.com/tox-dev/tox>.

## Examples

### Run tests on all test environments

```bash
tox
```

### Create a `tox.ini` configuration

```bash
tox-quickstart
```

### List the available environments

```bash
tox [-a|--listenvs-all]
```

### Run tests on a specific environment (e.g. Python 3.6)

```bash
tox -e py36
```

### Force the virtual environment to be recreated

```bash
tox [-r|--recreate] -e py27
```
