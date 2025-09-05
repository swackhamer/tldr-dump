# gitmoji

> Interactively insert emojis on commits. More information: <https://github.com/carloscuesta/gitmoji-cli>.

## Examples

### Start the commit wizard

```bash
gitmoji --commit
```

### Initialize the Git hook (so `gitmoji` will be run every time `git commit` is run)

```bash
gitmoji --init
```

### Remove the Git hook

```bash
gitmoji --remove
```

### List all available emojis and their descriptions

```bash
gitmoji --list
```

### Search emoji list for a list of keywords

```bash
gitmoji --search keyword1 keyword2
```

### Update cached list of emojis from main repository

```bash
gitmoji --update
```

### Configure global preferences

```bash
gitmoji --config
```
