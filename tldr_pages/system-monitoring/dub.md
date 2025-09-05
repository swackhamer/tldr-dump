# dub

> Package manager for D packages. More information: <https://dub.pm/commandline>.

## Examples

### Interactively create a new D project

```bash
dub init project_name
```

### Non-interactively create a new D project

```bash
dub init project_name [-n|--non-interactive]
```

### Build and run a D project

```bash
dub
```

### Install dependencies specified in a D project's `dub.json` or `dub.sdl` file

```bash
dub fetch
```

### Update the dependencies in a D project

```bash
dub upgrade
```

### Display help

```bash
dub [-h|--help]
```
