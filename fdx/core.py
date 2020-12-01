import sys
from typing import Iterable
from warnings import warn


class FDXNode:
    # __slots__ = 'text',

    def __init__(self, xml_attrib):
        self.children = list()
        self.xml_attrib = xml_attrib
        
# NATIVE FDX CLASSES 
# all in this section corresponds to actual XML nodes generated by FD

class FinalDraft(FDXNode):

    # __slots__ = 'DocumentType', 'Template', 'Version'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = None
    
    def _initialize(self):
        for child in self.children:
            if isinstance(child, Content):
                self.content = child
                break
        
        self.element_settings = dict()
        for node in filter(lambda n: isinstance(n, ElementSettings), self.children):
            self.element_settings[node.xml_attrib.get('Type')] = node

    def build_scenes(self):
        
        self.scenes = list()
        assert self.content is not None
        paragraphs = list(filter(lambda c: isinstance(c, Paragraph), self.content.children))
        this_paragraph_list = [paragraphs[0]]
        for p in paragraphs[1:]:
            if p.paragraph_type == "Scene Heading":
                self.scenes.append(Scene(this_paragraph_list))
                this_paragraph_list = [p]
            else:
                this_paragraph_list.append(p)
        self.scenes.append(Scene(this_paragraph_list))









class Content(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Watermarking(FDXNode):

    # __slots__ = 'Opacity', 'Position', 'Text'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class HeaderAndFooter(FDXNode):

    # __slots__ = 'FooterFirstPage', 'FooterVisible', 'HeaderFirstPage', 'HeaderVisible', 'StartingPage'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SpellCheckIgnoreLists(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PageLayout(FDXNode):

    # __slots__ = 'BackgroundColor', 'BottomMargin', 'BreakDialogueAndActionAtSentences', 'DocumentLeading', 'FooterMargin', 'ForegroundColor', 'HeaderMargin', 'InvisiblesColor', 'TopMargin', 'UsesSmartQuotes'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class WindowState(FDXNode):

    # __slots__ = 'Height', 'Left', 'Mode', 'Top', 'Width'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TextState(FDXNode):

    # __slots__ = 'Scaling', 'Selection', 'ShowInvisibles'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ElementSettings(FDXNode):

    # __slots__ = 'Type'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TitlePage(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UnanchoredScriptNotes(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SmartType(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MoresAndContinueds(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class LockedPages(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Revisions(FDXNode):

    # __slots__ = 'ActiveSet', 'Location', 'RevisionMode', 'RevisionsShown', 'ShowAllMarks', 'ShowAllSets', 'ShowPageColor'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SplitState(FDXNode):

    # __slots__ = 'ActivePanel', 'CardsAcross', 'SplitMode', 'SplitterPosition'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Macros(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Actors(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Cast(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SceneNumberOptions(FDXNode):

    # __slots__ = 'LeftLocation', 'NumberScheme', 'RightLocation', 'ShowNumbersOnLeft', 'ShowNumbersOnRight'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CastList(FDXNode):

    # __slots__ = 'SortOption'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CharacterHighlighting(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CharacterNavigatorPreferences(FDXNode):

    # __slots__ = 'IsSortAscending', 'SortColumn'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TagsNavigatorPreferences(FDXNode):

    # __slots__ = 'IsSortAscending', 'SortColumn'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AltCollection(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TargetScriptLength(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ListItems(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DisplayBoards(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TagData(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Characters(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Images(FDXNode):

    # __slots__ = 'Hidden'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Paragraph(FDXNode):

    ALL_CAPS_TYPES = [
        'Scene Heading',
        'Transition',
        'Shot',
        'Character',
        # TODO: redo using ElementSettings
    ]

    # __slots__ = 'Type', 'Alignment', 'FirstIndent', 'Leading', 'LeftIndent', 'RightIndent', 'SpaceBefore', 'Spacing', 'StartsNewPage', 'Number', 'Label'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def paragraph_type(self):
        return self.xml_attrib.get("Type")

    @property
    def plain_text(self):
        text = "".join(
            child.xml_text
            for child in self.children
            if isinstance(child, Text)
        )
        if self.paragraph_type in self.ALL_CAPS_TYPES:
            return text.upper()
        else:
            return text

class DynamicContent(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Distribution(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class WatermarkImage(FDXNode):

    # __slots__ = 'Height'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Header(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Footer(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class IgnoredRanges(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class IgnoredWords(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PageSize(FDXNode):

    # __slots__ = 'Height', 'Width'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AutoCastList(FDXNode):

    # __slots__ = 'AddParentheses', 'AutomaticallyGenerate', 'CastListElement'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class FontSpec(FDXNode):

    # __slots__ = 'AdornmentStyle', 'Background', 'Color', 'Font', 'RevisionID', 'Size', 'Style'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ParagraphSpec(FDXNode):

    # __slots__ = 'Alignment', 'FirstIndent', 'Leading', 'LeftIndent', 'RightIndent', 'SpaceBefore', 'Spacing', 'StartsNewPage'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Behavior(FDXNode):

    # __slots__ = 'PaginateAs', 'ReturnKey', 'Shortcut'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Extensions(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SceneIntros(FDXNode):

    # __slots__ = 'Separator'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Locations(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TimesOfDay(FDXNode):

    # __slots__ = 'Separator'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Transitions(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DialogueBreaks(FDXNode):

    # __slots__ = 'AutomaticCharacterContinueds', 'BottomOfPage', 'DialogueBottom', 'DialogueTop', 'TopOfNext'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SceneBreaks(FDXNode):

    # __slots__ = 'ContinuedNumber', 'SceneBottom', 'SceneBottomOfPage', 'SceneTop', 'SceneTopOfNext'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Revision(FDXNode):

    # __slots__ = 'Color', 'FullRevision', 'ID', 'Mark', 'Name', 'PageColor', 'Style'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ScriptPanel(FDXNode):

    # __slots__ = 'DisplayMode'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Macro(FDXNode):

    # __slots__ = 'Element', 'Name', 'Shortcut', 'Text', 'Transition'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Actor(FDXNode):

    # __slots__ = 'MacVoice', 'Name', 'Pitch', 'Speed', 'WinVoice'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Narrator(FDXNode):

    # __slots__ = 'Actor'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Member(FDXNode):

    # __slots__ = 'Actor', 'Character'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CustomOrder(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Character(FDXNode):

    # __slots__ = 'Color', 'Name', 'Visible'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Column(FDXNode):

    # __slots__ = 'Width', 'UserType'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DisplayBoard(FDXNode):

    # __slots__ = 'Height', 'ScrollOrigin', 'Type', 'Width', 'ZoomLevel'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TagCategories(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TableColumnSettings(FDXNode):

    # __slots__ = 'IsSortAscending', 'SortColumn', 'TableIdentifier'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CharacterTraitData(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ChartOptions(FDXNode):

    # __slots__ = 'Identifier'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SceneProperties(FDXNode):

    # __slots__ = 'Length', 'Page', 'Title', 'Color'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Text(FDXNode):

    # __slots__ = 'AdornmentStyle', 'Background', 'Color', 'Font', 'RevisionID', 'Size', 'Style'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Name(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Extension(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SceneIntro(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Location(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TimeOfDay(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Transition(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Alias(FDXNode):

    # __slots__ = 'Confirm', 'MatchCase', 'SmartReplace', 'Text', 'WordOnly'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Element(FDXNode):

    # __slots__ = 'Type'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TagCategory(FDXNode):

    # __slots__ = 'Color', 'Id', 'Name', 'Number', 'Style'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Traits(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Holders(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class FilterSets(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SceneArcBeats(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DynamicLabel(FDXNode):

    # __slots__ = 'Type', 'AdornmentStyle', 'Background', 'Color', 'Font', 'RevisionID', 'Size', 'Style'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Tabstops(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ActivateIn(FDXNode):

    # __slots__ = 'Element'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Trait(FDXNode):

    # __slots__ = 'ID', 'Name', 'Type'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class FilterSet(FDXNode):

    # __slots__ = 'Default'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CharacterArcBeat(FDXNode):

    # __slots__ = 'Name'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Tabstop(FDXNode):

    # __slots__ = 'Position', 'Type'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Filter(FDXNode):

    # __slots__ = 'Index', 'Name', 'Value'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Match(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ScriptNote(FDXNode):

    # __slots__ = 'Author', 'Color', 'DateModified', 'DateTime', 'Name', 'Type'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Range(FDXNode):

    # __slots__ = 'End', 'Start'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Word(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ScriptNoteDefinitions(FDXNode):

    # __slots__ = 'Active'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DeletedText(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ScriptNoteDefinition(FDXNode):

    # __slots__ = 'Color', 'ID', 'Marker', 'Name'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DeletedTextLocation(FDXNode):

    # __slots__ = 'Offset', 'RevisionID'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ScenePanel(FDXNode):

    # __slots__ = 'ActionVisible', 'SummaryVisible', 'TitleVisible'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ListItem(FDXNode):

    # __slots__ = 'Color', 'Id', 'Title', 'Type'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SubordinateTo(FDXNode):

    # __slots__ = 'Number', 'Order', 'Type'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Item(FDXNode):

    # __slots__ = 'Id', 'Height', 'Left', 'Top', 'Width'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UserDocumentData(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UserParagraphData(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class OmittedScene(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Image(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Picture(FDXNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# AUXILIARY CLASSES
# helper classes for this library

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


        

def _str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

def _node_to_object(node):
    this_class = _str_to_class(node.tag)
    this_instance = this_class(node.attrib)
    # TODO: deal with nonexistent classes
    
    
    this_instance.xml_text = node.text or ""
    
    
    return this_instance

def read_fdx(filename):
    from xml.etree import ElementTree as ET

    tree = ET.parse(filename)
    root = tree.getroot()
    assert root.tag == "FinalDraft"
    # TODO: define exception for non-final-draft file

    finaldraft = _node_to_object(root)
    queue = [(root, finaldraft)]
    
    while queue:
        node, instance = queue.pop()
        for child in node:
            child_instance = _node_to_object(child)
            instance.children.append(child_instance)
            queue.insert(0, (child, child_instance))
    
    finaldraft._initialize()

    return finaldraft
