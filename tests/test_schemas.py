import json
import unittest
from os import listdir
from os.path import abspath, dirname, join

from rac_schemas import handle_schema_filename, is_valid
from rac_schemas.exceptions import ValidationError

base_path = dirname(dirname(abspath(__file__)))

schemas_dir = join(base_path, "rac_schemas", "schemas")
fixtures_dir = join(base_path, "fixtures")


class TestSchemas(unittest.TestCase):

    def test_schemas_valid(self):
        """Ensures all schemas are valid JSON.

        Attempts to load each of the schemas using the json library. If any of
        them are invalid JSON a json.JSONDecodeError exception will be thrown.
        """
        for f in listdir(schemas_dir):
            with open(join(schemas_dir, f)) as sf:
                json.load(sf)

    def test_schema_filename(self):
        """Ensures that schema filenames are parsed properly."""
        for filename in ["schema.json", "schema"]:
            processed = handle_schema_filename(filename)
            self.assertEqual(
                processed, "schema.json",
                "Filename was not processed correctly. Expecting `schema.json` but got `{}`".format(processed))

    def test_missing_schema(self):
        """Ensures correct exception is raised when schema is missing."""
        for filename in ["missing.json", "not_there", "also-missing"]:
            with self.assertRaises(FileNotFoundError):
                is_valid({}, filename)

    def test_validation(self):
        """Validates fixtures against schemas.

        Uses a variety of fixtures to ensure that validation (and invalidation)
        takes place as expected.
        """
        for object_type in listdir(join(fixtures_dir, "valid")):
            for f in listdir(join(fixtures_dir, "valid", object_type)):
                with open(join(fixtures_dir, "valid", object_type, f), "r") as df:
                    data = json.load(df)
                    is_valid(data, object_type)
        for object_type in listdir(join(fixtures_dir, "invalid")):
            for f in listdir(join(fixtures_dir, "invalid", object_type)):
                with open(join(fixtures_dir, "invalid", object_type, f), "r") as df:
                    print(f)
                    data = json.load(df)
                    with self.assertRaises(
                            ValidationError,
                            msg="{} was not marked as invalid.".format(join(fixtures_dir, "invalid", object_type, f))):
                        is_valid(data, object_type)

    def test_input(self):
        """Checks TypeError exception is raised when input data is not a dict."""
        for data in ["string", ["this", "is", "a", "list"]]:
            for schema in listdir(schemas_dir):
                with self.assertRaises(TypeError):
                    is_valid(data, schema)
