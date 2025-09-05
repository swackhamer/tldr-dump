# sfdk-qmltypes

> Generate qmltypes files. More information: <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/80-ide-qmltypes/doc/command.qmltypes.adoc>.

## Examples

### Generate qmltypes files

```bash
sfdk qmltypes
```

### Generate qmltypes files without deploying them (usually to emulator)

```bash
sfdk qmltypes --no-deploy
```

### Generate qmltypes files without restoring the emulator after deployment

```bash
sfdk qmltypes --no-restore-emulator
```

### Generate qmltypes files and restore the emulator after deployment even on failure

```bash
sfdk qmltypes --restore-emulator
```

### Generate qmltypes files without reverting changes which only include removal of statements with `sdk-make-qmltypes:keep` in comments

```bash
sfdk qmltypes --no-keep
```
