# bw

> Access and manage a Bitwarden vault. More information: <https://help.bitwarden.com/article/cli/>.

## Examples

### Log in to a Bitwarden user account

```bash
bw login
```

### Log out of a Bitwarden user account

```bash
bw logout
```

### Search and display items from Bitwarden vault

```bash
bw list items --search github
```

### Display a particular item from Bitwarden vault

```bash
bw get item github
```

### Create a folder in Bitwarden vault

```bash
echo -n '{"name":"My Folder1"}' | base64 | bw create folder
```
