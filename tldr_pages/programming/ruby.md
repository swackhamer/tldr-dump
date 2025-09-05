# ruby

> Ruby programming language interpreter. See also: `gem`, `bundler`, `rake`, `irb`. More information: <https://manned.org/ruby>.

## Examples

### Execute a Ruby script

```bash
ruby path/to/script.rb
```

### Execute a single Ruby command in the command-line

```bash
ruby -e "command"
```

### Check for syntax errors on a given Ruby script

```bash
ruby -c path/to/script.rb
```

### Start the built-in HTTP server on port 8080 in the current directory

```bash
ruby -run -e httpd
```

### Locally execute a Ruby binary without installing the required library it depends on

```bash
ruby -I path/to/library_folder -r library_require_name path/to/bin_folder/bin_name
```

### Display version

```bash
ruby [-v|--version]
```
