#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def to_element(tag: str, data) -> ET.Element:
    element = ET.Element(tag)

    if isinstance(data, dict):
        for key, value in data.items():
            element.append(to_element(str(key), value))
    elif isinstance(data, list):
        for item in data:
            element.append(to_element("item", item))
    else:
        element.text = "" if data is None else str(data)

    return element


def from_element(element: ET.Element):
    children = list(element)

    if not children:
        return element.text or ""

    tags = [child.tag for child in children]
    if len(set(tags)) == 1 and len(children) > 1:
        return [from_element(child) for child in children]

    return {child.tag: from_element(child) for child in children}


def serialize_to_xml(data: dict, filename: str, root_tag: str = "root"):
    tree = ET.ElementTree(to_element(root_tag, data))
    ET.indent(tree, space="    ")
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename: str):
    return from_element(ET.parse(filename).getroot())
