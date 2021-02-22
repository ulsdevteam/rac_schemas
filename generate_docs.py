import os
from pathlib import Path

from json_schema_for_humans.generate import generate_from_filename


class DocumentGenerator:
    """Generates HTML documentation based on JSON schema files."""

    def run(self):
        """Iterates over a directory and generates an HTML schema file from any file ending in .json"""
        project_directory = Path(__file__).parent.absolute()
        json_directory = os.path.join(
            project_directory, "rac_schemas", "schemas")
        html_directory = os.path.join(project_directory, "docs")
        json_files = [file for file in os.listdir(
            json_directory) if file.endswith(".json")]
        for schema in json_files:
            html_file = "{}.html".format(schema.split(".")[0])
            generate_from_filename(
                os.path.join(
                    json_directory, schema), os.path.join(
                    html_directory, html_file))


DocumentGenerator().run()
