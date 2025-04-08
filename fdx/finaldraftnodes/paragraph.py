from fdx.finaldraftnodes.fdx_node import FDXNode


class Paragraph(FDXNode):

    ALL_CAPS_TYPES = [
        'Scene Heading',
        'Transition',
        'Shot',
        'Character',
        # TODO: redo using ElementSettings
    ]

    def __init__(self, xml_attrib: dict[str, str]):
        super().__init__(xml_attrib, tag="Paragraph")

    def __repr__(self):
        return f"Paragraph: {self.paragraph_type}"

    @property
    def paragraph_type(self) -> str:
        return self.xml_attrib.get("Type")

    @property
    def plain_text(self) -> str:
        text: str = "".join(
            child.xml_text
            for child in self
            if child.tag == "Text"
        )
        if self.paragraph_type in self.ALL_CAPS_TYPES:
            return text.upper()
        else:
            return text
