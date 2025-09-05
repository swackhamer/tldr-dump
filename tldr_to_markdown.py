#!/usr/bin/env python3
"""
Script to export all tldr pages to a single markdown file.
Uses tealdeer's tldr command to fetch and format all available pages.
"""

import subprocess
import re
import sys
from typing import List, Tuple, Optional
import argparse


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


def format_as_markdown(command: str, description: str, examples: List[Tuple[str, str]]) -> str:
    """Format a command's information as markdown."""
    md_lines = []
    
    # Command header
    md_lines.append(f"## {command}")
    md_lines.append("")
    
    # Description
    if description:
        md_lines.append(description)
        md_lines.append("")
    
    # Examples
    if examples:
        md_lines.append("### Examples")
        md_lines.append("")
        
        for example_desc, example_cmd in examples:
            if example_desc:
                md_lines.append(f"**{example_desc}**")
                md_lines.append("")
            md_lines.append("```bash")
            md_lines.append(example_cmd)
            md_lines.append("```")
            md_lines.append("")
    
    return '\n'.join(md_lines)


def main():
    parser = argparse.ArgumentParser(description='Export all tldr pages to markdown')
    parser.add_argument('-o', '--output', default='tldr_pages.md',
                        help='Output markdown file (default: tldr_pages.md)')
    parser.add_argument('-l', '--limit', type=int, default=None,
                        help='Limit number of commands to process (for testing)')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Show progress')
    
    args = parser.parse_args()
    
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
    
    # Process each command
    markdown_sections = []
    markdown_sections.append("# TLDR Pages Collection")
    markdown_sections.append("")
    markdown_sections.append(f"Collection of {len(commands)} command examples from tldr-pages.")
    markdown_sections.append("")
    markdown_sections.append("---")
    markdown_sections.append("")
    
    successful = 0
    failed = []
    
    for i, command in enumerate(commands, 1):
        if args.verbose and i % 100 == 0:
            print(f"Processing {i}/{len(commands)}: {command}")
        
        content = get_tldr_page(command)
        
        if content:
            description, examples = parse_tldr_output(content)
            markdown = format_as_markdown(command, description, examples)
            markdown_sections.append(markdown)
            markdown_sections.append("---")
            markdown_sections.append("")
            successful += 1
        else:
            failed.append(command)
    
    # Write output
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write('\n'.join(markdown_sections))
    
    # Summary
    print(f"\nSummary:")
    print(f"  Successfully processed: {successful} commands")
    print(f"  Failed: {len(failed)} commands")
    if failed and args.verbose:
        print(f"  Failed commands: {', '.join(failed[:10])}")
        if len(failed) > 10:
            print(f"    ... and {len(failed) - 10} more")
    print(f"\nOutput written to: {args.output}")


if __name__ == "__main__":
    main()