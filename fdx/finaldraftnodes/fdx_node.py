from xml.etree.ElementTree import Element


class FDXNode:
    """Base class for all FDX XML elements.

    This is the foundational class for all FDX nodes. It provides common functionality
    for handling XML attributes, child nodes, and conversion back to XML.

    Attributes:
        tag: The XML tag name for this node.
        children: List of child FDXNode objects.
        xml_attrib: Dictionary of XML attributes for this node.
        xml_text: The text content of this node (not including children).
    """

    def __init__(self, xml_attrib: dict[str, str], tag: str):
        """Initialize an FDXNode.

        Args:
            xml_attrib: Dictionary of XML attributes.
            tag: The XML tag name.
        """
        self.tag: str = tag
        self.children: list[FDXNode] = []
        self.xml_attrib: dict[str, str] = xml_attrib
        self.xml_text: str = ""

    def __repr__(self):
        """Return a string representation of the node.

        Returns:
            A string in the format "FDXNode: {tag}".
        """
        return f"FDXNode: {self.tag}"

    def __iter__(self):
        """Allow iteration over the node's children.

        Returns:
            An iterator over the children list.
        """
        return iter(self.children)

    def __getitem__(self, index: int) -> "FDXNode":
        """Access a child node by index.

        Args:
            index: The index of the child node to retrieve.

        Returns:
            The child FDXNode at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        return self.children[index]

    def __len__(self) -> int:
        """Get the number of child nodes.

        Returns:
            The number of children this node has.
        """
        return len(self.children)

    def to_element(self) -> Element:
        """Convert the FDXNode back to an XML element.

        This recursively converts this node and all its children to
        ElementTree.Element objects for XML serialization.

        Returns:
            An ElementTree.Element representing this node and its children.
        """
        element: Element = Element(self.tag, self.xml_attrib)
        element.text = self.xml_text
        for child in self.children:
            element.append(child.to_element())
        return element
