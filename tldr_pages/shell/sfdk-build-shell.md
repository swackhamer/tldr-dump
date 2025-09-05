# sfdk-build-shell

> Executes custom steps in build engine. See also: `sfdk config` for configuring the build target and `sfdk build-init` for initializing build tree. More information: <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/20-building-mb2/doc/command.build-shell.adoc>.

## Examples

### Launch interactive shell in the build engine

```bash
sfdk build-shell
```

### Run a specified command in the build shell

```bash
sfdk build-shell command
```

### Launch interactive shell in the build engine in maintenance mode, when inspecting or modifying the build environment

```bash
sfdk build-shell --maintain
```
