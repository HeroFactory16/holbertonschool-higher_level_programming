#!/usr/bin/env python3
import json
"""Let's play with simple data"""


def serialize_and_save_to_file(data: dict, filename):
    """Serialization!!!!!"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_and_deserialize(filename):
    """Deserialization!!!!!"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
