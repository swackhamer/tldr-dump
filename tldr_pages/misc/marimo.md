# marimo

> A reactive Python notebook environment. Combines features of Jupyter, Streamlit, and other notebook tools with reactive execution. More information: <https://docs.marimo.io/cli>.

## Examples

### Create or edit notebooks by starting a marimo server

```bash
marimo edit
```

### Start a marimo server on a specific port without launching a browser

```bash
marimo edit [-p|--port] port_number --headless
```

### Edit a specific notebook

```bash
marimo edit path/to/notebook.py
```

### Run a marimo notebook as an app in read-only mode

```bash
marimo run path/to/notebook.py
```

### Start an interactive tutorial to learn marimo

```bash
marimo tutorial intro|components|dataflow|io
```

### View command-specific help

```bash
marimo edit|run|tutorial|config|new|... --help
```
