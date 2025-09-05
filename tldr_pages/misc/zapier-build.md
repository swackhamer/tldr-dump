# zapier-build

> Build a pushable `zip` of a Zapier integration. More information: <https://platform.zapier.com/reference/cli#build>.

## Examples

### Create a build

```bash
zapier build
```

### Disable smart file inclusion (will only include files required by `index.js`)

```bash
zapier build --disable-dependency-detection
```

### Show extra debugging output

```bash
zapier build [-d|--debug]
```
