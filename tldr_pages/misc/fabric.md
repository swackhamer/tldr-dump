# fabric

> An open-source framework for augmenting humans using AI. Provides a modular framework for solving specific problems using a crowdsourced set of AI prompts. More information: <https://github.com/danielmiessler/fabric#usage>.

## Examples

### Run the setup to configure fabric

```bash
fabric [-S|--setup]
```

### List all available patterns

```bash
fabric [-l|--listpatterns]
```

### Run a pattern with input from a file

```bash
fabric [-p|--pattern] pattern_name < path/to/input_file
```

### Run a pattern on a YouTube video URL

```bash
fabric [-y|--youtube] "https://www.youtube.com/watch?v=video_id" [-p|--pattern] pattern_name
```

### Chain patterns together by piping output from one to another

```bash
fabric [-p|--pattern] pattern1 | fabric [-p|--pattern] pattern2
```

### Run a custom user-defined pattern

```bash
fabric [-p|--pattern] custom_pattern_name
```

### Run a pattern and save the output to a file

```bash
fabric [-p|--pattern] pattern_name [-o|--output] path/to/output_file
```

### Run a pattern with the specified variables

```bash
fabric [-p|--pattern] pattern_name [-v|--variable] "variable_name:value"
```
