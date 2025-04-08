import inspect
import pkgutil
import importlib
from types import ModuleType
from xml.etree.ElementTree import parse, Element

from fdx.finaldraftnodes import FDXNode, FinalDraft
from fdx.core.exceptions import FDXException


def _str_to_class(classname: str) -> type[FDXNode]:
    """Dynamically returns a class object if it exists within the fdx package, else FDXNode."""
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


def _node_to_object(node: Element) -> FDXNode:
    """Converts an XML node to an FDXNode object."""
    this_class: type[FDXNode] = _str_to_class(node.tag)
    if this_class is FDXNode:
        instance = FDXNode(node.attrib, tag=node.tag)
    else:
        instance = this_class(node.attrib)
    instance.xml_text = node.text or ""
    return instance


def read_fdx(filename: str) -> FinalDraft:
    """Reads an FDX file and returns a FinalDraft object."""
    tree = parse(filename)
    root = tree.getroot()
    if root.tag != "FinalDraft":
        raise FDXException("Not a FinalDraft file.")

    finaldraft = _node_to_object(root)
    queue: list[tuple[Element, FDXNode]] = [(root, finaldraft)]

    while queue:
        node, instance = queue.pop()
        for child in node:
            child_instance = _node_to_object(child)
            instance.children.append(child_instance)
            queue.insert(0, (child, child_instance))

    if isinstance(finaldraft, FinalDraft):
        finaldraft._initialize()

    return finaldraft
