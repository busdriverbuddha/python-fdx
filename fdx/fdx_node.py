from xml.etree.ElementTree import Element


class FDXNode:
    def __init__(self, xml_attrib, tag):
        self.tag = tag
        self.children = []
        self.xml_attrib = xml_attrib
        self.xml_text = ""

    def to_element(self):
        """Converts the FDXNode back to an XML element."""
        element = Element(self.tag, self.xml_attrib)
        element.text = self.xml_text
        for child in self.children:
            element.append(child.to_element())
        return element
