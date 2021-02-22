import argparse
import os

from json_schema_for_humans.generate import generate_from_filename


class DocumentGenerator:
    """Generates HTML documentation based on JSON schema files."""

    def run(self, json_directory, html_directory):
        """Iterates over a directory and generates an HTML schema file from any file ending in .json

        args:
            directory(str): a string representation of the full filepath of the directory containing schema files
        """
        filenames = [file for file in os.listdir(
            json_directory) if file.endswith(".json")]
        for schema in filenames:
            html_file = "{}.html".format(schema.split(".")[0])
            generate_from_filename(
                os.path.join(
                    json_directory, schema), os.path.join(
                    html_directory, html_file))


parser = argparse.ArgumentParser(
    description="Creates HTML files based on JSON schemas.")
parser.add_argument(
    "json_directory",
    help="Directory containing JSON Schema files.")
parser.add_argument(
    "html_directory",
    help="Directory to write HTML files to.")
args = parser.parse_args()

DocumentGenerator().run(args.json_directory, args.html_directory)
