# mods

> AI for the command-line, built for pipelines. More information: <https://github.com/charmbracelet/mods>.

## Examples

### Ask a generic question

```bash
mods "write me a poem about platypuses"
```

### Open settings in your `$EDITOR`

```bash
mods --settings
```

### Ask for comments on your code, in markdown format

```bash
mods --format "what are your thoughts on improving this code?" < path/to/file
```

### Ask for help with your documentation, in markdown format

```bash
mods --format "write a new section to this readme for a feature that sends you a free rabbit if you hit r" < README.md
```

### Organize your videos, in markdown format

```bash
ls path/to/videos | mods --format "organize these by decade and summarize"
```

### Read through raw HTML and summarize the contents, in markdown format

```bash
curl "https://api.open-meteo.com/v1/forecast?latitude=29.00&longitude=-90.00&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m" | mods --format "summarize this weather data for a human"
```

### Display help

```bash
mods --help
```
