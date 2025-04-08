from fdx.finaldraftnodes.fdx_node import FDXNode
from fdx.finaldraftnodes.paragraph import Paragraph


class Content(FDXNode):

    def __init__(self, xml_attrib):
        super().__init__(xml_attrib, tag="Content")

    def clean_empty_paragraphs(self):
        self.children = [p for p in self.children if p.plain_text.strip()]

    def get_paragraphs_by_type(self, type: str) -> list[Paragraph]:
        return [p for p in self if p.paragraph_type == type]
