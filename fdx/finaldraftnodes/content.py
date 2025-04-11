from fdx.finaldraftnodes.fdx_node import FDXNode
from fdx.finaldraftnodes.paragraph import Paragraph


class Content(FDXNode):
    """Represents the Content element in an FDX file.

    The Content element contains all the screenplay content, including paragraphs,
    scene headings, dialogue, and other elements that make up the screenplay text.

    This class provides methods for working with the content as a whole, such as
    cleaning empty paragraphs or filtering paragraphs by type.
    """

    def __init__(self, xml_attrib):
        """Initialize a Content node.

        Args:
            xml_attrib: Dictionary of XML attributes for this Content element.
        """
        super().__init__(xml_attrib, tag="Content")

    def clean_empty_paragraphs(self):
        """Remove empty paragraphs from the content.

        This method filters out any paragraph that has no visible text content.
        Useful for cleaning up the screenplay before saving or processing.
        """
        self.children = [p for p in self.children if p.plain_text.strip()]

    def get_paragraphs_by_type(self, type: str) -> list[Paragraph]:
        """Get all paragraphs of a specific type.

        Args:
            type: The paragraph type to filter by (e.g., "Scene Heading", "Action", "Character").

        Returns:
            A list of Paragraph objects that match the specified type.
        """
        return [p for p in self if p.paragraph_type == type]
