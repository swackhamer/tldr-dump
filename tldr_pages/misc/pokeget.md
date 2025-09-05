# pokeget

> Display sprites of Pokemon in your terminal. More information: <https://github.com/talwat/pokeget-rs>.

## Examples

### Print a sprite of a given pokemon

```bash
pokeget pokemon_name
```

### Print Mr. Mime (note the use of `-` instead of spaces)

```bash
pokeget mr-mime
```

### Print Mega Gengar

```bash
pokeget gengar [-m|--mega]
```

### Print a random shiny Pokemon

```bash
pokeget random [-s|--shiny]
```

### Print Alolan Meowth, without printing the Pokemon's name

```bash
pokeget meowth [-a|--alolan] --hide-name
```

### Print a random Pokemon with 1/4096 chance to be shiny

```bash
((RANDOM%4096 == 0)) && pokeget random --shiny || pokeget random
```
