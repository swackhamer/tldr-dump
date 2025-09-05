# pod

> Dependency manager for Swift and Objective-C Cocoa projects. More information: <https://guides.cocoapods.org/terminal/commands.html>.

## Examples

### Create a Podfile for the current project with the default contents

```bash
pod init
```

### Download and install all pods defined in the Podfile (that haven't been installed before)

```bash
pod install
```

### List all available pods

```bash
pod list
```

### Show the outdated pods (of those currently installed)

```bash
pod outdated
```

### Update all currently installed pods to their newest version

```bash
pod update
```

### Update a specific (previously installed) pod to its newest version

```bash
pod update pod_name
```

### Remove CocoaPods from a Xcode project

```bash
pod deintegrate xcode_project
```
