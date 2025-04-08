from xml.etree.ElementTree import Element


class FDXNode:
    def __init__(self, xml_attrib: dict[str, str], tag: str):
        self.tag: str = tag
        self.children: list[FDXNode] = []
        self.xml_attrib: dict[str, str] = xml_attrib
        self.xml_text: str = ""

    def __repr__(self):
        return f"FDXNode: {self.tag}"

    def __iter__(self):
        return iter(self.children)

    def __getitem__(self, index: int) -> "FDXNode":
        return self.children[index]

    def __len__(self) -> int:
        return len(self.children)

    def to_element(self) -> Element:
        """Converts the FDXNode back to an XML element."""
        element: Element = Element(self.tag, self.xml_attrib)
        element.text = self.xml_text
        for child in self.children:
            element.append(child.to_element())
        return element
