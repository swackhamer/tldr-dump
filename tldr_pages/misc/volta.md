# volta

> A JavaScript Tool Manager that installs Node.js runtimes, npm and Yarn package managers, or any binaries from npm. More information: <https://volta.sh>.

## Examples

### List all installed tools

```bash
volta list
```

### Install the latest version of a tool

```bash
volta install node|npm|yarn|package_name
```

### Install a specific version of a tool

```bash
volta install node|npm|yarn@version
```

### Choose a tool version for a project (will store it in `package.json`)

```bash
volta pin node|npm|yarn@version
```

### Display help

```bash
volta help
```

### Display help for a subcommand

```bash
volta help fetch|install|uninstall|pin|list|completions|which|setup|run|help
```
