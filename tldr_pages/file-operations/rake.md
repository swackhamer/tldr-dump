# rake

> A Make-like program for Ruby. Tasks for `rake` are specified in a Rakefile. More information: <https://ruby.github.io/rake>.

## Examples

### Run the `default` Rakefile task

```bash
rake
```

### Run a specific task

```bash
rake task
```

### Execute `n` jobs at a time in parallel (number of CPU cores + 4 by default)

```bash
rake --jobs n
```

### Use a specific Rakefile

```bash
rake --rakefile path/to/Rakefile
```

### Execute `rake` from another directory

```bash
rake --directory path/to/directory
```
