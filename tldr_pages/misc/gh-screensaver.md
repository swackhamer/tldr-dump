# gh-screensaver

> Extension for GitHub CLI that runs animated terminal screensavers. See also: `gh extension`. More information: <https://github.com/vilmibm/gh-screensaver>.

## Examples

### Run a random screensaver

```bash
gh screensaver
```

### Run a specific screensaver

```bash
gh screensaver [-s|--saver] fireworks|life|marquee|pipes|pollock|starfield
```

### Run the "marquee" screensaver with a specific text and font

```bash
gh screensaver [-s|--saver] marquee -- --message="message" --font=font_name
```

### Run the "starfield" screensaver with a specific density and speed

```bash
gh screensaver [-s|--saver] starfield -- --density 500 --speed 10
```

### List available screensavers

```bash
gh screensaver [-l|--list]
```
