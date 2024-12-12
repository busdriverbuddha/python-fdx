from xml.etree.ElementTree import ElementTree

from fdx.fdx_node import FDXNode
from fdx.scene import Scene


class FinalDraft(FDXNode):
    """Represents a full FDX file.
    """

    def __init__(self, xml_attrib):
        super().__init__(xml_attrib, tag="FinalDraft")
        self.content = None

    def _initialize(self):
        for child in self.children:
            if child.tag == "Content":
                self.content = child
                break

        self.element_settings = {
            node.xml_attrib.get('Type'): node
            for node in self.children
            if node.tag == "ElementSettings"
        }

    def build_scenes(self):

        self.scenes = list()
        assert self.content is not None
        paragraphs = list(filter(lambda c: c.tag == "Paragraph", self.content.children))
        this_paragraph_list = [paragraphs[0]]
        for p in paragraphs[1:]:
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
        root_element = self.to_element()
        tree = ElementTree(root_element)
        with open(filename, 'wb') as f:
            f.write(b'<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
            tree.write(f, encoding='utf-8', xml_declaration=False)
