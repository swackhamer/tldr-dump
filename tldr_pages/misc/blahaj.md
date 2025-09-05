# blahaj

> A lolcat-like output colorizer that also prints flags and colorful sharks. More information: <https://codeberg.org/GeopJr/BLAHAJ>.

## Examples

### Get a list of possible flags/colors

```bash
blahaj --flags
```

### Print a shark (blahaj) with default trans colors

```bash
blahaj [-s|--shark]
```

### Print a random flag with a 2x size multiplier

```bash
blahaj [-f|--flag] [-r|--random] [-m|--multiplier] 2
```

### Print the result of a text-producing command with lesbian colors

```bash
cowsay "Hello, world" | blahaj [-c|--colors] lesbian
```

### Print text and color by individual character

```bash
echo "Hello, world" | blahaj [-i|--individual]
```

### Print contents of a text document, coloring the background instead of text, by word

```bash
blahaj [-w|--words] [-b|--background] path/to/file
```
