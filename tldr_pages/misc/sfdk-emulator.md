# sfdk-emulator

> Maintains and controls emulators. More information: <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/40-testing-maintain/doc/command.emulator.adoc>.

## Examples

### Display the installed emulators

```bash
sfdk emulator list
```

### Start an emulator

```bash
sfdk emulator start name
```

### Stop an emulator

```bash
sfdk emulator stop name
```

### Display emulator status

```bash
sfdk emulator status name
```

### Run an interactive shell on an emulator

```bash
sfdk emulator exec emulator
```

### Execute a command on an emulator

```bash
sfdk emulator exec emulator command
```

### Set a property

```bash
sfdk emulator set name property=value
```

### Show emulator properties

```bash
sfdk emulator show name
```
