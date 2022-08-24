import json
import unittest
from os import listdir
from os.path import abspath, dirname, join

from rac_schema_validator import is_valid
from rac_schema_validator.exceptions import ValidationError

base_path = dirname(dirname(abspath(__file__)))

schemas_dir = join(base_path, "schemas")
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

    def test_validation(self):
        """Validates fixtures against schemas.

        Uses a variety of fixtures to ensure that validation (and invalidation)
        takes place as expected.
        """
        with open(join(schemas_dir, 'base.json'), 'r') as base_file:
            base_schema = json.load(base_file)
            for object_type in listdir(join(fixtures_dir, "valid")):
                with open(join(schemas_dir, f'{object_type}.json'), 'r') as object_file:
                    object_schema = json.load(object_file)
                    for f in listdir(join(fixtures_dir, "valid", object_type)):
                        with open(join(fixtures_dir, "valid", object_type, f), "r") as df:
                            data = json.load(df)
                            is_valid(data, object_schema, base_schema)
            for object_type in listdir(join(fixtures_dir, "invalid")):
                with open(join(schemas_dir, f'{object_type}.json'), 'r') as object_file:
                    object_schema = json.load(object_file)
                    for f in listdir(
                            join(fixtures_dir, "invalid", object_type)):
                        with open(join(fixtures_dir, "invalid", object_type, f), "r") as df:
                            data = json.load(df)
                            with self.assertRaises(
                                    ValidationError,
                                    msg="{} was not marked as invalid.".format(join(fixtures_dir, "invalid", object_type, f))):
                                is_valid(data, object_schema, base_schema)
