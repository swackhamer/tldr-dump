# git-mergetool

> Run merge conflict resolution tools to resolve merge conflicts. More information: <https://git-scm.com/docs/git-mergetool>.

## Examples

### Launch the default merge tool to resolve conflicts

```bash
git mergetool
```

### List valid merge tools

```bash
git mergetool --tool-help
```

### Launch the merge tool identified by a name

```bash
git mergetool [-t|--tool] tool_name
```

### Don't prompt before each invocation of the merge tool

```bash
git mergetool [-y|--no-prompt]
```

### Explicitly use the GUI merge tool (see the `merge.guitool` configuration variable)

```bash
git mergetool [-g|--gui]
```

### Explicitly use the regular merge tool (see the `merge.tool` configuration variable)

```bash
git mergetool --no-gui
```
