from fdx.finaldraftnodes.fdx_node import FDXNode


class Paragraph(FDXNode):
    """Represents a Paragraph element in an FDX file.

    Paragraphs are the basic building blocks of a screenplay and can be of various types:
    Scene Heading, Action, Character, Dialogue, Transition, etc. The type is determined
    by the "Type" attribute in the XML.

    Attributes:
        ALL_CAPS_TYPES: List of paragraph types that are traditionally displayed in all caps
            in screenplay formatting.
    """

    ALL_CAPS_TYPES = [
        'Scene Heading',
        'Transition',
        'Shot',
        'Character',
        # TODO: redo using ElementSettings
    ]

    def __init__(self, xml_attrib: dict[str, str]):
        """Initialize a Paragraph node.

        Args:
            xml_attrib: Dictionary of XML attributes, must contain a "Type" attribute
                that specifies the paragraph type.
        """
        super().__init__(xml_attrib, tag="Paragraph")

    def __repr__(self):
        """Return a string representation of the paragraph.

        Returns:
            A string in the format "Paragraph: {type}".
        """
        return f"Paragraph: {self.paragraph_type}"

    @property
    def paragraph_type(self) -> str:
        """Get the type of this paragraph.

        Returns:
            The paragraph type as specified in the "Type" attribute (e.g., "Scene Heading",
            "Action", "Character", "Dialogue").
        """
        return self.xml_attrib.get("Type")

    @property
    def plain_text(self) -> str:
        """Get the plain text content of the paragraph.

        This combines all Text child elements and applies formatting rules, such as
        converting certain paragraph types to all caps as per screenplay conventions.

        Returns:
            The formatted text content of the paragraph.
        """
        text: str = "".join(
            child.xml_text
            for child in self
            if child.tag == "Text"
        )
        if self.paragraph_type in self.ALL_CAPS_TYPES:
            return text.upper()
        else:
            return text
