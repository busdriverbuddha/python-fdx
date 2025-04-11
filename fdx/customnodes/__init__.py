"""Custom node types for the FDX package.

This module contains custom node types that provide higher-level functionality
not directly mapped to elements in the FDX XML structure, such as scenes
composed of multiple paragraphs.
"""

from .scene import Scene

__all__ = ["Scene"]
