#!/usr/bin/env python3
import xmltodict

def deserialize_from_xml(filename: str):
    with open(filename, "rb") as file:
        data = xmltodict.parse(file)
    return data


def serialize_to_xml(dictionary, filename):
    xml_string = xmltodict.unparse(dictionary, pretty=True)
    with open(filename, "wb") as file:
        file.write(xml_string)
