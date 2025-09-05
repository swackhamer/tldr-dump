# safeejectgpu

> Eject a GPU safely. More information: <https://keith.github.io/xcode-man-pages/SafeEjectGPU.8.html>.

## Examples

### Eject all GPUs

```bash
SafeEjectGPU Eject
```

### List all GPUs attached

```bash
SafeEjectGPU gpus
```

### List apps using a GPU

```bash
SafeEjectGPU gpuid GPU_ID apps
```

### Get the status of a GPU

```bash
SafeEjectGPU gpuid GPU_ID status
```

### Eject a GPU

```bash
SafeEjectGPU gpuid GPU_ID Eject
```

### Launch an app on a GPU

```bash
SafeEjectGPU gpuid GPU_ID LaunchOnGPU path/to/App.app
```
