from fdx.core.exceptions import FDXException
from fdx.finaldraftnodes.paragraph import Paragraph


class Scene:

    def __init__(self, paragraphs: list[Paragraph]):
        # scene may not be empty
        if len(paragraphs) == 0:
            raise FDXException("Scene may not be empty")

        # only first paragraph may be scene heading, if there is a scene heading
        if any(p.paragraph_type == 'Scene Heading' for p in paragraphs[1:]):
            raise FDXException("Only the first paragraph may be a scene heading")

        self.paragraphs: list[Paragraph] = paragraphs

    @property
    def plain_text(self) -> str:
        return "\n".join(p.plain_text for p in self.paragraphs)

    @property
    def is_preamble(self) -> bool:
        return self.paragraphs[0].paragraph_type != 'Scene Heading'
