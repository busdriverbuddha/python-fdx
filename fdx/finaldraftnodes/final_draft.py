from xml.etree.ElementTree import ElementTree, Element

from fdx.finaldraftnodes.fdx_node import FDXNode
from fdx.finaldraftnodes.content import Content
from fdx.finaldraftnodes.paragraph import Paragraph
from fdx.customnodes import Scene


class FinalDraft(FDXNode):
    """Represents a complete FDX screenplay file.

    This class is the root node of an FDX document and provides methods for working
    with the screenplay as a whole, such as building scenes, accessing paragraphs,
    and saving the screenplay to a file.

    Attributes:
        content: The Content node that contains all screenplay paragraphs.
        element_settings: Dictionary of ElementSettings nodes keyed by their Type attribute.
        scenes: List of Scene objects constructed from the paragraphs (only available after
            calling build_scenes()).
    """

    def __init__(self, xml_attrib):
        """Initialize a FinalDraft node.

        Args:
            xml_attrib: Dictionary of XML attributes for this FinalDraft element.
        """
        super().__init__(xml_attrib, tag="FinalDraft")
        self.content: Content | None = None

    def _initialize(self):
        """Initialize the FinalDraft object after all children have been loaded.

        This method is called internally after parsing to set up the content reference
        and element settings dictionary. It locates the Content node among the children
        and collects all ElementSettings nodes.
        """
        for child in self:
            if isinstance(child, Content):
                self.content = child
                break

        self.element_settings = {
            node.xml_attrib.get('Type'): node
            for node in self
            if node.tag == "ElementSettings"
        }

    def build_scenes(self):
        """Build Scene objects from the paragraphs in the screenplay.

        This method constructs a list of Scene objects by grouping paragraphs. Each new
        "Scene Heading" paragraph starts a new scene, and all following paragraphs until
        the next "Scene Heading" are included in that scene.

        After calling this method, the scenes will be available as the `scenes` attribute.

        Raises:
            AssertionError: If the content attribute is None (not initialized).
        """
        self.scenes: list[Scene] = list()
        assert self.content is not None

        this_paragraph_list = [self.paragraphs[0]]
        for p in self.paragraphs[1:]:
            if p.paragraph_type == "Scene Heading":
                self.scenes.append(Scene(this_paragraph_list))
                this_paragraph_list = [p]
            else:
                this_paragraph_list.append(p)
        self.scenes.append(Scene(this_paragraph_list))

    def save_fdx(self, filename):
        """Save the FinalDraft object to an FDX file.

        This method converts the FinalDraft object and all its children back to XML
        and writes it to the specified file. The output follows the FDX file format
        with the appropriate XML declaration.

        Args:
            filename: Path to the FDX file to save.

        Raises:
            IOError: If the file cannot be written to.
        """
        root_element: Element = self.to_element()
        tree: ElementTree = ElementTree(root_element)
        with open(filename, 'wb') as f:
            f.write(b'<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
            tree.write(f, encoding='utf-8', xml_declaration=False)

    @property
    def paragraphs(self) -> list[Paragraph]:
        """Get all paragraphs in the screenplay.

        Returns:
            A list of all Paragraph objects in the content section, in order.

        Raises:
            AttributeError: If accessed before content is initialized.
        """
        return list(filter(lambda c: isinstance(c, Paragraph), self.content.children))
