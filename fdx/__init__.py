"""FDX interface library for Python.

This module provides tools to read, parse, manipulate, and save Final Draft (FDX) screenplay files.
FDX is an XML-based file format used by Final Draft, a screenwriting software.

Examples:
    Basic usage to read an FDX file:

    >>> from fdx import read_fdx
    >>> screenplay = read_fdx("screenplay.fdx")
    >>> for paragraph in screenplay.paragraphs:
    ...     print(paragraph.plain_text)

    Creating an FDX file from a string:

    >>> from fdx import read_string_to_finaldraft
    >>> fdx_string = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
    ... <FinalDraft DocumentType="Script" Version="3">
    ...     <Content>
    ...         <Paragraph Type="Scene Heading">
    ...             <Text>INT. ROOM - DAY</Text>
    ...         </Paragraph>
    ...     </Content>
    ... </FinalDraft>'''
    >>> screenplay = read_string_to_finaldraft(fdx_string)
"""

from .finaldraftnodes import (
    Content,
    FinalDraft,
    Paragraph,
    FDXNode,
)

from .customnodes import (
    Scene,
)

from .utils import read_fdx, read_string_to_finaldraft

from .core import FDXException

__all__ = [
    "Content",
    "FinalDraft",
    "Paragraph",
    "FDXNode",
    "Scene",
    "read_fdx",
    "read_string_to_finaldraft",
    "FDXException",
]
