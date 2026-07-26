#!/usr/bin/env python3
"""Generate a JSON coverage summary from a coverage.xml file."""

import json
import sys
import xml.etree.ElementTree as ET
from typing import Optional


def main(coverage_xml_path: str) -> None:
    """Parse the given coverage.xml and print a JSON summary with the coverage percentage."""
    try:
        tree = ET.parse(coverage_xml_path)
    except (FileNotFoundError, ET.ParseError) as e:
        print(f"Error reading coverage file: {e}", file=sys.stderr)
        sys.exit(1)

    root = tree.getroot()
    line_rate: Optional[str] = root.attrib.get("line-rate")
    try:
        percent = float(line_rate) * 100.0 if line_rate is not None else 0.0
    except (ValueError, TypeError):
        percent = 0.0

    data = {"coverage": round(percent, 2)}
    print(json.dumps(data))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <coverage.xml>", file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1])
