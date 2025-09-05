# sfdk-build-requires

> Updates build time dependencies. More information: <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/20-building-mb2/doc/command.build-requires.adoc>.

## Examples

### Run a subcommand refreshing the cache

```bash
sfdk build-requires --refresh subcommand
```

### Run a subcommand without refreshing the cache

```bash
sfdk build-requires --no-refresh subcommand
```

### Install or update the build-time dependencies

```bash
sfdk build-requires pull
```

### Install or update the build-time dependencies, omitting all extra ones

```bash
sfdk build-requires reset
```

### Show the difference between current and clean build environments

```bash
sfdk build-requires diff
```
