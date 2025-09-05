#!/usr/bin/env python3
"""
Script to export all tldr pages to individual markdown files organized by category.
Uses tealdeer's tldr command to fetch and format all available pages.
"""

import subprocess
import re
import sys
import os
from typing import List, Tuple, Optional, Dict
import argparse
from pathlib import Path


def get_all_commands() -> List[str]:
    """Get list of all available tldr commands."""
    try:
        result = subprocess.run(
            ['tldr', '--list'],
            capture_output=True,
            text=True,
            check=True
        )
        commands = result.stdout.strip().split('\n')
        return [cmd.strip() for cmd in commands if cmd.strip()]
    except subprocess.CalledProcessError as e:
        print(f"Error getting command list: {e}", file=sys.stderr)
        return []
    except FileNotFoundError:
        print("Error: tldr (tealdeer) is not installed", file=sys.stderr)
        sys.exit(1)


def get_tldr_page(command: str) -> Optional[str]:
    """Get tldr page content for a specific command."""
    try:
        result = subprocess.run(
            ['tldr', command],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError:
        return None


def parse_tldr_output(content: str) -> Tuple[str, List[Tuple[str, str]]]:
    """
    Parse tldr output into description and examples.
    Returns: (description, [(description, command), ...])
    """
    lines = content.strip().split('\n')
    
    description = ""
    examples = []
    current_example_desc = []
    
    i = 0
    # Get main description (first lines before examples)
    while i < len(lines) and not lines[i].strip().endswith(':'):
        if lines[i].strip():
            description += lines[i].strip() + " "
        i += 1
    
    description = description.strip()
    
    # Parse examples
    while i < len(lines):
        line = lines[i].strip()
        
        if line.endswith(':'):
            # This is an example description
            current_example_desc = [line[:-1]]  # Remove colon
        elif line and current_example_desc:
            # This is the command for the current example
            if not line.startswith('More information:'):
                examples.append((' '.join(current_example_desc), line))
            current_example_desc = []
        
        i += 1
    
    return description, examples


def determine_category(command: str, description: str) -> str:
    """
    Determine the category of a command based on its name and description.
    """
    cmd_lower = command.lower()
    desc_lower = description.lower() if description else ""
    
    # Priority-based categorization (check in order)
    
    # Git commands
    if cmd_lower.startswith('git-') or cmd_lower == 'git':
        return 'git'
    
    # Docker/Container commands
    if any(x in cmd_lower for x in ['docker', 'podman', 'kubectl', 'k8s', 'k3s', 'helm']):
        return 'containers'
    
    # Cloud provider commands
    if cmd_lower.startswith('aws') or cmd_lower.startswith('az') or cmd_lower.startswith('gcloud'):
        return 'cloud'
    
    # Package managers
    if any(x in cmd_lower for x in ['apt', 'yum', 'dnf', 'brew', 'npm', 'pip', 'cargo', 'gem', 'composer', 'yarn', 'pnpm', 'pacman', 'zypper', 'snap', 'flatpak']):
        return 'package-managers'
    
    # Programming languages and tools
    if any(x in cmd_lower for x in ['python', 'node', 'ruby', 'rust', 'java', 'kotlin', 'swift', 'go', 'php', 'perl', 'lua', 'scala', 'clojure', 'elixir', 'crystal', 'nim', 'zig']):
        return 'programming'
    
    # Database tools
    if any(x in cmd_lower for x in ['sql', 'postgres', 'mysql', 'mongo', 'redis', 'cassandra', 'sqlite', 'mariadb', 'influx', 'elastic']):
        return 'databases'
    
    # Network tools
    if any(x in cmd_lower for x in ['ping', 'netstat', 'nmap', 'curl', 'wget', 'ssh', 'scp', 'sftp', 'telnet', 'dig', 'nslookup', 'traceroute', 'ifconfig', 'ip', 'iptables', 'tcpdump', 'wireshark']) or 'network' in desc_lower:
        return 'network'
    
    # System monitoring and process management
    if any(x in cmd_lower for x in ['top', 'htop', 'ps', 'kill', 'systemctl', 'service', 'journalctl', 'dmesg', 'uptime', 'free', 'df', 'du', 'iostat', 'vmstat', 'sar']):
        return 'system-monitoring'
    
    # File and directory operations
    if any(x in cmd_lower for x in ['ls', 'cd', 'cp', 'mv', 'rm', 'mkdir', 'touch', 'cat', 'head', 'tail', 'grep', 'find', 'locate', 'which', 'whereis', 'file', 'stat', 'chmod', 'chown', 'ln']) or cmd_lower.endswith('dir'):
        return 'file-operations'
    
    # Compression and archives
    if any(x in cmd_lower for x in ['zip', 'tar', 'gzip', 'bzip', '7z', 'rar', 'compress', 'extract']) or 'compress' in desc_lower or 'archive' in desc_lower:
        return 'compression'
    
    # Text processing
    if any(x in cmd_lower for x in ['sed', 'awk', 'cut', 'sort', 'uniq', 'wc', 'diff', 'patch', 'tr', 'fold', 'column', 'paste', 'join', 'comm', 'tee', 'xargs']):
        return 'text-processing'
    
    # Editors
    if any(x in cmd_lower for x in ['vim', 'emacs', 'nano', 'vi', 'ed', 'pico', 'code', 'subl', 'atom']):
        return 'editors'
    
    # Security tools
    if any(x in cmd_lower for x in ['gpg', 'pgp', 'openssl', 'pass', 'vault', 'keychain', 'ssh-', 'keygen', 'encrypt', 'decrypt']) or 'security' in desc_lower or 'encryption' in desc_lower:
        return 'security'
    
    # Web servers and tools
    if any(x in cmd_lower for x in ['apache', 'nginx', 'caddy', 'httpd', 'lighttpd']):
        return 'web-servers'
    
    # Build tools
    if any(x in cmd_lower for x in ['make', 'cmake', 'gradle', 'maven', 'ant', 'bazel', 'scons', 'meson', 'ninja']):
        return 'build-tools'
    
    # Version control (non-git)
    if any(x in cmd_lower for x in ['svn', 'hg', 'mercurial', 'bzr', 'cvs', 'fossil', 'perforce']):
        return 'version-control'
    
    # Media tools
    if any(x in cmd_lower for x in ['ffmpeg', 'convert', 'mogrify', 'identify', 'mp3', 'mp4', 'jpg', 'png', 'gif', 'svg', 'pdf', 'imagemagick', 'sox', 'vlc', 'mpv', 'mplayer']) or any(x in desc_lower for x in ['image', 'video', 'audio', 'media']):
        return 'media'
    
    # Shell-specific
    if cmd_lower in ['!', '$', '%', '.', '[', '[[', ']', ']]', '^', '{', '}', '~'] or any(x in cmd_lower for x in ['bash', 'zsh', 'fish', 'shell', 'sh']):
        return 'shell'
    
    # macOS specific
    if cmd_lower.startswith('osx-') or any(x in cmd_lower for x in ['brew', 'defaults', 'launchctl', 'osascript', 'pbcopy', 'pbpaste', 'open', 'mdfind', 'mdls', 'ditto']):
        return 'macos'
    
    # Windows specific
    if any(x in cmd_lower for x in ['wmic', 'powershell', 'cmd', 'reg', 'netsh', 'sfc', 'dism', 'choco', 'scoop', 'winget']):
        return 'windows'
    
    # Linux specific
    if any(x in cmd_lower for x in ['systemd', 'journald', 'ufw', 'firewalld', 'selinux', 'apparmor']):
        return 'linux'
    
    # Android tools
    if any(x in cmd_lower for x in ['adb', 'fastboot', 'aapt', 'apktool', 'android']):
        return 'android'
    
    # iOS/Apple development
    if any(x in cmd_lower for x in ['xcode', 'swift', 'cocoapods', 'carthage', 'fastlane']):
        return 'ios'
    
    # Data science / ML
    if any(x in cmd_lower for x in ['jupyter', 'pandas', 'numpy', 'scikit', 'tensorflow', 'pytorch', 'keras']):
        return 'data-science'
    
    # Game development
    if any(x in cmd_lower for x in ['unity', 'unreal', 'godot', 'love2d', 'pygame']):
        return 'gamedev'
    
    # Virtualization
    if any(x in cmd_lower for x in ['vagrant', 'virtualbox', 'vmware', 'qemu', 'kvm', 'virt-']):
        return 'virtualization'
    
    # Check description for hints
    if description:
        if 'file' in desc_lower or 'directory' in desc_lower:
            return 'file-operations'
        if 'network' in desc_lower or 'connection' in desc_lower:
            return 'network'
        if 'system' in desc_lower:
            return 'system'
        if 'text' in desc_lower or 'string' in desc_lower:
            return 'text-processing'
    
    # Default category
    return 'misc'


def format_as_markdown(command: str, description: str, examples: List[Tuple[str, str]]) -> str:
    """Format a command's information as markdown."""
    md_lines = []
    
    # Command header
    md_lines.append(f"# {command}")
    md_lines.append("")
    
    # Description
    if description:
        md_lines.append(f"> {description}")
        md_lines.append("")
    
    # Examples
    if examples:
        md_lines.append("## Examples")
        md_lines.append("")
        
        for example_desc, example_cmd in examples:
            if example_desc:
                md_lines.append(f"### {example_desc}")
                md_lines.append("")
            md_lines.append("```bash")
            md_lines.append(example_cmd)
            md_lines.append("```")
            md_lines.append("")
    
    return '\n'.join(md_lines)


def sanitize_filename(filename: str) -> str:
    """Sanitize a filename to be filesystem-safe."""
    # Replace problematic characters
    replacements = {
        '/': '-',
        '\\': '-',
        ':': '-',
        '*': 'star',
        '?': 'q',
        '"': '',
        '<': 'lt',
        '>': 'gt',
        '|': 'pipe',
        '$': 'dollar',
        '!': 'bang',
        '%': 'percent',
        '^': 'caret',
        '&': 'and',
        '[': 'lbracket',
        ']': 'rbracket',
        '{': 'lbrace',
        '}': 'rbrace',
        '~': 'tilde',
        '.': 'dot',
        ',': 'comma'
    }
    
    for old, new in replacements.items():
        filename = filename.replace(old, new)
    
    # Handle special single-character commands
    if len(filename) == 1 and not filename.isalnum():
        special_names = {
            '.': 'dot',
            ',': 'comma',
            '!': 'bang',
            '$': 'dollar',
            '%': 'percent',
            '^': 'caret',
            '&': 'ampersand',
            '*': 'star',
            '(': 'lparen',
            ')': 'rparen',
            '-': 'dash',
            '_': 'underscore',
            '=': 'equals',
            '+': 'plus',
            '[': 'lbracket',
            ']': 'rbracket',
            '{': 'lbrace',
            '}': 'rbrace',
            '\\': 'backslash',
            '|': 'pipe',
            ';': 'semicolon',
            ':': 'colon',
            "'": 'apostrophe',
            '"': 'quote',
            '<': 'lt',
            '>': 'gt',
            '/': 'slash',
            '?': 'question',
            '~': 'tilde',
            '`': 'backtick'
        }
        filename = special_names.get(filename, filename)
    
    return filename


def main():
    parser = argparse.ArgumentParser(description='Export all tldr pages to categorized markdown files')
    parser.add_argument('-o', '--output', default='tldr_pages',
                        help='Output directory (default: tldr_pages)')
    parser.add_argument('-l', '--limit', type=int, default=None,
                        help='Limit number of commands to process (for testing)')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Show progress')
    parser.add_argument('--index', action='store_true',
                        help='Create index files for each category')
    
    args = parser.parse_args()
    
    # Create output directory
    output_dir = Path(args.output)
    output_dir.mkdir(exist_ok=True)
    
    # Get all commands
    if args.verbose:
        print("Fetching list of all commands...")
    
    commands = get_all_commands()
    
    if not commands:
        print("No commands found", file=sys.stderr)
        sys.exit(1)
    
    total_commands = len(commands)
    if args.limit:
        commands = commands[:args.limit]
    
    print(f"Processing {len(commands)} of {total_commands} commands...")
    
    # Track categories and their commands
    categories: Dict[str, List[Tuple[str, str]]] = {}
    
    successful = 0
    failed = []
    
    for i, command in enumerate(commands, 1):
        if args.verbose and i % 100 == 0:
            print(f"Processing {i}/{len(commands)}: {command}")
        
        content = get_tldr_page(command)
        
        if content:
            description, examples = parse_tldr_output(content)
            category = determine_category(command, description)
            
            # Create category directory
            category_dir = output_dir / category
            category_dir.mkdir(exist_ok=True)
            
            # Track for index
            if category not in categories:
                categories[category] = []
            categories[category].append((command, description))
            
            # Format and write markdown
            markdown = format_as_markdown(command, description, examples)
            
            # Sanitize filename
            safe_filename = sanitize_filename(command)
            file_path = category_dir / f"{safe_filename}.md"
            
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(markdown)
                successful += 1
            except Exception as e:
                print(f"Error writing {command}: {e}", file=sys.stderr)
                failed.append(command)
        else:
            failed.append(command)
    
    # Create index files if requested
    if args.index:
        print("\nCreating index files...")
        
        # Main index
        main_index_path = output_dir / "README.md"
        with open(main_index_path, 'w', encoding='utf-8') as f:
            f.write("# TLDR Pages Collection\n\n")
            f.write(f"Collection of {successful} command examples from tldr-pages, organized by category.\n\n")
            f.write("## Categories\n\n")
            
            for category in sorted(categories.keys()):
                count = len(categories[category])
                f.write(f"- [{category}](./{category}/) ({count} commands)\n")
        
        # Category indexes
        for category, commands in categories.items():
            category_index_path = output_dir / category / "README.md"
            with open(category_index_path, 'w', encoding='utf-8') as f:
                f.write(f"# {category.replace('-', ' ').title()}\n\n")
                f.write(f"{len(commands)} commands in this category.\n\n")
                f.write("## Commands\n\n")
                
                for cmd, desc in sorted(commands):
                    safe_filename = sanitize_filename(cmd)
                    desc_short = desc[:100] + "..." if len(desc) > 100 else desc
                    f.write(f"- [{cmd}](./{safe_filename}.md)")
                    if desc_short:
                        f.write(f" - {desc_short}")
                    f.write("\n")
    
    # Summary
    print(f"\nSummary:")
    print(f"  Successfully processed: {successful} commands")
    print(f"  Failed: {len(failed)} commands")
    print(f"  Categories created: {len(categories)}")
    
    if categories and args.verbose:
        print(f"\nCategory breakdown:")
        for category in sorted(categories.keys()):
            print(f"  {category}: {len(categories[category])} commands")
    
    if failed and args.verbose:
        print(f"\nFailed commands: {', '.join(failed[:10])}")
        if len(failed) > 10:
            print(f"    ... and {len(failed) - 10} more")
    
    print(f"\nOutput written to: {output_dir}/")


if __name__ == "__main__":
    main()