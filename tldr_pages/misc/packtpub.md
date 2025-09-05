# packtpub

> Download freely offered books from packtpub.com. More information: <https://github.com/vladimyr/packtpub-cli>.

## Examples

### Download the daily offer book into the current directory with the specified book format (defaults to `pdf`)

```bash
packtpub download [-t|--type] pdf|ebup|mobi
```

### Download the daily offer book into the specified directory

```bash
packtpub download [-d|--dir] path/to/directory
```

### Start an interactive login to packtpub.com

```bash
packtpub login
```

### Log out from packtpub.com

```bash
packtpub logout
```

### Display the daily offer

```bash
packtpub view-offer
```

### Open the daily offer in the default web browser

```bash
packtpub view-offer
```

### Display the currently logged-in user

```bash
packtpub whoami
```
