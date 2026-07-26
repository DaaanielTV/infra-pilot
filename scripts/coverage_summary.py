#!/usr/bin/env python3
"""Print the current coverage percentage from coverage.xml."""

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional


def read_coverage(xml_path: Path) -> float:
    """Parse coverage.xml and return the line coverage percentage as a float."""
    if not xml_path.exists():
        return 0.0
    try:
        tree = ET.parse(xml_path)
    except ET.ParseError as e:
        print(f"Error parsing coverage XML: {e}", file=sys.stderr)
        return 0.0

    root = tree.getroot()
    line_rate: Optional[str] = root.attrib.get("line-rate")
    try:
        return float(line_rate) * 100.0 if line_rate is not None else 0.0
    except (ValueError, TypeError):
        return 0.0


def main() -> None:
    """Parse CLI arguments and print coverage summary."""
    parser = argparse.ArgumentParser(
        description="Print current coverage percentage from coverage.xml."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default="coverage.xml",
        help="Path to coverage.xml (default: coverage.xml)",
    )
    args = parser.parse_args()

    cov = read_coverage(Path(args.path))
    print(f"Current coverage: {cov:.2f}%")
    print(json.dumps({"coverage": round(cov, 2)}))


if __name__ == "__main__":
    main()
