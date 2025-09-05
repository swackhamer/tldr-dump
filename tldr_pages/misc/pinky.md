# pinky

> Print user information using the `finger` protocol. More information: <https://manned.org/pinky>.

## Examples

### Display details about the current user

```bash
pinky
```

### Display details for a specific user

```bash
pinky user
```

### Display details in the long format

```bash
pinky user -l
```

### Omit the user's home directory and shell in long format

```bash
pinky user -lb
```

### Omit the user's project file in long format

```bash
pinky user -lh
```

### Omit the column headings in short format

```bash
pinky user -f
```
