# arduino

> Arduino Studio - Integrated Development Environment for the Arduino platform. More information: <https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc>.

## Examples

### Build a sketch

```bash
arduino --verify path/to/file.ino
```

### Build and upload a sketch

```bash
arduino --upload path/to/file.ino
```

### Build and upload a sketch to an Arduino Nano with an Atmega328p CPU, connected on port `/dev/ttyACM0`

```bash
arduino --board arduino:avr:nano:cpu=atmega328p --port /dev/ttyACM0 --upload path/to/file.ino
```

### Set the preference `name` to a given `value`

```bash
arduino --pref name=value
```

### Build a sketch, put the build results in the build directory, and reuse any previous build results in that directory

```bash
arduino --pref build.path=path/to/build_directory --verify path/to/file.ino
```

### Save any (changed) preferences to `preferences.txt`

```bash
arduino --save-prefs
```

### Install the latest SAM board

```bash
arduino --install-boards "arduino:sam"
```

### Install Bridge and Servo libraries

```bash
arduino --install-library "Bridge:1.0.0,Servo:1.2.0"
```
