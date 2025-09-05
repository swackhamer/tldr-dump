# jupytext

> Convert Jupyter notebooks to plain text documents, and back again. More information: <https://jupytext.readthedocs.io>.

## Examples

### Turn a notebook into a paired `.ipynb`/`.py` notebook

```bash
jupytext --set-formats ipynb,py notebook.ipynb
```

### Convert a notebook to a `.py` file

```bash
jupytext --to py notebook.ipynb
```

### Convert a `.py` file to a notebook with no outputs

```bash
jupytext --to notebook notebook.py
```

### Convert a `.md` file to a notebook and run it

```bash
jupytext --to notebook --execute notebook.md
```

### Update the input cells in a notebook and preserve outputs and metadata

```bash
jupytext --update --to notebook notebook.py
```

### Update all paired representations of a notebook

```bash
jupytext --sync notebook.ipynb
```
