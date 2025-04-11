# python-fdx

A Python library for parsing, manipulating, and saving Final Draft (FDX) screenplay files.

## Installation

```bash
git clone https://github.com/busdriverbuddha/python-fdx.git
pip install ./python-fdx
```

## Features

- Parse FDX files into Python objects
- Manipulate screenplay content programmatically
- Save modified screenplays back to FDX format
- Extract and work with screenplay elements (paragraphs, scenes, etc.)

## Usage Examples

### Opening an FDX file

```python
from fdx import read_fdx

# Open an FDX file
screenplay = read_fdx("my_screenplay.fdx")

# Access screenplay content
content = screenplay.content

# Get all paragraphs
paragraphs = screenplay.paragraphs

# Print the text of each paragraph
for paragraph in paragraphs:
    print(f"Type: {paragraph.paragraph_type}, Text: {paragraph.plain_text}")
```

### Working with Scenes

```python
from fdx import read_fdx

screenplay = read_fdx("my_screenplay.fdx")

# Build the scene objects
screenplay.build_scenes()

# Iterate through scenes
for i, scene in enumerate(screenplay.scenes):
    print(f"Scene {i+1}:")
    print(f"Is preamble: {scene.is_preamble}")
    print(f"Scene text: {scene.plain_text}")
    print("---")
```

### Creating a New Screenplay from a String

```python
from fdx import read_string_to_finaldraft

fdx_string = """<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<FinalDraft DocumentType="Script" Version="3">
    <Content>
        <Paragraph Type="Scene Heading">
            <Text>INT. LIVING ROOM - DAY</Text>
        </Paragraph>
        <Paragraph Type="Action">
            <Text>A character sits on the couch.</Text>
        </Paragraph>
    </Content>
</FinalDraft>"""

screenplay = read_string_to_finaldraft(fdx_string)
print(screenplay.paragraphs[0].plain_text)  # INT. LIVING ROOM - DAY
```

### Saving Changes to an FDX File

```python
from fdx import read_fdx

screenplay = read_fdx("my_screenplay.fdx")

# Make some changes to the screenplay
# ...

# Save the screenplay to a new file
screenplay.save_fdx("updated_screenplay.fdx")
```

## Class Structure

- `FDXNode`: Base class for all FDX elements
- `FinalDraft`: Represents a complete screenplay
- `Content`: Contains the screenplay content
- `Paragraph`: Represents a paragraph element (scene heading, action, character, dialogue, etc.)
- `Scene`: Custom class that groups paragraphs into logical scenes

## License

This project is licensed under the terms included in the LICENSE file.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
