"""Generates HTML documentation from JSONSchema files.

Assumes JSONSchema files are located in a directory named `/schemas`.
HTML documentation will be created in a directory called `/docs`.

This script requires the Python package [json_schema_for_humans](https://pypi.org/project/json-schema-for-humans/).
"""

import os
from pathlib import Path

from json_schema_for_humans.generate import generate_from_filename


def main():
    project_directory = Path(__file__).parent.absolute()
    json_directory = os.path.join(
        project_directory, "schemas")
    html_directory = os.path.join(project_directory, "docs")
    for schema in [f for f in os.listdir(
            json_directory) if f.endswith(".json")]:
        html_file = "{}.html".format(schema.split(".")[0])
        generate_from_filename(
            os.path.join(
                json_directory, schema), os.path.join(
                html_directory, html_file))


if __name__ == "__main__":
    main()
