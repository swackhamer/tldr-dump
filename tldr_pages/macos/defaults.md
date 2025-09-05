# defaults

> Read and write macOS user configuration for applications. More information: <https://keith.github.io/xcode-man-pages/defaults.1.html>.

## Examples

### Read system defaults for an application option

```bash
defaults read "application" "option"
```

### Read default values for an application option

```bash
defaults read -app "application" "option"
```

### Search for a keyword in domain names, keys, and values

```bash
defaults find "keyword"
```

### Write the default value of an application option

```bash
defaults write "application" "option" -type value
```

### Speed up Mission Control animations

```bash
defaults write com.apple.Dock expose-animation-duration -float 0.1
```

### Delete all defaults of an application

```bash
defaults delete "application"
```
