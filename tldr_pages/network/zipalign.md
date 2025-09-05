# zipalign

> Zip archive alignment tool. Part of the Android SDK build tools. More information: <https://developer.android.com/tools/zipalign>.

## Examples

### Align the data of a Zip file on 4-byte boundaries

```bash
zipalign 4 path/to/input.zip path/to/output.zip
```

### Check that a Zip file is correctly aligned on 4-byte boundaries and display the results in a verbose manner

```bash
zipalign -v -c 4 path/to/input.zip
```
