from xml.etree.ElementTree import ElementTree, Element

from fdx.finaldraftnodes.fdx_node import FDXNode
from fdx.finaldraftnodes.content import Content
from fdx.finaldraftnodes.paragraph import Paragraph
from fdx.customnodes import Scene


class FinalDraft(FDXNode):
    """Represents a full FDX file.
    """

    def __init__(self, xml_attrib):
        super().__init__(xml_attrib, tag="FinalDraft")
        self.content: Content | None = None

    def _initialize(self):
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
        """Saves the FinalDraft object to an FDX file.

        Args:
            finaldraft (FinalDraft): The FinalDraft object to save.
            filename (str): Path to the FDX file to save.
        """
        root_element: Element = self.to_element()
        tree: ElementTree = ElementTree(root_element)
        with open(filename, 'wb') as f:
            f.write(b'<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
            tree.write(f, encoding='utf-8', xml_declaration=False)

    @property
    def paragraphs(self) -> list[Paragraph]:
        return list(filter(lambda c: isinstance(c, Paragraph), self.content.children))
