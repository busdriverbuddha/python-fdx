"""Final Draft node classes that directly represent FDX XML elements.

This module contains classes that directly map to elements in the FDX XML structure.
These are the core building blocks for working with FDX content:

- FDXNode: Base class for all FDX elements
- FinalDraft: The root element of an FDX file
- Content: Contains all screenplay content
- Paragraph: Represents a paragraph element (scene heading, action, character, dialogue, etc.)
"""

from .fdx_node import FDXNode
from .final_draft import FinalDraft
from .content import Content
from .paragraph import Paragraph

__all__ = ["Content", "FinalDraft", "Paragraph", "FDXNode"]
