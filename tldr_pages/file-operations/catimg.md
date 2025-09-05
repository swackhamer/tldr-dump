# catimg

> Image printing in the terminal. See also: `pixterm`, `chafa`. More information: <https://manned.org/catimg>.

## Examples

### Print a JPEG, PNG, or GIF to the terminal

```bash
catimg path/to/file
```

### Double the [r]esolution of an image

```bash
catimg -r 2 path/to/file
```

### Disable 24-bit color for better [t]erminal support

```bash
catimg -t path/to/file
```

### Specify a custom [w]idth or [H]eight

```bash
catimg -w|-H 40 path/to/file
```
