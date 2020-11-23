import sys

class FDXNode:
    # __slots__ = 'text',

    def __init__(self):
        self.children = list()
        
        
class FinalDraft(FDXNode):

    # __slots__ = 'DocumentType', 'Template', 'Version'

    def __init__(self):
        super().__init__()


class Content(FDXNode):

    def __init__(self):
        super().__init__()


class Watermarking(FDXNode):

    # __slots__ = 'Opacity', 'Position', 'Text'

    def __init__(self):
        super().__init__()


class HeaderAndFooter(FDXNode):

    # __slots__ = 'FooterFirstPage', 'FooterVisible', 'HeaderFirstPage', 'HeaderVisible', 'StartingPage'

    def __init__(self):
        super().__init__()


class SpellCheckIgnoreLists(FDXNode):

    def __init__(self):
        super().__init__()


class PageLayout(FDXNode):

    # __slots__ = 'BackgroundColor', 'BottomMargin', 'BreakDialogueAndActionAtSentences', 'DocumentLeading', 'FooterMargin', 'ForegroundColor', 'HeaderMargin', 'InvisiblesColor', 'TopMargin', 'UsesSmartQuotes'

    def __init__(self):
        super().__init__()


class WindowState(FDXNode):

    # __slots__ = 'Height', 'Left', 'Mode', 'Top', 'Width'

    def __init__(self):
        super().__init__()


class TextState(FDXNode):

    # __slots__ = 'Scaling', 'Selection', 'ShowInvisibles'

    def __init__(self):
        super().__init__()


class ElementSettings(FDXNode):

    # __slots__ = 'Type'

    def __init__(self):
        super().__init__()


class TitlePage(FDXNode):

    def __init__(self):
        super().__init__()


class UnanchoredScriptNotes(FDXNode):

    def __init__(self):
        super().__init__()


class SmartType(FDXNode):

    def __init__(self):
        super().__init__()


class MoresAndContinueds(FDXNode):

    def __init__(self):
        super().__init__()


class LockedPages(FDXNode):

    def __init__(self):
        super().__init__()


class Revisions(FDXNode):

    # __slots__ = 'ActiveSet', 'Location', 'RevisionMode', 'RevisionsShown', 'ShowAllMarks', 'ShowAllSets', 'ShowPageColor'

    def __init__(self):
        super().__init__()


class SplitState(FDXNode):

    # __slots__ = 'ActivePanel', 'CardsAcross', 'SplitMode', 'SplitterPosition'

    def __init__(self):
        super().__init__()


class Macros(FDXNode):

    def __init__(self):
        super().__init__()


class Actors(FDXNode):

    def __init__(self):
        super().__init__()


class Cast(FDXNode):

    def __init__(self):
        super().__init__()


class SceneNumberOptions(FDXNode):

    # __slots__ = 'LeftLocation', 'NumberScheme', 'RightLocation', 'ShowNumbersOnLeft', 'ShowNumbersOnRight'

    def __init__(self):
        super().__init__()


class CastList(FDXNode):

    # __slots__ = 'SortOption'

    def __init__(self):
        super().__init__()


class CharacterHighlighting(FDXNode):

    def __init__(self):
        super().__init__()


class CharacterNavigatorPreferences(FDXNode):

    # __slots__ = 'IsSortAscending', 'SortColumn'

    def __init__(self):
        super().__init__()


class TagsNavigatorPreferences(FDXNode):

    # __slots__ = 'IsSortAscending', 'SortColumn'

    def __init__(self):
        super().__init__()


class AltCollection(FDXNode):

    def __init__(self):
        super().__init__()


class TargetScriptLength(FDXNode):

    def __init__(self):
        super().__init__()


class ListItems(FDXNode):

    def __init__(self):
        super().__init__()


class DisplayBoards(FDXNode):

    def __init__(self):
        super().__init__()


class TagData(FDXNode):

    def __init__(self):
        super().__init__()


class Characters(FDXNode):

    def __init__(self):
        super().__init__()


class Images(FDXNode):

    # __slots__ = 'Hidden'

    def __init__(self):
        super().__init__()


class Paragraph(FDXNode):

    # __slots__ = 'Type', 'Alignment', 'FirstIndent', 'Leading', 'LeftIndent', 'RightIndent', 'SpaceBefore', 'Spacing', 'StartsNewPage', 'Number', 'Label'

    def __init__(self):
        super().__init__()


class DynamicContent(FDXNode):

    def __init__(self):
        super().__init__()


class Distribution(FDXNode):

    def __init__(self):
        super().__init__()


class WatermarkImage(FDXNode):

    # __slots__ = 'Height'

    def __init__(self):
        super().__init__()


class Header(FDXNode):

    def __init__(self):
        super().__init__()


class Footer(FDXNode):

    def __init__(self):
        super().__init__()


class IgnoredRanges(FDXNode):

    def __init__(self):
        super().__init__()


class IgnoredWords(FDXNode):

    def __init__(self):
        super().__init__()


class PageSize(FDXNode):

    # __slots__ = 'Height', 'Width'

    def __init__(self):
        super().__init__()


class AutoCastList(FDXNode):

    # __slots__ = 'AddParentheses', 'AutomaticallyGenerate', 'CastListElement'

    def __init__(self):
        super().__init__()


class FontSpec(FDXNode):

    # __slots__ = 'AdornmentStyle', 'Background', 'Color', 'Font', 'RevisionID', 'Size', 'Style'

    def __init__(self):
        super().__init__()


class ParagraphSpec(FDXNode):

    # __slots__ = 'Alignment', 'FirstIndent', 'Leading', 'LeftIndent', 'RightIndent', 'SpaceBefore', 'Spacing', 'StartsNewPage'

    def __init__(self):
        super().__init__()


class Behavior(FDXNode):

    # __slots__ = 'PaginateAs', 'ReturnKey', 'Shortcut'

    def __init__(self):
        super().__init__()


class Extensions(FDXNode):

    def __init__(self):
        super().__init__()


class SceneIntros(FDXNode):

    # __slots__ = 'Separator'

    def __init__(self):
        super().__init__()


class Locations(FDXNode):

    def __init__(self):
        super().__init__()


class TimesOfDay(FDXNode):

    # __slots__ = 'Separator'

    def __init__(self):
        super().__init__()


class Transitions(FDXNode):

    def __init__(self):
        super().__init__()


class DialogueBreaks(FDXNode):

    # __slots__ = 'AutomaticCharacterContinueds', 'BottomOfPage', 'DialogueBottom', 'DialogueTop', 'TopOfNext'

    def __init__(self):
        super().__init__()


class SceneBreaks(FDXNode):

    # __slots__ = 'ContinuedNumber', 'SceneBottom', 'SceneBottomOfPage', 'SceneTop', 'SceneTopOfNext'

    def __init__(self):
        super().__init__()


class Revision(FDXNode):

    # __slots__ = 'Color', 'FullRevision', 'ID', 'Mark', 'Name', 'PageColor', 'Style'

    def __init__(self):
        super().__init__()


class ScriptPanel(FDXNode):

    # __slots__ = 'DisplayMode'

    def __init__(self):
        super().__init__()


class Macro(FDXNode):

    # __slots__ = 'Element', 'Name', 'Shortcut', 'Text', 'Transition'

    def __init__(self):
        super().__init__()


class Actor(FDXNode):

    # __slots__ = 'MacVoice', 'Name', 'Pitch', 'Speed', 'WinVoice'

    def __init__(self):
        super().__init__()


class Narrator(FDXNode):

    # __slots__ = 'Actor'

    def __init__(self):
        super().__init__()


class Member(FDXNode):

    # __slots__ = 'Actor', 'Character'

    def __init__(self):
        super().__init__()


class CustomOrder(FDXNode):

    def __init__(self):
        super().__init__()


class Character(FDXNode):

    # __slots__ = 'Color', 'Name', 'Visible'

    def __init__(self):
        super().__init__()


class Column(FDXNode):

    # __slots__ = 'Width', 'UserType'

    def __init__(self):
        super().__init__()


class DisplayBoard(FDXNode):

    # __slots__ = 'Height', 'ScrollOrigin', 'Type', 'Width', 'ZoomLevel'

    def __init__(self):
        super().__init__()


class TagCategories(FDXNode):

    def __init__(self):
        super().__init__()


class TableColumnSettings(FDXNode):

    # __slots__ = 'IsSortAscending', 'SortColumn', 'TableIdentifier'

    def __init__(self):
        super().__init__()


class CharacterTraitData(FDXNode):

    def __init__(self):
        super().__init__()


class ChartOptions(FDXNode):

    # __slots__ = 'Identifier'

    def __init__(self):
        super().__init__()


class SceneProperties(FDXNode):

    # __slots__ = 'Length', 'Page', 'Title', 'Color'

    def __init__(self):
        super().__init__()


class Text(FDXNode):

    # __slots__ = 'AdornmentStyle', 'Background', 'Color', 'Font', 'RevisionID', 'Size', 'Style'

    def __init__(self):
        super().__init__()


class Name(FDXNode):

    def __init__(self):
        super().__init__()


class Extension(FDXNode):

    def __init__(self):
        super().__init__()


class SceneIntro(FDXNode):

    def __init__(self):
        super().__init__()


class Location(FDXNode):

    def __init__(self):
        super().__init__()


class TimeOfDay(FDXNode):

    def __init__(self):
        super().__init__()


class Transition(FDXNode):

    def __init__(self):
        super().__init__()


class Alias(FDXNode):

    # __slots__ = 'Confirm', 'MatchCase', 'SmartReplace', 'Text', 'WordOnly'

    def __init__(self):
        super().__init__()


class Element(FDXNode):

    # __slots__ = 'Type'

    def __init__(self):
        super().__init__()


class TagCategory(FDXNode):

    # __slots__ = 'Color', 'Id', 'Name', 'Number', 'Style'

    def __init__(self):
        super().__init__()


class Traits(FDXNode):

    def __init__(self):
        super().__init__()


class Holders(FDXNode):

    def __init__(self):
        super().__init__()


class FilterSets(FDXNode):

    def __init__(self):
        super().__init__()


class SceneArcBeats(FDXNode):

    def __init__(self):
        super().__init__()


class DynamicLabel(FDXNode):

    # __slots__ = 'Type', 'AdornmentStyle', 'Background', 'Color', 'Font', 'RevisionID', 'Size', 'Style'

    def __init__(self):
        super().__init__()


class Tabstops(FDXNode):

    def __init__(self):
        super().__init__()


class ActivateIn(FDXNode):

    # __slots__ = 'Element'

    def __init__(self):
        super().__init__()


class Trait(FDXNode):

    # __slots__ = 'ID', 'Name', 'Type'

    def __init__(self):
        super().__init__()


class FilterSet(FDXNode):

    # __slots__ = 'Default'

    def __init__(self):
        super().__init__()


class CharacterArcBeat(FDXNode):

    # __slots__ = 'Name'

    def __init__(self):
        super().__init__()


class Tabstop(FDXNode):

    # __slots__ = 'Position', 'Type'

    def __init__(self):
        super().__init__()


class Filter(FDXNode):

    # __slots__ = 'Index', 'Name', 'Value'

    def __init__(self):
        super().__init__()


class Match(FDXNode):

    def __init__(self):
        super().__init__()


class ScriptNote(FDXNode):

    # __slots__ = 'Author', 'Color', 'DateModified', 'DateTime', 'Name', 'Type'

    def __init__(self):
        super().__init__()


class Range(FDXNode):

    # __slots__ = 'End', 'Start'

    def __init__(self):
        super().__init__()


class Word(FDXNode):

    def __init__(self):
        super().__init__()


class ScriptNoteDefinitions(FDXNode):

    # __slots__ = 'Active'

    def __init__(self):
        super().__init__()


class DeletedText(FDXNode):

    def __init__(self):
        super().__init__()


class ScriptNoteDefinition(FDXNode):

    # __slots__ = 'Color', 'ID', 'Marker', 'Name'

    def __init__(self):
        super().__init__()


class DeletedTextLocation(FDXNode):

    # __slots__ = 'Offset', 'RevisionID'

    def __init__(self):
        super().__init__()


class ScenePanel(FDXNode):

    # __slots__ = 'ActionVisible', 'SummaryVisible', 'TitleVisible'

    def __init__(self):
        super().__init__()


class ListItem(FDXNode):

    # __slots__ = 'Color', 'Id', 'Title', 'Type'

    def __init__(self):
        super().__init__()


class SubordinateTo(FDXNode):

    # __slots__ = 'Number', 'Order', 'Type'

    def __init__(self):
        super().__init__()


class Item(FDXNode):

    # __slots__ = 'Id', 'Height', 'Left', 'Top', 'Width'

    def __init__(self):
        super().__init__()


class UserDocumentData(FDXNode):

    def __init__(self):
        super().__init__()


class UserParagraphData(FDXNode):

    def __init__(self):
        super().__init__()


class OmittedScene(FDXNode):

    def __init__(self):
        super().__init__()

def _str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

def _node_to_object(node):
    this_class = _str_to_class(node.tag)
    this_instance = this_class()
    # TODO: deal with nonexistent classes
    
    for key, value in node.attrib.items():
        setattr(this_instance, key, value)
    
    if node.text:
        this_instance.text = node.text
    
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
    
    return finaldraft
