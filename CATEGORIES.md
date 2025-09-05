# Categories Documentation

This document describes the categorization logic used to organize tldr commands into folders.

## Category List

The script automatically categorizes 4,177+ commands into the following 26 categories:

| Category | Count | Description | Key Patterns |
|----------|-------|-------------|--------------|
| **android** | 12 | Android development tools | `adb`, `fastboot`, `aapt`, `apktool` |
| **build-tools** | 32 | Build automation and compilation | `make`, `cmake`, `gradle`, `maven`, `bazel` |
| **cloud** | 116 | Cloud provider CLIs | `aws`, `gcloud`, `az`, cloud platforms |
| **compression** | 85 | Archive and compression tools | `zip`, `tar`, `gzip`, `7z`, `rar` |
| **containers** | 80 | Container and orchestration | `docker`, `kubectl`, `podman`, `helm` |
| **data-science** | 3 | Data science and ML tools | `jupyter`, `pandas`, `tensorflow` |
| **databases** | 38 | Database management | `mysql`, `postgres`, `mongo`, `redis` |
| **editors** | 138 | Text editors and IDEs | `vim`, `emacs`, `nano`, `code` |
| **file-operations** | 525 | File and directory management | `ls`, `cp`, `mv`, `find`, `grep` |
| **git** | 191 | Git version control | `git-*` commands, `git` |
| **ios** | 2 | iOS development | `xcode`, `swift`, `cocoapods` |
| **linux** | 63 | Linux-specific tools | `systemd`, `journald`, `ufw` |
| **macos** | 16 | macOS-specific tools | `brew`, `defaults`, `osascript` |
| **media** | 225 | Image, audio, video tools | `ffmpeg`, `convert`, `imagemagick` |
| **misc** | 1501 | Uncategorized commands | Various tools |
| **network** | 218 | Networking utilities | `curl`, `ssh`, `ping`, `nmap` |
| **package-managers** | 130 | Package management | `apt`, `npm`, `pip`, `cargo` |
| **programming** | 171 | Programming languages | `python`, `node`, `ruby`, `go` |
| **security** | 59 | Security and encryption | `gpg`, `openssl`, `ssh-keygen` |
| **shell** | 94 | Shell built-ins and features | `!`, `$`, `[`, `bash`, `zsh` |
| **system** | 63 | System utilities | General system tools |
| **system-monitoring** | 253 | Monitoring and diagnostics | `top`, `htop`, `ps`, `iostat` |
| **text-processing** | 188 | Text manipulation | `sed`, `awk`, `cut`, `sort` |
| **version-control** | 24 | Non-git VCS | `svn`, `hg`, `cvs` |
| **virtualization** | 3 | VM management | `vagrant`, `virtualbox`, `qemu` |
| **web-servers** | 5 | Web server software | `apache`, `nginx`, `caddy` |
| **windows** | 5 | Windows-specific | `wmic`, `powershell`, `winget` |

## Categorization Logic

The `determine_category()` function uses a priority-based system to categorize commands:

### 1. Priority Order

Categories are checked in a specific order to ensure accurate classification:

1. **Git commands** - Highest priority for `git-*` pattern
2. **Container tools** - Docker ecosystem commands
3. **Cloud providers** - AWS, GCP, Azure CLIs
4. **Package managers** - System and language package tools
5. **Programming languages** - Language-specific tools
6. ... (continuing through all categories)
7. **Misc** - Default fallback category

### 2. Detection Methods

#### Pattern Matching in Command Name

```python
# Git commands
if cmd_lower.startswith('git-') or cmd_lower == 'git':
    return 'git'

# Docker/Container commands
if any(x in cmd_lower for x in ['docker', 'podman', 'kubectl']):
    return 'containers'
```

#### Description Analysis

```python
# Network tools (also checks description)
if 'network' in desc_lower:
    return 'network'

# Media tools (checks for media-related terms)
if any(x in desc_lower for x in ['image', 'video', 'audio']):
    return 'media'
```

#### Special Character Handling

Shell built-ins and special characters get dedicated handling:

```python
# Shell-specific characters
if cmd_lower in ['!', '$', '%', '.', '[', '[[', ']', ']]']:
    return 'shell'
```

### 3. Category Rules

#### git (191 commands)
- Pattern: `git-*` or exactly `git`
- Examples: `git`, `git-add`, `git-commit`, `git-flow`

#### containers (80 commands)
- Keywords: `docker`, `podman`, `kubectl`, `k8s`, `helm`
- Examples: `docker`, `docker-compose`, `kubectl`, `helm`

#### cloud (116 commands)
- Patterns: `aws*`, `az*`, `gcloud*`
- Examples: `aws`, `aws-s3`, `gcloud`, `azure-cli`

#### file-operations (525 commands)
- Keywords: Basic file commands
- Examples: `ls`, `cp`, `mv`, `rm`, `find`, `locate`

#### network (218 commands)
- Keywords: Network tools and protocols
- Examples: `curl`, `wget`, `ssh`, `ping`, `netstat`

#### programming (171 commands)
- Language names: `python`, `node`, `ruby`, `rust`, `java`
- Examples: `python`, `pip`, `node`, `npm`, `cargo`

#### system-monitoring (253 commands)
- Keywords: Monitoring and process tools
- Examples: `top`, `htop`, `ps`, `free`, `iostat`

#### security (59 commands)
- Keywords: Encryption and security tools
- Examples: `gpg`, `openssl`, `pass`, `ssh-keygen`

#### media (225 commands)
- Keywords: Media formats and tools
- Examples: `ffmpeg`, `convert`, `mp3`, `jpg`, `pdf`

#### text-processing (188 commands)
- Keywords: Text manipulation utilities
- Examples: `sed`, `awk`, `grep`, `cut`, `sort`

## Adding Custom Categories

To add a new category, edit the `determine_category()` function:

```python
def determine_category(command: str, description: str) -> str:
    cmd_lower = command.lower()
    desc_lower = description.lower() if description else ""
    
    # Add your custom category (add before misc)
    if 'mycriteria' in cmd_lower:
        return 'my-category'
    
    # ... rest of the function
```

### Best Practices for Custom Categories

1. **Be Specific**: Use clear, specific patterns
2. **Order Matters**: Place more specific rules before general ones
3. **Test Patterns**: Check for false positives
4. **Document Rules**: Add comments explaining the logic

Example custom category:

```python
# DevOps tools category
if any(x in cmd_lower for x in ['terraform', 'ansible', 'puppet', 'chef']):
    return 'devops'

# Scientific computing
if any(x in cmd_lower for x in ['matlab', 'octave', 'r', 'julia']):
    return 'scientific'
```

## Category Statistics

Based on current categorization (4,177 total commands):

- **Largest**: `misc` (1,501 commands, 36%)
- **Smallest**: `ios` (2 commands, 0.05%)
- **Most specific**: `git` (191 commands, all git-related)
- **Most diverse**: `file-operations` (525 commands, various file tools)

### Coverage Analysis

- **Well-categorized**: 2,676 commands (64%)
- **Misc (needs refinement)**: 1,501 commands (36%)

## Improving Categorization

### Current Limitations

1. **Misc category is large**: 36% of commands
2. **Some overlap**: Commands could fit multiple categories
3. **Platform-specific**: Some commands are OS-specific

### Potential Improvements

1. **Sub-categories**: Add nested categories (e.g., `network/http`, `network/dns`)
2. **Multi-category**: Allow commands in multiple categories
3. **AI-based**: Use NLP for better description analysis
4. **Community input**: Crowdsource categorization improvements

## File Naming

Special characters in command names are converted:

| Original | Converted | Example |
|----------|-----------|---------|
| `/` | `-` | `a/b` → `a-b.md` |
| `$` | `dollar` | `$` → `dollar.md` |
| `!` | `bang` | `!` → `bang.md` |
| `[` | `lbracket` | `[` → `lbracket.md` |
| `.` | `dot` | `.` → `dot.md` |

## Future Enhancements

1. **Machine Learning**: Train a classifier on command descriptions
2. **Hierarchical Categories**: Implement parent-child relationships
3. **Tag System**: Multiple tags per command
4. **User Preferences**: Allow custom categorization rules
5. **Dynamic Categories**: Auto-generate based on patterns