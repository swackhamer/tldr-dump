# bundle

> Dependency manager for the Ruby programming language. More information: <https://bundler.io/man/bundle.1.html>.

## Examples

### Install all gems defined in the `Gemfile` expected in the working directory

```bash
bundle install
```

### Execute a command in the context of the current bundle

```bash
bundle exec command arguments
```

### Update all gems by the rules defined in the `Gemfile` and regenerate `Gemfile.lock`

```bash
bundle update
```

### Update one or more specific gem(s) defined in the `Gemfile`

```bash
bundle update gem_name1 gem_name2
```

### Update one or more specific gems(s) defined in the `Gemfile` but only to the next patch version

```bash
bundle update --patch gem_name1 gem_name2
```

### Update all gems within the given group in the `Gemfile`

```bash
bundle update --group development
```

### List installed gems in the `Gemfile` with newer versions available

```bash
bundle outdated
```

### Create a new gem skeleton

```bash
bundle gem gem_name
```
