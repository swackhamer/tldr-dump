# sonar-scanner

> A generic scanner for SonarQube projects that do not use build tools such as Maven, Gradle, or Ant. More information: <https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/>.

## Examples

### Scan a project with configuration file in your project's root directory named `sonar-project.properties`

```bash
sonar-scanner
```

### Scan a project using configuration file other than `sonar-project.properties`

```bash
sonar-scanner [-D|--define] project.settings=myproject.properties
```

### Print debugging information

```bash
sonar-scanner [-X|--debug]
```

### Display help

```bash
sonar-scanner [-h|--help]
```
