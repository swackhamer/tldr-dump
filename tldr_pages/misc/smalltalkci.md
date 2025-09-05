# smalltalkci

> Framework for testing Smalltalk projects with GitHub Actions, Travis CI, AppVeyor, GitLab CI, and others. More information: <https://github.com/hpi-swa/smalltalkCI>.

## Examples

### Run tests for a configuration file

```bash
smalltalkci path/to/.smalltalk.ston
```

### Run tests for the `.smalltalk.ston` configuration in the current directory

```bash
smalltalkci
```

### Debug tests in headful mode (show VM window)

```bash
smalltalkci --headful
```

### Download and prepare a well-known smalltalk image for the tests

```bash
smalltalkci --smalltalk Squeak64-Trunk
```

### Specify a custom Smalltalk image and VM

```bash
smalltalkci --image path/to/Smalltalk.image --vm path/to/vm
```

### Clean up caches and delete builds

```bash
smalltalkci --clean
```
