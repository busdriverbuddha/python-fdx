class Scene:

    def __init__(self, paragraphs):
        # scene may not be empty
        assert len(paragraphs) > 0

        # only first paragraph may be scene heading, if there is a scene heading
        assert not any(p.paragraph_type == 'Scene Heading' for p in paragraphs[1:])

        self.preamble = paragraphs[0].paragraph_type != 'Scene Heading'
        self.paragraphs = paragraphs

    @property
    def plain_text(self):
        return "\n".join(p.plain_text for p in self.paragraphs)
