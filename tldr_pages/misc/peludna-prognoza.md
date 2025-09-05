# peludna-prognoza

> Fetch pollen measurement data for Croatian cities from your terminal using Pliva's allergies data API. More information: <https://github.com/vladimyr/peludna-prognoza>.

## Examples

### Start an interactive search for a city and fetch data for it

```bash
peludna-prognoza
```

### Fetch data for a city

```bash
peludna-prognoza "city"
```

### Display data in a machine-readable format

```bash
peludna-prognoza "city" --json|xml
```

### Display the pollen measurement page for a city at <https://plivazdravlje.hr> in the default web browser

```bash
peludna-prognoza "city" [-w|--web]
```
