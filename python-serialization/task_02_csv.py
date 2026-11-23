#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename: str, json_filename: str = "data.json"):
    try:
        with open(csv_filename, "r", encoding="utf-8", newline="") as csv_file:
            rows = list(csv.DictReader(csv_file))
    except:
        return False

    with open(json_filename, "w", encoding="utf-8") as json_file:
        json.dump(rows, json_file, indent=4, ensure_ascii=False)

    return True
