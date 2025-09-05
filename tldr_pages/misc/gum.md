# gum

> Make glamorous shell scripts. More information: <https://github.com/charmbracelet/gum>.

## Examples

### Interactively pick a specific option to print to `stdout`

```bash
gum choose "option_1" "option_2" "option_3"
```

### Open an interactive prompt for the user to input a string with a specific placeholder

```bash
gum input --placeholder "value"
```

### Open an interactive confirmation prompt and exit with either `<0>` or `<1>`

```bash
gum confirm "Continue?" --default=false --affirmative "Yes" --negative "No" && echo "Yes selected" || echo "No selected"
```

### Show a spinner while a command is taking place with text alongside

```bash
gum spin --spinner dot|line|minidot|jump|pulse|points|globe|moon|monkey|meter|hamburger --title "loading..." -- command
```

### Format text to include emojis

```bash
gum format -t emoji ":smile: :heart: hello"
```

### Interactively prompt for multi-line text (`<Ctrl d>` to save) and write to `data.txt`

```bash
gum write > data.txt
```
