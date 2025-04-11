#!/usr/bin/env python3
"""
FDX to Plain Text Converter

This example demonstrates how to convert an FDX screenplay file to a plain text format.
It preserves the basic structure of the screenplay but removes FDX-specific formatting.
"""

import os
import sys
from fdx import read_fdx, FDXException


def format_paragraph(paragraph):
    """Format a paragraph based on its type."""
    text = paragraph.plain_text.strip()

    if not text:
        return ""

    paragraph_type = paragraph.paragraph_type

    if paragraph_type == "Scene Heading":
        return f"\n{text}\n"
    elif paragraph_type == "Character":
        return f"\n{text}"
    elif paragraph_type == "Dialogue":
        return f"    {text}\n"
    elif paragraph_type == "Parenthetical":
        return f"  ({text})"
    elif paragraph_type == "Transition":
        return f"\n{text}\n"
    else:  # Action, General, etc.
        return f"{text}\n"


def fdx_to_text(fdx_path, output_path=None):
    """Convert an FDX file to plain text."""
    try:
        screenplay = read_fdx(fdx_path)
    except FDXException as e:
        print(f"Error reading FDX file: {e}")
        return None

    # Convert each paragraph to formatted text
    text_content = []
    for paragraph in screenplay.paragraphs:
        text_content.append(format_paragraph(paragraph))

    # Join all parts with appropriate spacing
    full_text = "".join(text_content)

    # Save to file if output path is provided
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_text)
        print(f"Converted screenplay saved to: {output_path}")

    return full_text


def main():
    if len(sys.argv) < 2:
        print("Usage: python fdx_to_text.py <fdx_file> [output_file]")
        return

    fdx_path = sys.argv[1]
    if not os.path.exists(fdx_path):
        print(f"Error: File {fdx_path} not found.")
        return

    # Determine output path (default is replacing .fdx extension with .txt)
    output_path = None
    if len(sys.argv) > 2:
        output_path = sys.argv[2]
    else:
        base_name = os.path.splitext(fdx_path)[0]
        output_path = f"{base_name}.txt"

    # Convert FDX to text
    text_content = fdx_to_text(fdx_path, output_path)

    if not text_content:
        print("Conversion failed.")
        return

    # Print a sample of the converted text (first 500 characters)
    print("\nSample of converted text:")
    print("-" * 40)
    print(text_content[:500] + "...")
    print("-" * 40)


if __name__ == "__main__":
    main()
