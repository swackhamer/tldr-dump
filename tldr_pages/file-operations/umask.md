# umask

> Manage the read/write/execute permissions that are masked out (i.e. restricted) for newly created files by the user. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-umask>.

## Examples

### Display the current mask in octal notation

```bash
umask
```

### Display the current mask in symbolic (human-readable) mode

```bash
umask -S
```

### Change the mask symbolically to allow read permission for all users (the rest of the mask bits are unchanged)

```bash
umask a+r
```

### Set the mask (using octal) to restrict no permissions for the file's owner, and restrict all permissions for everyone else

```bash
umask 077
```
