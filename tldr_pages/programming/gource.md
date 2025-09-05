# gource

> Renders an animated tree diagram of Git, SVN, Mercurial and Bazaar repositories. It shows files and directories being created, modified or removed over time. More information: <https://gource.io>.

## Examples

### Run gource in a directory (if it isn't the repository's root directory, the root is sought up from there)

```bash
gource path/to/repository
```

### Run gource in the current directory, with a custom output resolution

```bash
gource -widthxheight
```

### Specify how long each day should be in the animation (this combines with -c, if provided)

```bash
gource [-s|--seconds-per-day] seconds
```

### Use fullscreen mode and a custom background color

```bash
gource [-f|--fullscreen ] [-b|--background-colour] hex_color_code
```

### Specify the animation title

```bash
gource --title title
```

### Pause the animation

```bash
<Space>
```

### Adjust simulation speed

```bash
<+|->
```

### Display help

```bash
gource [-h|--help]
```
