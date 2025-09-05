# ollama

> A large language model runner. For a list of available models, see <https://ollama.com/library>. More information: <https://github.com/ollama/ollama>.

## Examples

### Start the daemon required to run other commands

```bash
ollama serve
```

### Run a model and chat with it

```bash
ollama run model
```

### Run a model with a single prompt

```bash
ollama run model prompt
```

### List downloaded models

```bash
ollama list
```

### Pull a specific model

```bash
ollama pull model
```

### List running models

```bash
ollama ps
```

### Delete a model

```bash
ollama rm model
```

### Create a model from a `Modelfile`

```bash
ollama create new_model_name [-f|--file] path/to/Modelfile
```
