# accelerate

> A library that enables the same PyTorch code to be run across any distributed configuration. More information: <https://huggingface.co/docs/accelerate/index>.

## Examples

### Print environment information

```bash
accelerate env
```

### Interactively create a configuration file

```bash
accelerate config
```

### Print the estimated GPU memory cost of running a Hugging Face model with different data types

```bash
accelerate estimate-memory name/model
```

### Test an Accelerate configuration file

```bash
accelerate test --config_file path/to/config.yaml
```

### Run a model on CPU with Accelerate

```bash
accelerate launch path/to/script.py --cpu
```

### Run a model on multi-GPU with Accelerate, with 2 machines

```bash
accelerate launch path/to/script.py --multi_gpu --num_machines 2
```
