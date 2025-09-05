# packwiz

> Create, edit and manage Minecraft modpacks. More information: <https://packwiz.infra.link/reference/commands/packwiz/>.

## Examples

### Interactively create a new modpack in the current directory

```bash
packwiz init
```

### Add a mod from Modrinth or Curseforge

```bash
packwiz modrinth|curseforge add url|slug|search_term
```

### List all mods in the modpack

```bash
packwiz list
```

### Update `index.toml` after manually editing files

```bash
packwiz refresh
```

### Export as a Modrinth (`.mrpack`) or Curseforge (Zip) file

```bash
packwiz modrinth|curseforge export
```
