import os
import inspect
import pkgutil
import importlib
from types import ModuleType
import xml.etree.ElementTree as ET

from fdx.finaldraftnodes import FDXNode, FinalDraft
from fdx.core.exceptions import FDXException


def _str_to_class(classname: str) -> type[FDXNode]:
    """Dynamically returns a class object if it exists within the fdx package, else FDXNode.

    This function searches through all modules in the fdx package to find a class with the
    name matching the given XML tag. If found, returns that class, otherwise returns the
    base FDXNode class.

    Args:
        classname: The name of the class to find, which typically corresponds to an XML tag.

    Returns:
        A class reference that is either the requested class or the base FDXNode class.

    Raises:
        ImportError: If the module cannot be imported.
    """
    classes: dict[str, type[FDXNode]] = {}
    package: str = __package__

    try:
        pkg: ModuleType = importlib.import_module(package)
    except ImportError as e:
        raise ImportError(f"Cannot import package '{package}': {e}") from e

    for _, module_name, _ in pkgutil.walk_packages(path=pkg.__path__, prefix=package + "."):
        try:
            module: ModuleType = importlib.import_module(module_name)
            for name, cls in inspect.getmembers(module, inspect.isclass):
                if cls.__module__ == module_name:
                    classes[name] = cls
        except ImportError:
            continue

    return classes.get(classname, FDXNode)


def _node_to_object(node: ET.Element) -> FDXNode:
    """Converts an XML node to an FDXNode object.

    Takes an ElementTree XML node and creates the appropriate Python object based on
    the node's tag. The tag is used to determine which class to instantiate. If a
    specialized class for the tag exists, it will be used, otherwise a generic FDXNode.

    Args:
        node: ElementTree XML element to convert to an FDXNode object.

    Returns:
        An instance of FDXNode or a subclass corresponding to the XML tag.
    """
    this_class: type[FDXNode] = _str_to_class(node.tag)
    if this_class is FDXNode:
        instance = FDXNode(node.attrib, tag=node.tag)
    else:
        instance = this_class(node.attrib)
    instance.xml_text = node.text or ""
    return instance


def read_fdx(filename: os.PathLike) -> FinalDraft:
    """Reads an FDX file and returns a FinalDraft object.

    Parses the specified FDX file and constructs a tree of FDXNode objects that
    represents the screenplay. The root node will be a FinalDraft instance, and
    its children will be various FDXNode subclasses representing elements like
    paragraphs, content sections, etc.

    Args:
        filename: Path to the FDX file to read.

    Returns:
        A FinalDraft object representing the parsed screenplay.

    Raises:
        FDXException: If the file is not a valid FinalDraft file.
        Various XML parsing exceptions: If the file contains invalid XML.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    if root.tag != "FinalDraft":
        raise FDXException("Not a FinalDraft file.")

    finaldraft = _node_to_object(root)
    queue: list[tuple[ET.Element, FDXNode]] = [(root, finaldraft)]

    while queue:
        node, instance = queue.pop()
        for child in node:
            child_instance = _node_to_object(child)
            instance.children.append(child_instance)
            queue.insert(0, (child, child_instance))

    if isinstance(finaldraft, FinalDraft):
        finaldraft._initialize()

    return finaldraft


def read_string_to_finaldraft(string: str) -> FinalDraft:
    """Reads an FDX string and returns a FinalDraft object.

    Similar to read_fdx(), but parses from a string containing the XML content
    rather than from a file. This is useful for testing, examples, or when the
    FDX content is coming from a non-file source.

    Args:
        string: A string containing valid FDX (XML) content.

    Returns:
        A FinalDraft object representing the parsed screenplay.

    Raises:
        FDXException: If the string is not valid FinalDraft content.
        Various XML parsing exceptions: If the string contains invalid XML.
    """
    tree = ET.ElementTree(ET.fromstring(string))
    root = tree.getroot()
    if root.tag != "FinalDraft":
        raise FDXException("Not a FinalDraft file.")

    finaldraft = _node_to_object(root)
    queue: list[tuple[ET.Element, FDXNode]] = [(root, finaldraft)]

    while queue:
        node, instance = queue.pop()
        for child in node:
            child_instance = _node_to_object(child)
            instance.children.append(child_instance)
            queue.insert(0, (child, child_instance))

    if isinstance(finaldraft, FinalDraft):
        finaldraft._initialize()

    return finaldraft
