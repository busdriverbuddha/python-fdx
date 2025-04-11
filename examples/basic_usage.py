#!/usr/bin/env python3
"""
Basic usage example for python-fdx

This example demonstrates how to:
1. Read an FDX file
2. Access and print paragraph content
3. Build and work with scenes
4. Make simple modifications
5. Save the modified script
"""

import os
import sys
from fdx import read_fdx, read_string_to_finaldraft, FDXException


# Sample FDX content for testing if no file is provided
SAMPLE_FDX = """<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<FinalDraft DocumentType="Script" Version="3">
    <Content>
        <Paragraph Type="Scene Heading">
            <Text>INT. COFFEE SHOP - DAY</Text>
        </Paragraph>
        <Paragraph Type="Action">
            <Text>A writer sits alone at a table, typing furiously on a laptop.</Text>
        </Paragraph>
        <Paragraph Type="Character">
            <Text>WRITER</Text>
        </Paragraph>
        <Paragraph Type="Dialogue">
            <Text>This library makes working with FDX files so simple!</Text>
        </Paragraph>
        <Paragraph Type="Scene Heading">
            <Text>EXT. PARK - SUNSET</Text>
        </Paragraph>
        <Paragraph Type="Action">
            <Text>The writer walks through the park, relaxed and content.</Text>
        </Paragraph>
    </Content>
</FinalDraft>"""


def main():
    # Check if a filename was provided
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        filename = sys.argv[1]
        print(f"Reading FDX file: {filename}")
        try:
            screenplay = read_fdx(filename)
        except FDXException as e:
            print(f"Error reading file: {e}")
            return
    else:
        # Use the sample FDX content
        print("No file provided or file not found. Using sample FDX content.")
        screenplay = read_string_to_finaldraft(SAMPLE_FDX)

    # Print basic information
    print("\n=== Screenplay Paragraphs ===")
    for i, paragraph in enumerate(screenplay.paragraphs):
        print(f"{i+1}. Type: {paragraph.paragraph_type}")
        print(f"   Text: {paragraph.plain_text}")

    # Build and work with scenes
    screenplay.build_scenes()

    print("\n=== Screenplay Scenes ===")
    for i, scene in enumerate(screenplay.scenes):
        print(f"Scene {i+1}:")
        print(f"  Is preamble: {scene.is_preamble}")
        print(f"  First paragraph type: {scene.paragraphs[0].paragraph_type}")
        print(f"  Scene text (first 50 chars): {scene.plain_text[:50]}...")

    # Modify the screenplay (simple example: add a new paragraph)
    if screenplay.content:
        from fdx.finaldraftnodes import Paragraph
        from xml.etree.ElementTree import Element
        from fdx.finaldraftnodes import FDXNode

        # Create a new paragraph
        new_paragraph = Paragraph({"Type": "Action"})
        new_paragraph.xml_text = ""

        # Create Text element for the paragraph
        text_element = Element("Text")
        text_element.text = "THE END."

        # Add the Text element to the paragraph
        text_node = FDXNode({}, tag="Text")
        text_node.xml_text = "THE END."
        new_paragraph.children.append(text_node)

        # Add the paragraph to the screenplay
        screenplay.content.children.append(new_paragraph)

        print("\n=== Added new paragraph ===")
        print(f"New paragraph type: {new_paragraph.paragraph_type}")
        print(f"New paragraph text: {new_paragraph.plain_text}")

    # Save the modified screenplay to a new file
    output_file = "modified_screenplay.fdx"
    screenplay.save_fdx(output_file)
    print(f"\nSaved modified screenplay to: {output_file}")


if __name__ == "__main__":
    main()
