from fdx.core.exceptions import FDXException
from fdx.finaldraftnodes.paragraph import Paragraph


class Scene:
    """Represents a scene in a screenplay.

    A scene is a collection of paragraphs, typically starting with a Scene Heading
    (e.g., "INT. LIVING ROOM - DAY") followed by action, dialogue, and other paragraph types.

    The first paragraph may be a Scene Heading, in which case the scene is a regular scene.
    If the first paragraph is not a Scene Heading, the scene is considered a "preamble" scene.

    Attributes:
        paragraphs: A list of Paragraph objects that make up the scene.
    """

    def __init__(self, paragraphs: list[Paragraph]):
        """Initialize a Scene with a list of paragraphs.

        Args:
            paragraphs: A list of Paragraph objects that form the scene.

        Raises:
            FDXException: If the paragraphs list is empty or if there are Scene Heading
                paragraphs in positions other than the first.
        """
        # scene may not be empty
        if len(paragraphs) == 0:
            raise FDXException("Scene may not be empty")

        # only first paragraph may be scene heading, if there is a scene heading
        if any(p.paragraph_type == 'Scene Heading' for p in paragraphs[1:]):
            raise FDXException("Only the first paragraph may be a scene heading")

        self.paragraphs: list[Paragraph] = paragraphs

    @property
    def plain_text(self) -> str:
        """Get the plain text content of the entire scene.

        Returns:
            A string containing all paragraph text joined with newlines.
        """
        return "\n".join(p.plain_text for p in self.paragraphs)

    @property
    def is_preamble(self) -> bool:
        """Check if this scene is a preamble scene.

        A preamble scene is one that doesn't start with a Scene Heading paragraph.
        This is typically content that appears before the first proper scene in a screenplay.

        Returns:
            True if the scene is a preamble, False otherwise.
        """
        return self.paragraphs[0].paragraph_type != 'Scene Heading'

    @property
    def heading(self) -> Paragraph:
        """Get the heading of the scene.

        Returns:
            The heading of the scene.
        """
        if not self.is_preamble:
            return self.paragraphs[0]
        else:
            return None
