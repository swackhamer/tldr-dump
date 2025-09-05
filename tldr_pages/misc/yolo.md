# yolo

> Train, validate or infer models on various tasks and versions. More information: <https://docs.ultralytics.com/cli/>.

## Examples

### Create a copy of the default configuration in your current working directory

```bash
yolo task=init
```

### Train the object detection, instance segment, or classification model with the specified configuration file

```bash
yolo task=detect|segment|classify mode=train cfg=path/to/config.yaml
```
